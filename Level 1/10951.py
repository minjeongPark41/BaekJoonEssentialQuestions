"""
해당 문제는 입력 개수에 제한이 없음.
따라서 try ... except 으로, 두 수가 입력되지 않는 경우에 반복문이 끝나도록

"""

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break