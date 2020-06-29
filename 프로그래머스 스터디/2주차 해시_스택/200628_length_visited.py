def solution(dirs):
    answer = 0
    SIZE = 11
    check_move = [[{'U': False, 'D': False, 'R': False, 'L': False} for _ in range(SIZE)] for _ in range(SIZE)]
    opposites = {'U': 'D', 'D': 'U', 'R': 'L', 'L': 'R'}
    DELTAS = {'U': [0, 1], 'D': [0, -1], 'R': [-1, 0], 'L': [1, 0]}
    START = 5
    now_x = START
    now_y = START

    for dir in dirs:
        add_x, add_y = DELTAS[dir]
        next_x = now_x + add_x
        next_y = now_y + add_y

        if 0 <= next_x <= (SIZE - 1) and 0 <= next_y <= (SIZE - 1):
            if not check_move[now_x][now_y][dir]:
                check_move[now_x][now_y][dir] = True
                opposite = opposites[dir]
                check_move[next_x][next_y][opposite] = True
                answer += 1

            now_x = next_x
            now_y = next_y

    return answer