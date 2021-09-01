# Darren Browne - 01/09/2021 - 3:00am

puzzle = [[5, 0, 0, 4, 6, 7, 3, 0, 9],
          [9, 0, 3, 8, 1, 0, 4, 2, 7],
          [1, 7, 4, 2, 0, 3, 0, 0, 0],
          [2, 3, 1, 9, 7, 6, 8, 5, 4],
          [8, 5, 7, 1, 2, 4, 0, 9, 0],
          [4, 9, 6, 3, 0, 8, 1, 7, 2],
          [3, 0, 0, 0, 8, 9, 2, 6, 0],
          [7, 8, 2, 6, 4, 1, 0, 0, 5],
          [0, 1, 0, 0, 0, 0, 7, 0, 8]]

solved = [[5, 2, 8, 4, 6, 7, 3, 1, 9],
          [9, 6, 3, 8, 1, 5, 4, 2, 7],
          [1, 7, 4, 2, 9, 3, 5, 8, 6],
          [2, 3, 1, 9, 7, 6, 8, 5, 4],
          [8, 5, 7, 1, 2, 4, 6, 9, 3],
          [4, 9, 6, 3, 5, 8, 1, 7, 2],
          [3, 4, 5, 7, 8, 9, 2, 6, 1],
          [7, 8, 2, 6, 4, 1, 9, 3, 5],
          [6, 1, 9, 5, 3, 2, 7, 4, 8]]


def print_sudoku(sud):
    string = ""
    for i in range(0, 9):
        if i % 3 == 0:
            print("-------------------------")
        for j in range(0, 9):
            if j == 0:
                string += str(sud[i][j]) + " "
                continue
            if (j == 3) or (j == 6):
                string += "| " + str(sud[i][j]) + " "
            elif j == 8:
                string += str(sud[i][j]) + " "
                print("| " + string + "|")
                string = ""
            else:
                string += str(sud[i][j]) + " "
    print("-------------------------")


def solve(sud):
    lst = []
    for i in range(0, 9):
        ilst = []
        for j in range(0, 9):
            if sud[i][j] != 0:
                ilst.append([sud[i][j]])
            else:
                inlst = []
                for x in range(1, 10):
                    if x not in sud[i]:
                        newlst = []
                        for q in range(0, 9):
                            newlst.append(sud[q][j])
                        if x not in newlst:
                            if i < 3:
                                ii = 0
                            elif i < 6:
                                ii = 3
                            else:
                                ii = 6
                            if j < 3:
                                jj = 0
                            elif j < 6:
                                jj = 3
                            else:
                                jj = 6
                            newLst = []
                            for g in range(0, 3):
                                for h in range(0, 3):
                                    newLst.append(sud[ii + g][jj + h])
                            if x not in newlst:
                                inlst.append(x)
                ilst.append(inlst)
        lst.append(ilst)
    while(True):
        sud = lst
        lst = []
        for i in range(0, 9):
            ilst = []
            for j in range(0, 9):
                if len(sud[i][j]) == 1:
                    ilst.append(sud[i][j])
                else:
                    noList = []
                    ist = []
                    for x in range(0, 9):
                        if len(sud[i][x]) == 1:
                            noList.append(sud[i][x][0])
                    for z in sud[i][j]:
                        if z not in noList:
                            newlst = []
                            for q in range(0, 9):
                                if len(sud[q][j]) == 1:
                                    newlst.append(sud[q][j][0])
                            if z not in noList:
                                if i < 3:
                                    g = 0
                                elif i < 6:
                                    g = 3
                                else:
                                    g = 6
                                if j < 3:
                                    h = 0
                                elif j < 6:
                                    h = 3
                                else:
                                    h = 6
                                llst = []
                                for qq in range(0, 3):
                                    for jj in range(0, 3):
                                        if len(sud[qq + g][jj + h]) == 1:
                                            llst.append(sud[qq + g][jj + h][0])
                                if z not in llst:
                                    ist.append(z)
                    ilst.append(ist)
            lst.append(ilst)
        puz = []
        fin = True
        for i in range(0, 9):
            inPuz = []
            for j in range(0, 9):
                if len(lst[i][j]) != 1:
                    fin = False
                else:
                    inPuz.append(lst[i][j][0])
            puz.append(inPuz)
        if fin:
            print_sudoku(puz)
            break


if __name__ == "__main__":
    print("Pre Solve:")
    print_sudoku(puzzle)

    print("Post Solve:")
    solve(puzzle)
