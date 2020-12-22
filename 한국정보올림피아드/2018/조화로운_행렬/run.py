

def acmic_solution():
    R, C = map(int, input().strip().split())
    mat = [list(map(int, input().strip().split())) for _ in range(R)]
    for r in range(R):
        row = [(i, e) for i,e in enumerate(mat[r])]
        row_sorted = sorted(row, key=lambda x:-x[1])
        for c in range(C):
            mat[r][row_sorted[c][0]] = c+1

    count = 0
    for c in range(C):
        same = True 
        for r in range(R-1):
            if mat[r][c] != mat[r+1][c]:
                same = False 
                break 
        if same:
            count +=1 
    print(count)
    for i in range(R):
        print(mat[i])

def main():
    acmic_solution()


if __name__=="__main__":
    main()