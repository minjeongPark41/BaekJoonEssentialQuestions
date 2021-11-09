a, b = map(int, input().split())

if a > b :
    print('>')
if a <b : 
    print('<')
if a == b : 
    print('=')

# if, elif, else로 해주자

# 삼항 연산자
print ('>') if a > b else print('<') if a < b else print('==')