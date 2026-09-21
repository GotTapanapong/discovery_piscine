#!/usr/bin/env python3

# (0, 1) คือไปทางขวา, (0, -1) คือไปทางซ้าย, (1, 0) คือลงล่าง, (-1, 0) คือขึ้นบน
rook_dirs   = [(0,1), (0,-1), (1,0), (-1,0)]
# ทิศทางแนวทแยงทั้ง 4 มุม 
bishop_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]
# Queen สามารถเดินได้ทั้งแบบ Rook และ Bishop รวมกัน
queen_dirs  = rook_dirs + bishop_dirs

def king_position(board):
    """ ค้นหาตำแหน่งพิกัด (แถว, คอลัมน์) ของพระราชา (K) บนกระดาน """
    lines = board.strip().split('\n')
    for r, row in enumerate(lines):
        for c, piece in enumerate(row):
            if piece == 'K':
                return r, c
    return None

def is_valid(r, c, lines):
    """ ตรวจสอบว่าพิกัด (r, c) ยังอยู่ในขอบเขตของกระดาน ไม่ให้โปรแกรม Crash"""
    return 0 <= r < len(lines) and 0 <= c < len(lines[0])

def check_sliding_attack(king_r, king_c, lines, attackers, directions):
    """
    ฟังก์ชันตรวจสอบการโจมตีระยะไกล (Rook, Bishop, Queen) 
    โดยเริ่มมองจากตำแหน่ง King ออกไปตามทิศทางที่กำหนด 
    """
    for dr, dc in directions:
        r, c = king_r + dr, king_c + dc
        # วนลูปพุ่งไปในทิศทางนั้นเรื่อยๆ จนกว่าจะขอบกระดานหรือมีตัวขวาง 
        while is_valid(r, c, lines):
            piece = lines[r][c]
            # ถ้าเจอหมากศัตรูที่กินในแนวนี้ได้ ให้ถือว่า Check Success
            if piece in attackers:
                return True
            # ถ้าเจอตัวอักษรอื่นที่ไม่ใช่จุด (ว่าง) แสดงว่ามีตัวหมากขวางทางอยู่
            elif piece not in ('.', ' '):
                break
            r, c = r + dr, c + dc
    return False

def check_pawn_attack(king_r, king_c, lines):
    """ ตรวจสอบการโจมตีของเบี้ย (Pawn) ซึ่งจะกินในแนวทแยงระยะ 1 ช่อง """
    # ในที่นี้กำหนดทิศทางกินลงด้านล่าง (row + 1) ตามลักษณะของโจทย์
    for dr, dc in [(1, -1), (1, 1)]:
        r, c = king_r + dr, king_c + dc
        if is_valid(r, c, lines) and lines[r][c] == 'P':
            return True
    return False

def checkmate(board):
    """ ฟังก์ชันหลักที่ใช้ตัดสินว่า King อยู่ในสภาวะโดนรุกหรือไม่ [cite: 48] """
    try:
        # 1. ตรวจสอบว่ามีพระราชาอยู่ในกระดานหรือไม่
        king = king_position(board)
        if not king:
            print("Fail"); return
        
        kr, kc = king
        lines = board.strip().split('\n')
        
        # 2. ตรวจสอบเงื่อนไขกระดานต้องเป็นสี่เหลี่ยมจัตุรัส
        n = len(lines)
        if any(len(line) != n for line in lines):
            print("Fail"); return
        
        # 3. ตรวจสอบกรณีไม่มี Input หรือสายอักขระว่างเปล่า
        if not board or not board.strip():
            print("Fail"); return
        
        # 4. ตรวจสอบการโจมตีจากหมากทุกประเภท
        if (check_pawn_attack(kr, kc, lines) or
            check_sliding_attack(kr, kc, lines, {'R'}, rook_dirs) or
            check_sliding_attack(kr, kc, lines, {'B'}, bishop_dirs) or
            check_sliding_attack(kr, kc, lines, {'Q'}, queen_dirs)):
            print("Success") # พิมพ์ Success เมื่อ King โดนรุก
        else:
            print("Fail") # พิมพ์ Fail เมื่อ King ปลอดภัย
            
    except Exception:
        # หากเกิดข้อผิดพลาดที่ไม่ได้คาดการณ์ ให้คืนการควบคุมแก่ผู้ใช้ (ไม่ Crash) 
        print("Fail")
