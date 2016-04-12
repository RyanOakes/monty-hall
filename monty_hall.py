import os
import random



                              #FUNCTIONS
#------------------------------------------------------------------------------#


victory = "\nVictory!"
defeat = "\nHindsight is 20/20! Enjoy the goat!"


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def choose_prize_door():

    return random.randint(1, 3)


def contestant_chooses_initial_door():

    return random.randint(1,3)


def choose_goat_door(prize_door, first_door_selection, doors):

    expendable_doors = []

    for door in doors:
        if door != prize_door and door != first_door_selection:
            expendable_doors.append(door)


    expendable_doors = random.choice(expendable_doors)

    return expendable_doors


def eliminiate_a_door(expendable_door, doors):

    if expendable_door in doors:
        doors.remove(expendable_door)
    return doors



def final_door_selection(first_door_selection, prize_door):

    return first_door_selection == prize_door


def keeping_score_of_wins_and_losses(verdict, wins, losses):


    if verdict:
         wins += 1

    else:
        losses += 1

    return wins, losses



def main():

    wins = 0
    losses = 0


    for _ in range(1000):

        print("\nWelcome contestant, let's transcend time and space and simulate 1000 games!\n")
        doors = [1, 2, 3]

        clear()

        #Prize door is chosen
        prize_door = choose_prize_door()


        #Contestant chooses initial door selection
        first_door_selection = contestant_chooses_initial_door()


        #Establish eligible doors to eliminate
        expendable_doors = choose_goat_door(prize_door, first_door_selection, doors)


        #Host asks to choose from final two doors
        doors = eliminiate_a_door(expendable_doors, doors)



        verdict = final_door_selection(first_door_selection, prize_door)


        wins, losses = keeping_score_of_wins_and_losses(verdict, wins, losses)


        print("Current wins: ", wins)

        print("Current losses: ", losses)

        print("Win Percentage: ", (wins / 1000) * 100, "%")

        print("Loss Percentage: ", (losses/ 1000) * 100, "%")

    print("\nOut of 1000 total games, not switching doors resulted in {} wins and {} losses!\n".format(wins, losses))

                              #MAIN
#------------------------------------------------------------------------------#



if __name__ == '__main__':
    main()
