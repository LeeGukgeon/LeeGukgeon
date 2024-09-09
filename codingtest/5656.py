def find_optimization(eliminate, level): #모든 조합으로 구슬 떨어뜨리기
    if level == N:
        result = W * H
        for i in range(H):
            result -= eliminate[i].count(0)
        return result
    result = 10000
    for i in range(W):
        temp = find_optimization(change(eliminate, i), level + 1)
        if temp < result:
            result = temp
    return result


def change(blocks, c): # 중력
    boomed = [[False for i in range(W)] for j in range(H)]
    new_blocks = [[blocks[i][j] for j in range(W)] for i in range(H)]
    r = 0
    while r < H and blocks[r][c] == 0:
        r += 1
    if r == H:
        return new_blocks
    boom(r, c, boomed, new_blocks)
    for i in range(W): #블럭 아래로 내려서 빈칸 채우기
        upper_index = H - 1
        lower_index = H - 1
        while 0 <= lower_index and new_blocks[lower_index][i] != 0:
            upper_index -= 1
            lower_index -= 1
        if lower_index == -1:
            continue
        while 0 <= upper_index:
            if new_blocks[upper_index][i] != 0:
                new_blocks[upper_index][i], new_blocks[lower_index][i] = new_blocks[lower_index][i],new_blocks[upper_index][i]
                upper_index -= 1
                lower_index -= 1
            else:
                upper_index -= 1
    return new_blocks

def boom(r, c, boomed, new_blocks): #연쇄적으로 터트리기
    # print(r,c)
    boomed[r][c] = True
    for i in range(4):
        for l in range(1, new_blocks[r][c]):
            if (0 <= r + l * dr[i] < H) and (0 <= c + l * dc[i] < W) and boomed[r + l * dr[i]][c + l * dc[i]] == False:
                boom(r + l * dr[i], c + l * dc[i], boomed, new_blocks)
    new_blocks[r][c] = 0


T = int(input())
for tc in range(1, 1 + T):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for i in range(H)]
    print(f'#{tc} {find_optimization(blocks, 0)}')