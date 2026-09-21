def check_error(board):
    count_error = 0
    count_K = 0
    for i in range(0,len(board),1):
        if abs(len(board[i])-len(board)) >= 1:
            count_error += 1
    for row in board:
        for col in row:
            if col == "K":
                count_K += 1
    if count_K != 1:
        count_error += 1
    return count_error


def block(board, row1, col1, rowK, colK):
    if row1 == rowK:
        direct_row = 0
    else:
        if rowK > row1:
            direct_row = 1
        else:
            direct_row = -1

    if col1 == colK:
        direct_col = 0
    else:
        if colK > col1:
            direct_col = 1
        else:
            direct_col = -1
    
    row = row1 + direct_row
    col = col1 + direct_col

    while (row, col) != (rowK, colK):
        if board[row][col] in ["R","P","B","Q","K"]:
            return False
        row += direct_row
        col += direct_col
    return True


def checkmate(board):
    board_spl = board
    if check_error(board_spl) >= 1:
        print("Error")
        return
    
    positions = {
    "r": None,"p": None,"b": None,"q": None,"k": None
    }

    have = {
    "r": 0,"p": 0,"b": 0,"q": 0,"k": 0
    }

    sus = 0
    fail = 0

    for i in range(0,len(board_spl),1):
        for j in range(0,len(board_spl[i]),1):
            if board_spl[i][j] in ["R","P","B","Q","K"]:
                if board_spl[i][j] == "R":
                    have["r"] += 1
                    positions["r"] = (i,j)
                elif  board_spl[i][j] == "P":
                    have["p"] += 1
                    positions["p"] = (i,j)
                elif  board_spl[i][j] == "B":
                    have["b"] += 1
                    positions["b"] = (i,j)
                elif  board_spl[i][j] == "Q":
                    have["q"] += 1
                    positions["q"] = (i,j)
                elif  board_spl[i][j] == "K":
                    have["k"] += 1
                    positions["k"] = (i,j)
    if have["p"] > 0:
        """pawn"""
        if abs(positions["p"][1] - positions["k"][1]) == 1 and positions["p"][0] - positions["k"][0] == 1:
            """หา p จาก เอาตำแหน่ง col_p +- cal_k ต้องได้ 1 และ row_p +- row_k ก็ต้องได้ 1 เพราะ ตำแหน่งชนะมันอยู่ ซ้ายบน ขวาบน"""
            sus += 1
    else:
        fail += 1
    if have["b"] > 0:
        """Bishop"""
        if abs(positions["b"][0] - positions["k"][0]) == abs(positions["b"][1] - positions["k"][1]) \
            and block(board_spl, positions["b"][0], positions["b"][1], positions["k"][0], positions["k"][1]):
            """ชนะโดยแนวแทยงซ้ายขวา หาจาก row_b +- row_k เท่ากันกับ col_b - col_k เพราะว่าเวลาคิด หาก b อยู่(3,3) K อยู่ที่ (2,2) โดยคิดคือ row ลบกันเท่ากับ 1 และ col ลบกัน = 1 ดังนั้น 1=1 ก็ถูก """
            sus += 1
    else:
        fail += 1
    if have["r"] > 0:
        """rook"""
        if ((positions["r"][0] == positions["k"][0]) or (positions["r"][1] == positions["k"][1])) \
            and block(board_spl, positions["r"][0], positions["r"][1], positions["k"][0], positions["k"][1]):

            """ชนะโดย แถวแนวนอนและแถวแนวตั้ง หาจาก row_r เท่ากับ row_k หรือ col_r เท่ากับ col_k"""
            sus += 1
    else:
        fail += 1
    if have["q"] > 0:
        """queen"""
        if (positions["q"][0] == positions["k"][0] or positions["q"][1] == positions["k"][1] \
            or abs(positions["q"][0] - positions["k"][0]) == abs(positions["q"][1] - positions["k"][1])) \
        and block(board_spl, positions["q"][0], positions["q"][1], positions["k"][0], positions["k"][1]):
            """ได้ทั้งแทยงและแนวตั้วแนวนอน คือ r หรือ b"""
            sus += 1
    else:
        fail += 1

    if sus >= 1:
        print("Success")
    elif fail >= 1:
        print("Fail")
    else:
        print("Error")