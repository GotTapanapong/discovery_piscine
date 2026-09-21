from checkmate_input import checkmate
def main():
    print("Input Row of Board :")
    row = int(input())
    print("Input Board :")
    board = []
    for i in range(0,row,1):
        board.append(list(input()))
    checkmate(board)
if __name__ == "__main__":
    main()