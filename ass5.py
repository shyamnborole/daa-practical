def main():
    n = int(input())
    r = int(input())
    c = int(input())
    chess = [[0 for i in range(n)] for j in range(n)]
    printknightsTour(chess, r, c, 0)

def printknightsTour(chess, r, c, move):
    if r < 0 or c < 0 or r >= len(chess) or c >= len(chess) or chess[r][c] > 0:
        return
    elif move == len(chess) * len(chess) - 1:
        chess[r][c] = move
        displayBoard(chess)
        exit()
    if move < len(chess) * len(chess) - 1:
        chess[r][c] = move
        printknightsTour(chess, r - 2, c + 1, move + 1)
        printknightsTour(chess, r - 1, c + 2, move + 1)
        printknightsTour(chess, r + 1, c + 2, move + 1)
        printknightsTour(chess, r + 2, c + 1, move + 1)
        printknightsTour(chess, r + 2, c - 1, move + 1)
        printknightsTour(chess, r + 1, c - 2, move + 1)
        printknightsTour(chess, r - 1, c - 2, move + 1)
        printknightsTour(chess, r - 2, c - 1, move + 1)
        chess[r][c] = 0

def displayBoard(chess):
    for i in range(len(chess)):
        for j in range(len(chess[0])):
            print(chess[i][j], end=" ")
        print()
    print()

main()