# 한 줄씩 입력을 받네? 나는 max 뽑아내기도 편하고, index 뽑기도 편하게 list로 만들어주자는 아이디어

list = []

for _ in range(0,9):
    list.append(int(input()))

big = max(list)
print(big)
print(list.index(big)+1)











