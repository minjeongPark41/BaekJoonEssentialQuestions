N = int(input())
num = list(map(int, input().split()))

small = min(num)
big = max(num)

# print(small, ' ', big)
#  가운데 ' ' 해주면 두 칸 띄어줘서 나와서 생략하고 그냥 하자.
print(small, big)