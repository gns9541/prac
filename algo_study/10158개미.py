w, h = map(int, input().split())  # 격자 크기 가로 세로 6 4 6 4
p, q = map(int, input().split())  # 개미 시작 위치 4 1 5 3
t = int(input()) # 개미 움직인 시간 8 4

a = abs(t-(w-p)) # 6 3       시간 - (가로에서 시작위치)
b = abs(t-(h-q)) # 5 3
a1 = int(a/w)
a2 = a%w
b1 = int(b/h)
b2 = b%h

if a1%2 == 0:
    p = w-a2
if a1%2 != 0:
    p = a2
if b1%2 == 0:
    q = h-b2
if b1%2 != 0:
    q = b2
print(p, q)         
 
