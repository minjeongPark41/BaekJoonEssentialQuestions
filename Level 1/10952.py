# 고맙게도! 무한루프 나올 수 있도록 조건이 주어진건데 사용해야지~~ 

while True:
    a, b = map(int, input().split())
    # print(a+b) 이게 여기 나오면 안되는 이유는 0, 0일때 0을 print하는게 아니라 그만둬야 하니

    if a==0 and b==0:
        break;

    else:
        print(a+b)
    
    
