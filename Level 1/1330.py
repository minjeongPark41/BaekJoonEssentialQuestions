a, b = map(int, input().split())

if a > b :
    print('>')
elif a <b : 
    print('<')
else:
    print('==')

# if, elif, else로 해주자

# 삼항 연산자
print ('>') if a > b else print('<') if a < b else print('==')