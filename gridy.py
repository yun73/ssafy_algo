'''
공유기 설치

- 주어지는 좌표들간의
1,2,4,8,9
 1 2 4 1
- 인접한 두 공유기 사의의 거리가 최대가 되야 하므로
- 해당 두 공유기는 다른 공유기들보다 멀리 떨어져 있어야 함
- 그럼 C-1 개의 공유기를 멀리 떨어저 있게 배치한 다음 나머지 한개를 껴넣는 식으로 하면?

- 근데 멀리 4하고 9에 설치하는 경우 중간 의 거리들이 딱히 필요가 없음
- 예전에 풀었던 쭉 나열하고 그중에 가중치 몇개를 제거하는 식으로 풀리지는 않는다
- 중간값, 시작과 끝을 이용하는 이분탐색을 하면 좋을 거 같다
- 예를 들어 현재 주어진 좌표들의 범위인 1~9에서 두 공유기를 설치하는 경우는 좌우 양 끝에대 두는게 최대
- 3개인 경우는 중앙에 일단 하나 놔둬 보는게 맞다
- 근데 생각해 봐야 할게 많은 공유기를 설치할 때 공유기를 성치하는 순간 가장 인접한 공유기 두개가 바뀌수도 있는거?

- 구해야하는 가장 인접한 두 공유기의 최대거리를 인자로 하여 탐색
- 그러면 시작점부터 해당 거리로 놔두는 경우를 조사하면서 파악 가능

'''
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = [0]*N
for i in range(N):
    x = int(input())
    X[i] = x

X.sort()

if C == 2:
    print(X[-1]-X[0])
else:
    ans = 0
    left,right = 0, X[-1] - X[0]
    while left <= right:
        mid = (left+right)//2
        # 총 C 개의 위치를 선택해야 함
        cnt = 1
        # 시작점 무조건 포함
        now = X[0]
        # 전체 다 돌면서 지금 정한 최소 간격보다 커지면 구간 하나 생기는 거임
        for i in range(1,len(X)):
            if X[i] >= now + mid:
                cnt += 1
                now = X[i]

        if cnt >= C:
            ans = mid
            # 설치 가능한 공유기 개수가 C 개를 넘어가면 더 넓게 설치 가능
            left = mid + 1
        else:
            # 넘어가지 않으면 더 좁게 설치
            right = mid - 1

    print(ans)