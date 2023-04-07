def find_set(n):
    if n==p[n]:
        return n
    p[n]=find_set(p[n])
    return p[n]

def union(s,e):
    p[find_set(e)] = find_set(s)


def kruskal():
    cnt = ret = 0
    for (s,e,w) in arr:
        if find_set(s)!=find_set(e):
            union(s,e)
            ret += w
            cnt+=1
            if cnt == V:
                return ret
    return -1


T = int(input())
for test_case in range(1, T + 1):
    V,E = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]

    arr.sort(key=lambda x: x[2])
    p = [n for n in range(V + 1)]
    ans = kruskal()
    print(f"#{test_case} {ans}")