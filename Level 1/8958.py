N = int(input())

for i in range(1, N+1):
    text = list(input())
    # 받은 걸 list화 해줘야. 그래야 아래 for문도 돌 수 있음

    # O에 대한 점수 
    sum = 0
    # 이게 복병!
    c = 1

    for i in text:
        if i == 'O':
            sum += c
            # 그리고 만약 또 O라면 1을 더 해줘야하니까
            c += 1
        else:
            c = 1
    print(sum)