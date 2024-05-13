from Controller import Controller


def main():
    print("\t\tWelcome to Othello game")
    difficulty = int(input("Choose difficulty of the computer 1- Easy, 2- Medium, 3-Hard: "))
    controller = Controller(difficulty)
    controller.print_scores()
    turn = "B"
    blocked = 0
    while not controller.game_finished():
        if blocked >= 2:
            print("You both don't have any valid moves!!!")
            controller.declare_winner()
            break
        controller.print_board()
        print("\n")
        if turn == "B":
            moves = controller.get_valid_moves(turn)
            if len(moves) == 0:
                print("You have no valid moves")
                turn = "W"
                blocked += 1
                continue
            if blocked > 0:
                blocked -= 1
            print("Here are your valid moves")
            print(moves)
            index = int(input("Enter your move index: "))
            while not controller.make_move(moves[index][0], moves[index][1], turn):
                index = int(input("Enter a valid index"))
            turn = "W"
        else:
            if not controller.computer_move():
                print("computer has no valid moves")
                blocked += 1
                turn = "B"
                continue
            if blocked > 0:
                blocked -= 1

            turn = "B"


if __name__ == "__main__":
    main()
