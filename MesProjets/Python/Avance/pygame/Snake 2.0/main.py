import pygame
import random
import math
from ai import ai_next_move

# --- CONFIG ---
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 24
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

SNAKE_COLORS = [(0, 255, 90), (90, 120, 255)]
GLOW_COLORS = [(0, 180, 60, 80), (60, 80, 220, 80)]
BG_TOP = (30, 40, 60)
BG_BOTTOM = (10, 20, 30)

LEVELS = [
    {"name": "Niveau 1 (Très facile)", "fps": 4, "fps_max": 8},
    {"name": "Niveau 2 (Facile)", "fps": 6, "fps_max": 12},
    {"name": "Niveau 3 (Normal)", "fps": 8, "fps_max": 16},
    {"name": "Niveau 4 (Difficile)", "fps": 11, "fps_max": 20},
    {"name": "Niveau 5 (Expert)", "fps": 15, "fps_max": 28},
]

WIN_CONDITIONS = [10, 25, 50, 100, 200]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake V2.2 – Duel")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 32, bold=True)
font_small = pygame.font.SysFont("consolas", 24, bold=True)

def draw_gradient_background():
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio
        g = BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio
        b = BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio
        pygame.draw.line(screen, (int(r), int(g), int(b)), (0, y), (WIDTH, y))

def draw_cell(pos, color, glow_color=None):
    x, y = pos
    px, py = x * CELL_SIZE, y * CELL_SIZE
    if glow_color:
        s = pygame.Surface((CELL_SIZE*2, CELL_SIZE*2), pygame.SRCALPHA)
        pygame.draw.ellipse(s, glow_color, (0, 0, CELL_SIZE*2, CELL_SIZE*2))
        screen.blit(s, (px - CELL_SIZE//2, py - CELL_SIZE//2))
    pygame.draw.rect(screen, color, (px+2, py+2, CELL_SIZE-4, CELL_SIZE-4), border_radius=8)

def spawn_apple(snake1, snake2, apples):
    while True:
        pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
        if pos not in snake1 and pos not in snake2 and pos not in apples:
            return pos

def draw_scoreboard(score1, score2, win_score):
    leader = 0 if score1 > score2 else 1 if score2 > score1 else -1
    s1 = font.render(f"Joueur 1: {score1}", True, SNAKE_COLORS[0])
    s2 = font.render(f"Joueur 2: {score2}", True, SNAKE_COLORS[1])
    win_txt = font_small.render(f"Score à atteindre : {win_score}", True, (255,255,180))
    bg1 = pygame.Surface((s1.get_width()+20, s1.get_height()+10), pygame.SRCALPHA)
    bg2 = pygame.Surface((s2.get_width()+20, s2.get_height()+10), pygame.SRCALPHA)
    if leader == 0:
        pygame.draw.rect(bg1, (255,255,255,60), bg1.get_rect(), border_radius=12)
    elif leader == 1:
        pygame.draw.rect(bg2, (255,255,255,60), bg2.get_rect(), border_radius=12)
    screen.blit(bg1, (40, 20))
    screen.blit(bg2, (WIDTH - s2.get_width() - 60, 20))
    screen.blit(s1, (50, 25))
    screen.blit(s2, (WIDTH - s2.get_width() - 50, 25))
    screen.blit(win_txt, (WIDTH//2 - win_txt.get_width()//2, 25))

def increase_difficulty(level, apples, fps, fps_max):
    if level % 10 == 0 and fps < fps_max:
        fps += 1
    if level % 7 == 0 and len(apples) < 3:
        apples.append(spawn_apple([], [], apples))
    return apples, fps

class Snake:
    def __init__(self, color, glow, start_pos, direction):
        self.body = [start_pos]
        self.dir = direction
        self.grow = False
        self.alive = True
        self.color = color
        self.glow = glow

    def move(self):
        if not self.alive:
            return
        dx, dy = self.dir
        nx, ny = self.body[0][0] + dx, self.body[0][1] + dy
        nx = nx % GRID_WIDTH
        ny = ny % GRID_HEIGHT
        new_head = (nx, ny)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def set_direction(self, d):
        if (d[0] == -self.dir[0] and d[1] == -self.dir[1]):
            return
        self.dir = d

    def eat(self):
        self.grow = True

    def draw(self):
        for i, pos in enumerate(self.body):
            if i == 0:
                draw_cell(pos, self.color, self.glow)
            else:
                draw_cell(pos, self.color)

def menu():
    mode = 0  # 0 = IA, 1 = 2P
    level = 2  # par défaut niveau 3 (normal)
    win_idx = 2  # par défaut 50 points
    selected = 0  # 0 = mode, 1 = niveau, 2 = win, 3 = jouer
    running = True

    while running:
        draw_gradient_background()
        title = font.render("Snake V2.2", True, (255,255,255))
        screen.blit(title, (WIDTH//2-title.get_width()//2, 60))

        # Mode de jeu
        m1 = font_small.render("Mode :", True, (220,220,220))
        mode_ia = font_small.render("1. Joueur vs IA", True, (180,255,180) if mode==0 else (120,140,120))
        mode_2p = font_small.render("2. Joueur vs Joueur", True, (180,180,255) if mode==1 else (120,140,120))
        screen.blit(m1, (WIDTH//2-200, 150))
        screen.blit(mode_ia, (WIDTH//2-100, 150))
        screen.blit(mode_2p, (WIDTH//2+120, 150))

        # Niveau
        n1 = font_small.render("Niveau :", True, (220,220,220))
        for i, lvl in enumerate(LEVELS):
            color = (255,255,120) if i == level else (140,140,80)
            txt = font_small.render(f"{i+1}", True, color)
            screen.blit(txt, (WIDTH//2-90+50*i, 210))
        lvl_name = font_small.render(LEVELS[level]["name"], True, (255,255,255))
        screen.blit(n1, (WIDTH//2-200, 210))
        screen.blit(lvl_name, (WIDTH//2-80, 250))

        # Condition de victoire
        win1 = font_small.render("Score pour gagner :", True, (220,220,220))
        for i, val in enumerate(WIN_CONDITIONS):
            color = (255,180,180) if i == win_idx else (140,80,80)
            txt = font_small.render(f"{val}", True, color)
            screen.blit(txt, (WIDTH//2-50+70*i, 310))
        screen.blit(win1, (WIDTH//2-300, 310))

        # Bouton jouer
        play_color = (255,255,255) if selected==3 else (180,180,180)
        play = font.render("Appuie sur ENTRÉE pour jouer", True, play_color)
        screen.blit(play, (WIDTH//2-play.get_width()//2, 400))

        # Sélections visuelles
        if selected == 0:
            pygame.draw.rect(screen, (255,255,255,60), (WIDTH//2-120, 145, 10, 30), border_radius=8)
        elif selected == 1:
            pygame.draw.rect(screen, (255,255,255,60), (WIDTH//2-100, 205, 10, 30), border_radius=8)
        elif selected == 2:
            pygame.draw.rect(screen, (255,255,255,60), (WIDTH//2-90, 305, 10, 30), border_radius=8)
        elif selected == 3:
            pygame.draw.rect(screen, (255,255,255,60), (WIDTH//2-play.get_width()//2-10, 395, play.get_width()+20, 45), border_radius=8)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_DOWN, pygame.K_TAB):
                    selected = (selected + 1) % 4
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % 4
                if selected == 0:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_1:
                        mode = 0
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_2:
                        mode = 1
                if selected == 1:
                    if event.key == pygame.K_LEFT and level > 0:
                        level -= 1
                    if event.key == pygame.K_RIGHT and level < 4:
                        level += 1
                    if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5):
                        level = int(event.unicode)-1
                if selected == 2:
                    if event.key == pygame.K_LEFT and win_idx > 0:
                        win_idx -= 1
                    if event.key == pygame.K_RIGHT and win_idx < len(WIN_CONDITIONS)-1:
                        win_idx += 1
                if selected == 3 and event.key == pygame.K_RETURN:
                    return mode, level, WIN_CONDITIONS[win_idx]

def main():
    mode, level, win_score = menu()
    FPS_START = LEVELS[level]["fps"]
    FPS_MAX = LEVELS[level]["fps_max"]

    snake1 = Snake(SNAKE_COLORS[0], GLOW_COLORS[0], (GRID_WIDTH//4, GRID_HEIGHT//2), (1,0))
    snake2 = Snake(SNAKE_COLORS[1], GLOW_COLORS[1], (3*GRID_WIDTH//4, GRID_HEIGHT//2), (-1,0))
    apples = [spawn_apple(snake1.body, snake2.body, [])]
    score1 = score2 = 0
    fps = FPS_START
    lvl_counter = 0

    running = True
    winner = None
    while running:
        clock.tick(fps)
        lvl_counter += 1
        apples, fps = increase_difficulty(lvl_counter, apples, fps, FPS_MAX)
        # --- Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Joueur 1 (flèches)
                if event.key == pygame.K_UP:    snake1.set_direction((0,-1))
                if event.key == pygame.K_DOWN:  snake1.set_direction((0,1))
                if event.key == pygame.K_LEFT:  snake1.set_direction((-1,0))
                if event.key == pygame.K_RIGHT: snake1.set_direction((1,0))
                # Joueur 2 (ZQSD ou WASD)
                if mode == 1:
                    if event.key in (pygame.K_w, pygame.K_z): snake2.set_direction((0,-1))
                    if event.key == pygame.K_s: snake2.set_direction((0,1))
                    if event.key == pygame.K_a: snake2.set_direction((-1,0))
                    if event.key == pygame.K_d: snake2.set_direction((1,0))

        # --- AI Move
        if mode == 0:
            snake2.set_direction(ai_next_move(snake2, snake1, apples, GRID_WIDTH, GRID_HEIGHT))

        # --- Move snakes
        snake1.move()
        snake2.move()

        # --- Eat apples
        for apple in apples[:]:
            if snake1.body[0] == apple:
                snake1.eat()
                apples.remove(apple)
                apples.append(spawn_apple(snake1.body, snake2.body, apples))
                score1 += 1
            elif snake2.body[0] == apple:
                snake2.eat()
                apples.remove(apple)
                apples.append(spawn_apple(snake1.body, snake2.body, apples))
                score2 += 1

        # --- Condition de victoire
        if score1 >= win_score:
            winner = "Joueur 1"
            running = False
        elif score2 >= win_score:
            winner = "Joueur 2" if mode == 1 else "IA"
            running = False

        # --- Draw
        draw_gradient_background()
        for apple in apples:
            pygame.draw.ellipse(screen, (255,60,60), (apple[0]*CELL_SIZE+6, apple[1]*CELL_SIZE+6, CELL_SIZE-12, CELL_SIZE-12))
        snake1.draw()
        snake2.draw()
        draw_scoreboard(score1, score2, win_score)
        pygame.display.flip()

    # --- End screen
    msg = font.render(f"{winner} gagne !", True, (255,255,255))
    screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2))
    pygame.display.flip()
    pygame.time.wait(2500)
    pygame.quit()

if __name__ == "__main__":
    main()