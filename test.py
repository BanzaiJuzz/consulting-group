# tic_tac_toe.py
# Простые крестики-нолики в консоли с игрой против компьютера (AI ходит случайно/по простым правилам)

import random

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def check_win(board, player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

def check_draw(board):
    return all(cell != " " for cell in board)

def player_move(board):
    while True:
        move = input("Твой ход (введи позицию 1-9): ").strip()
        if not (move.isdigit() and 1 <= int(move) <= 9):
            print("Нужно число от 1 до 9.")
            continue
        idx = int(move) - 1
        if board[idx] != " ":
            print("Эта клетка занята. Выбери другую.")
            continue
        board[idx] = "X"
        break

def find_winning_move(board, player):
    # вернуть индекс выигрышного хода для player, если есть
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_win(board, player):
                board[i] = " "
                return i
            board[i] = " "
    return None

def ai_move(board):
    # 1) если AI может выиграть — сделать ход
    win = find_winning_move(board, "O")
    if win is not None:
        board[win] = "O"
        return

    # 2) если игрок может выиграть на следующем ходу — блокировать
    block = find_winning_move(board, "X")
    if block is not None:
        board[block] = "O"
        return

    # 3) занять центр если свободен
    if board[4] == " ":
        board[4] = "O"
        return

    # 4) занять случайный угол
    corners = [i for i in [0,2,6,8] if board[i] == " "]
    if corners:
        board[random.choice(corners)] = "O"
        return

    # 5) занять любую свободную клетку
    empties = [i for i in range(9) if board[i] == " "]
    if empties:
        board[random.choice(empties)] = "O"

def main():
    print("Крестики-нолики. Ты — X, компьютер — O.")
    board = [" "] * 9
    current = "player"  # player или ai

    while True:
        print_board(board)

        if current == "player":
            player_move(board)
            if check_win(board, "X"):
                print_board(board)
                print("Поздравляю! Ты выиграл! 🎉")
                break
            current = "ai"
        else:
            print("Ход компьютера...")
            ai_move(board)
            if check_win(board, "O"):
                print_board(board)
                print("Компьютер выиграл. Попробуй ещё раз.")
                break
            current = "player"

        if check_draw(board):
            print_board(board)
            print("Ничья.")
            break

    # спросить сыграть ещё раз
    again = input("Сыграть ещё раз? (y/n): ").strip().lower()
    if again == "y":
        main()
    else:
        print("Спасибо за игру!")

if __name__ == "__main__":
    main()