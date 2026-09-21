#!/usr/bin/env python3

from checkmate import checkmate

def main():
    # Test Case 1 (from PDF example)
    board1 = """\
R...
.K..
..P.
....\
"""
    print("Test 1 (from PDF example):")
    checkmate(board1)
    
    # Test Case 2 (from PDF example)
    board2 = """\
..
.K\
"""
    print("Test 2 (from PDF example):")
    checkmate(board2)
    
    # Test Case 3: Pawn attack
    board3 = """\
....
....
..K.
...P\
"""
    print("Test 3 (Pawn attack):")
    checkmate(board3)
    
    # Test Case 4: Bishop attack
    board4 = """\
...K
....
.B..
....\
"""
    print("Test 4 (Bishop attack):")
    checkmate(board4)
    
    # Test Case 5: Rook attack
    board5 = """\
....
.K..
....
.R..\
"""
    print("Test 5 (Rook attack):")
    checkmate(board5)
    
    # Test Case 6: Queen attack
    board6 = """\
....
....
Q...
K...\
"""
    print("Test 6 (Queen attack):")
    checkmate(board6)

    # Test Case 7: No attack
    board7 = """\
....
...K
....
....\
"""
    print("Test 7 (No attack):")
    checkmate(board7)

    #Not square
    board8 = """\
....
.K..
.....\
"""
    print("Test 8 (Not Square):")
    checkmate(board8)

    # Test Case 9: 10x10 board with Rook check
    board9 = """\
........BP
..........
Q.........
..........
..........
..........
..........
R.........
..........
K........P\
"""
    print("Test 9 (10x10 Rook check):")
    checkmate(board9)

    #No board
    board10 = """"""
    print("Test 10 (No board):")
    checkmate(board10)

main()
