T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    n = len(arr)  # n 집합의 원소의 개수

    # 모든 부분 집합 검사
    # 1<<n 부분집합의 개수 2*n 이랑 똑같은 거임 2^6 == 1<<6 == 1*2^6
    for i in range(1 << n):  # 부분 집합의 개수만큼 반복
        # i 번째 부분집합을 검사하겠다
        # i 번째 부분집합이 n개의 원소 중에 j 번쨰 원소를 포함하는지
        sum_subset = 0  # 부분집합의 합 초기화
        for j in range(n):  # 원소의 수만큼 비트를 비교 3<<4 == 3 * 2^4
            if i & (1 << j):  # 부분집합 i가 j번째 원소를 포함했는지 비트가 1인 경우
                sum_subset += arr[j]
                print(arr[j], end=', ')  # j 번 원소 출력
        if sum_subset == 0:
            answer = 1
            print(answer)
            break
        print()

    # i는 1,2,3,4...,2^n 개 까지 반복 부분집합의 개수가 2^n 개인데
    # 각 i를 2진수로 나타내면 0001,0010, 0011, 0100 과 같음
    # 이떄 주어진 원소가 [1,2,3,4] 라면 j를 n만큼 미는걸 반복할때
    # 0001, 0010, 0100, 1000 처럼 밀게 되는데
    # 부분집합 i에서 j번 민 자리에 같이 1이 있다면 arr에서 j 번째 자리에[ 위치하는 숫자를
    # 추가
    # 예를들어 i > 0101 일 때 j은 0, 2 일 때 i에 포함됨 따라서 반환되는 부분집합은 1,3

