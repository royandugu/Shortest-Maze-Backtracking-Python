a=[
    [1,1,1,1,1,0,0,1,1,1],
    [0,1,1,1,1,1,0,1,0,1],
    [0,0,1,0,1,1,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,0,0,1,1,0],
    [0,0,0,0,1,0,0,1,0,1],
    [0,1,1,1,1,1,1,1,0,0],
    [1,1,1,1,1,0,0,1,1,1],
    [0,0,1,0,0,1,1,0,0,1]
]
def shortest_path(i,j,x,y):
    rows=len(a)
    cols=len(a[0])
    vis=[    
        [False,False,False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False,False,False],
        [False,False,False,False,False,False,False,False,False,False]
    ]
    return shortest_path_main(i, j, x, y, vis)

def is_valid(i,j,vis):
    rows=len(a)
    cols=len(a[0])
    return i>=0 and j>=0 and i<rows and j<cols and a[i][j]==1 and not vis[i][j]

def shortest_path_main(i,j,x,y,vis):
    if(not is_valid(i, j, vis)):
        return 1000
    if i==x and j==y:
        return 0
    vis[i][j]=True
    left=shortest_path_main(i, j-1, x, y, vis)+1
    bottom=shortest_path_main(i+1, j, x, y, vis)+1
    right=shortest_path_main(i, j+1, x, y, vis)+1
    top=shortest_path_main(i-1, j, x, y, vis)+1
    
    vis[i][j]=False
    return min(min(left,bottom),min(right,top))

result=shortest_path(0, 0, 8, 0)
print(result)