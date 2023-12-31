# 꽃길

# 씨앗 심으면 1년후에 꽃이 핌
# NxN 크기의 꽃밭, 씨앗을 (1,1) ~ (N,N) 지점 중 한곳에 심기 가능
# 상하좌우로 꽃잎이 생김
# 꽃 필 때 다른 꽃잎이나 꽃술과 닿게되면 죽어버리고
# 화단 밖으로 가면 죽음
# 꽃 하나당 5평의 땅 대여
# 꽃을 심기 위한 최소 비용


def bt(now,End, price):
    global visited
    global min_price

    # 종료조건 : 꽃 3개 다 심으면
    if now == End:
        if min_price > price:
            min_price = price
        return
    
    # 가지치기 : 최종 단계 가기전에 이미 값이 최소값이 아니면
    if price >= min_price:
        return
    
    # 재귀호출
    # 가장자리 안되니까 제외하고 탐색
    for r in range(1,N-1):
        for c in range(1,N-1):
            # 가능하다면
            # 일단 가격 계산
            now_price = field[r][c]
            stack = [(r,c)]
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr,nc = r+dr, c +dc
                # 다른 꽃잎이 있으면
                if visited[nr][nc]:
                    break
                now_price += field[nr][nc]
                stack.append((nr,nc))
             # 없으면
            else:
                for i,j in stack:
                    visited[i][j] += 1
                bt(now+1, End, price + now_price)
                for i,j in stack:
                    visited[i][j] -= 1


# 꽃밭 크기
N = int(input())
# 꽃밭 위치당 비용
field = [list(map(int, input().split())) for _ in range(N)]

# 꽃을 무조건 다 피게 해야하니까
# 겹치는 경우는 아이에 보지 말자
# 피면 안되는 위치 저장
visited = [[0]*(N) for _ in range(N)]
# 최소비용
min_price = 200000
# 꽃 심으러 가자
bt(0,3,0)

print(min_price)