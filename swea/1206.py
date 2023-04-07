n = int(input())
N = list(map(int,input().split()))

building = []

for i in range(len(N)):
    Nr1 = N[i] - N[i+1]
    Nr2 = N[i] - N[i+2]
    Nl1 = N[i] - N[i-1]
    Nl2 = N[i] - N[i-2]

    if Nr1 >= 2 and Nr2 >= 2 and Nl1 >= 2 and Nl2 >= 2:
        building.append(N[i])
    elif Nr1 >= 2 and 2> Nr2 >= 1:



