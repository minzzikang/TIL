dr = [-1,1,0,0]
dc = [0,0,-1,1]
def find_start():
    for r in range(H):
        for c in range(W):
            if game_map[r][c] in ['^', 'v', '<', '>']:
                return r, c, game_map[r][c]

def battle():
    sr, sc, direction = find_start()

    for i in range(N):
        # 포탄쏘기
        if user[i] == 'S':
            if direction == '^':
                # 같은 방향으로 쭉 나감(벽 만나기 전까지)
                for j in range(sr, H):
                    if game_map[j][sc] == '*':  # 벽돌인 경우
                        game_map[j][sc] = '.'
                        break
                    elif game_map[j][sc] == '#':  # 강철인 경우
                        break

            if direction == 'v':
                # 같은 방향으로 쭉 나감(벽 만나기 전까지)
                for j in range(sr, H):
                    if game_map[j][sc] == '*':  # 벽돌인 경우
                        game_map[j][sc] = '.'
                        break
                    elif game_map[j][sc] == '#':  # 강철인 경우
                        break

            if direction == '<':
                # 같은 방향으로 쭉 나감(벽 만나기 전까지)
                for j in range(sc, W):
                    if game_map[sr][j] == '*':  # 벽돌인 경우
                        game_map[sr][j] = '.'
                        break
                    elif game_map[sr][j] == '#':  # 강철인 경우
                        break

            if direction == '>':
                # 같은 방향으로 쭉 나감(벽 만나기 전까지)
                for j in range(sc, W):
                    if game_map[sr][j] == '*':  # 벽돌인 경우
                        game_map[sr][j] = '.'
                        break
                    elif game_map[sr][j] == '#':  # 강철인 경우
                        break

        # 방향 바꾸고 이동
        elif user[i] == 'U':  # 위쪽
            direction = '^'
            nr = sr - 1
            if



T = int(input())
for tc in range(1, T+1):
    # 맵 크기 H*W
    H, W = map(int, input().split())
    game_map = [input() for _ in range(H)]
    # print(game_map)

    N = int(input())  # 입력 개수
    user = input()

    battle()

    print(f'#{tc}', *game_map)