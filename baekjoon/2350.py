A,B,C = map(int, input().split())
cook_time = int(input())
print(A,B,C)
print(cook_time)

B1 = int((cook_time + C) / 60)
if B1 > 60:
    B1 = B1/60 
C1 = int((cook_time + C) % 60)
A1 = int((B1 + B) / 60)


print(A1, B1, C1)