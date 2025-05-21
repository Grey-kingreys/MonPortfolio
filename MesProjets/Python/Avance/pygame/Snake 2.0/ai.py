import random

def ai_next_move(snake, opponent, apples, grid_w, grid_h):
    head = snake.body[0]
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    # Occasionally make a mistake for human-like play
    if random.random() < 0.08:
        random.shuffle(dirs)
    # Find closest apple
    target = min(apples, key=lambda a: abs(a[0]-head[0])+abs(a[1]-head[1]))
    best = None
    min_dist = float('inf')
    for d in dirs:
        nx, ny = head[0]+d[0], head[1]+d[1]
        if (nx, ny) in snake.body or (nx, ny) in opponent.body:
            continue
        if not (0 <= nx < grid_w and 0 <= ny < grid_h):
            continue
        dist = abs(target[0]-nx) + abs(target[1]-ny)
        if dist < min_dist:
            min_dist = dist
            best = d
    if best:
        return best
    # No good move: pick any safe move
    safe = [d for d in dirs if (0 <= head[0]+d[0] < grid_w and 0 <= head[1]+d[1] < grid_h) and (head[0]+d[0], head[1]+d[1]) not in snake.body and (head[0]+d[0], head[1]+d[1]) not in opponent.body]
    if safe:
        return random.choice(safe)
    # No safe move: go forward
    return snake.dir