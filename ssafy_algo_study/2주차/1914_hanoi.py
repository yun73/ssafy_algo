N = int(input())
# A에 있는걸 3번쨰로 다 옮겨야 해
A = []
B = []
C = []
# 처음에 주어지는 원판 정리
for i in range(N,0,-1): # N부터 1까지
    A.append(i)
print(A)
# while len(C) < N:
#     while len(B) < N-1:
for n in range(len(A)-1):
    temp = A.pop() # 1 # A : 3 2
    C.append(temp)
    print(A, B, C)

K = 0 # 옮긴 횟수
# #홀수 일때 C로 먼저
# 3
# 1 3
# 1 2
# 3 2
# 1 3  # 중간 3을 c에
# 2 1
# 2 3
# 1 3
# # 짝수일 때 B로 먼저
# 4
# 1 2
# 1 3
# 2 3
# 1 2
# 3 1
# 3 2
# 1 2
# 1 3 # 4를 c에 깜
# 2 3 # 중간에 321 이전거 이써
# 2 1
# 3 1
# 2 3
# 1 2
# 1 3
# 2 3

