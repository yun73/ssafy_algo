'''
전략
분할(Dvide) : 해결할 문제를 여러개의 작은 부분으로 나눔
정복(Conquer) : 나눈 작은 문제를 각각 해결
통합(Combine) : 필요하다면 해결된 해답을 모음
'''
# 거듭제곱을 구하는 알고리즘 O(n)
def Power1(Base, Exponent):
    global cnt1

    if Base == 0 : return 1
    result = 1 # Base^0 은 1이므로
    for i in range(Exponent):
        result *= Base
        cnt1 += 1
    return result

# 분할 정복 기반의 알고리즘 O(log2n)
def Power2(Base, Exponent):
    global cnt2

    if Exponent == 0 or Base == 0:
        return 1
    if Exponent % 2 == 0:
        NewBase = Power2(Base, Exponent//2)
        cnt2 += 1
        return NewBase*NewBase
    else:
        NewBase = Power2(Base, (Exponent-1)//2)
        cnt2 += 1
        return  (NewBase*NewBase)*Base

cnt1= 0
cnt2= 0
print(Power1(2, 20), cnt1)
print(Power2(2, 20), cnt2)