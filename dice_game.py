import random

def dice_game():
    player_1 = 0
    player_1_wins = 0
    player_2 = 0
    player_2_wins = 0
    draws = 0
    round = 1

    while round <= 10:
        print("Round: " + str(round))
        player_1 = roll()
        player_2 = roll()
        print("Player 1: " + str(player_1))
        print("Player 2: " + str(player_2))
        
        if player_1 > player_2:
            print("Player 1 wins\n")
            player_1_wins += 1
            round += 1
        elif player_2 > player_1:
            print("Player 2 wins\n")
            player_2_wins += 1
            round += 1
        else:
            print("Draw\n")
            draws += 1
            round += 1

    if player_1_wins > player_2_wins:
        print("Player 1 is Victorious - Record: " + str(player_1_wins) + " - " + str(player_2_wins) + " - " + str(draws))
    elif player_2_wins > player_1_wins:
        print("Player 2 is Victorious - Record: " + str(player_2_wins) + " - " + str(player_1_wins) + " - " + str(draws))
    else:
        print("Tie")

def roll():
    dice_roll = random.randint(1, 6)
    return dice_roll

dice_game()