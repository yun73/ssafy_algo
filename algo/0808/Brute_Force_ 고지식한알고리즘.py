# 본문 문자열과 찾을 문자열을 비교하며 각각의 인덱스를 계속 조작해준다
# 찾을 문자열의 첫 문자와 같으면 둘다 인덱스 올려서 비교
# 실패하면은 찾을 문자열의 인덱스는 초기화 하고
# 본문 문자열의 인덱스는 1칸 이동하여 다시 비교

p = 'is'
t = 'This is a book~!'
M = len(p)  # 찾을 패턴의 길이
N = len(t)  # 전체 텍스트의 길이


def BruteForce(p, t):
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while j < M and i < N:  # 못찾고 j가 M보다 커져도 종료, i이 N 이랑 같아지면 찾은거임
        if t[i] != p[j]:
            i = i - j  # 실패하면 지금까지 검사한만큼 다시 돌아감
            j = -1  # 실패하면 j 값 -1 초기화 다음구문에서 다시 0됨
        i += 1  # 다를때 +1하면 다음칸 부터 시작, 같을 때 1증가하여 비교
        j += 1

    if j == M:
        return i - M
    else:
        return -1
