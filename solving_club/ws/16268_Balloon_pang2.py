import sys

sys.stdin = open('in_balloon.txt', 'r')

#N*M 의 배열
# 풍선 터뜨리면 상하좌우의 풍선 터짐
# 배열 안에 터뜨릴 수 있는 수 2이면 2번 터뜨릴 수 있음
T = int(input())

# 배열에서 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 2차 배열 탐색하며 자기자신 포함 십자가 모양으로 터뜨리기
    # 가능한 꽃가루 수 = 현재 위치 기준 십자가 안의 꽃가루 개수 다 더한값
    # 이중 최대 값 > max 값 기본 설정 후 현재 위치 갱신 할 때 마다 비교
    max_flower = 0
    for r in range(N):
        for c in range(M):
            now_flower = arr[r][c] # 현재 위치는 중심값> 중심값 총 꽃가루에 더하기
            for d in range(4): # d는 델타의 인덱스 델타는 상하좌우 이동벡터
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    now_flower += arr[nr][nc]

            if max_flower < now_flower:
                max_flower = now_flower

    print(f'#{tc} {max_flower}')




