# bfs 탐색
# 뒤에서부터 출발하자
# 처음에 bfs 탐색하면서
# 지금까지 남은횟수 1
# 출발점이 막힌 경우에는 상하좌우 2칸 까지랑 대각선 탐색하고 길 일ㅆ으면 파괴해
# 남은횟수 0으로 바꿔줘
# 그리고 탐색
# 탐색하면서 다시 완전히 막혔을 때 남은 횟수가 없으면 못가는 거니까-1
# 그리고 일반적으로 길을 따라가면서 이 점에서 뚫을 곡이 있는 지 화ㄱ인해줘
# 뚫어도 되는 곳이면 지금까지 몇칸 갔느지를 넣어주고 가
# 벽에도
import sys

def bfs(r,c):
    pass

N, M = int(sys.stdin.readline().split())
# 부술수 있는 횟수
crush = 1
maze = [list(sys.stdin.readline()) for _ in range(N)]

# 출발지점에서 탐색 시작
bfs(0.0)