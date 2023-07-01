"""
Welcome to a Text Based Adventure Game
where a player will have to choose between two doors
The doors lead to another room, each room has its own story
"""


# diamond room
def diamond_room():
    """
    This function will take the player to the diamond room
    And will ask the player to choose between two options
    """
    # take some prompts
    print(
        """
  You are now in a room filled with diamonds!
  And there is a door too!
  What would you do? (1 or 2)
  1). Take some diamonds and go through the door.
  2). Just go through the door."""
    )

    # take input()
    answer = input(">")

    if answer == "1":
        # the player is dead, call game_over() function with the "reason"
        game_over(
            "They were cursed diamonds!\nThe moment you touched it,\nThe building collapsed, and you die!"
        )
    elif answer == "2":
        # the player won the game
        print("Good one!\nyou win the game!")
        # activate play_again() function
        play_again()
    else:
        # call game_over() with "reason"
        game_over("you lost.")


# bear room
def bear_room():
    """
    This function will take the player to the bear room
    And will ask the player to choose between taunting the bear or taking the honey
    """
    print(
        """
  There is a bear here
  Behind the bear is another door.
  The bear is eating tasty honey!
  What would you do? (1 or 2)
  1). Take the honey.
  2). Taunt the bear."""
    )

    # take input()
    answer = input(">")

    if answer == "1":
        # the player is dead!
        game_over("The bear killed you.")
    elif answer == "2":
        # lead him to the diamond_room()
        print(
            "Your Good time,\nthe bear moved from the door.\nYou can go through it now!"
        )
        diamond_room()
    else:
        # else call game_over() function with the "reason" argument
        game_over(
            "You lost,\nInvalid Input,\nrestart the game and choose correct option:- (1 or 2)."
        )


# monster room
def monster_room():
    """
    This function will take the player to the monster room
    And will ask the player to choose between two options
    """
    print(
        """
  Now you entered the room of a monster!
  The monster is sleeping.
  Behind the monster,there is another door. What would you do? (1 or 2)
  1). Go through the door silently.
  2). Kill the monster and show your courage!"""
    )

    # take input()
    answer = input(">")

    if answer == "1":
        # leads to the diamond_room()
        diamond_room()
    elif answer == "2":
        # the player is dead, call game_over() with "reason"
        game_over("The monster was hungry,its ate you.")
    else:
        # game_over() with "reason"
        game_over(
            "You lost,\nInvalid Input,\nrestart the game and choose correct option."
        )


# function to ask play again or not
def play_again():
    """
    This function will ask the player to play again or not
    """
    print("Do you want to play again?\n(yes or no)")

    # converts the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        start()
    else:
        # if player types anything besides "yes" or "y", exit() the program
        exit("Goodbye!!!")


# game_over function accepts an argument called "reason"
def game_over(reason):
    """
    This function ends the game with reasons
    """
    print(reason)
    print("Game Over!")
    # ask player to play again or not by play_again() function
    play_again()


def start():
    """
    This Function starts the game
    and asks the player to choose between the left or right door
    """
    print(
        """
  Welcome to The Text based adventure game,
  You are standing in a dark room.
  There is a door to your left and right, which one do you take? (left or right)"""
    )

    # converts the player's input() to lower_case
    answer = input(">").lower()

    if "l" in answer:
        # if player typed "left" or "l" leads him to bear_room()
        bear_room()
    elif "r" in answer:
        # elif player typed "right" or "r" leads him to monster_room()
        monster_room()
    else:
        # else game_over() function with the "reason" as argument
        game_over(
            "You lost,\nrestart the game and choose either the left or right door "
        )


# start the game
start()
