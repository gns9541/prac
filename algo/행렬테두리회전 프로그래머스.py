rows, columns = map(int,input().split())
queries = [[1, 1, 2, 2], [1, 2, 2, 3], [1, 3, 2, 4], [2, 3, 3, 4]]


def solution(rows, columns, queries):
    arr = [[0]*(columns+1) for _ in range(rows+1)]
    n=1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            arr[i][j] = n
            n+=1
    print(*arr,sep="\n")
    print()
    answer = []
    if len(queries) == 1:
        answer.append(arr[queries[0][0]][queries[0][1]])
    else:
        for q in queries:
            arr2 = [[0]*(columns+1) for _ in range(rows+1)]
            x1=q[0] #2 세로
            y1=q[1] #2 가로
            x2=q[2] #5
            y2=q[3] #4

            di = [0,1,0,-1] #시계방향 우 하 좌 상
            dj = [1,0,-1,0]

            i=x1
            j=y1
            k = 0
            while True:
                if k == 4:
                    break
                ni, nj = i+di[k], j+dj[k]
                if (j==y1 or i==x1) or (j==y2 or i==x1) or (j==y1 or i==x2) or (j==y2 or i==x2):
                    if y1<=nj<y2+1 and x1<=ni<x2+1:
                        arr2[ni][nj] = arr[i][j]
                        i,j = ni,nj
                    else:
                        k+=1
            print(*arr2,sep="\n")
            # print()
            fin = 100000
            for i in range(1,rows+1):
                for j in range(1,columns+1):
                    if arr2[i][j] != 0:
                        if arr2[i][j]<fin:
                            fin = arr2[i][j]
                        arr[i][j] = arr2[i][j]
            # print(*arr,sep="\n") 
            print()
            answer.append(fin)
    return answer
print(solution(rows, columns, queries))




