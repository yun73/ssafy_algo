T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 20 * N 의
    # 뭐가 들어오든 하나 넣으면 다음에 ㅣ, ㅁ , ㅡ 이렇게 올 수 있고
    # ㅡ 같은 경우는 = 이렇게 쌍으로 들어와야 한다
    # 근데 하나 ㅡ 이렇게 놓으면 무조건 아래도 ㅡ인 거니까
    # 그냥 하나로 취급하되 ㅁ과는 다름
    stack = [] * N # 스택을 생성
    # top 번호가 N이랑 같으면 즉 stack이 꽉차면 경우 1 추가
    # 다시 되돌아 가면서
    frame = [] # 직사각형 채워진 모양
    top += 1 #인경우
    top += 2 #인경우
    top += 1 # * 2 #인경우

    # 채우다가 top == N 이 되면 pop 과정 반복해서
    # 새로운 경우 ㅣ 로 다 채우고 2칸 뒤로 와서 다른 경우 2가지
    # 각 경우다 했으면 2칸 더 뒤로와서

    # 그냥 규칙이 있음ㅋㅋㅋㅋ
    an = a(n-1) + 2* a(n-2)

