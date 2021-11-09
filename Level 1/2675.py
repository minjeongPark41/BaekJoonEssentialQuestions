"""
문자열 S
R번 반복
-> 새 문자열 P
"""

N = int(input())
for _ in range(0,N):
    R, S = input().split()
    R = int(R)

    # 내가 출력해줘야 하는 결과물은 '문자열'이지.
    # 이 문자열에 대한 변수를 준다. 
    result = ''
    
    for i in S:
        result += R*i
    print(result)