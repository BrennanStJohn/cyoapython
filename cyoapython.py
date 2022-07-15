from tkinter import N, Y


print("""████████╗██████╗ ███████╗ █████╗ ███████╗██╗   ██╗██████╗ ███████╗    ██╗███████╗██╗      █████╗ ███╗   ██╗██████╗ 
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝    ██║██╔════╝██║     ██╔══██╗████╗  ██║██╔══██╗
   ██║   ██████╔╝█████╗  ███████║███████╗██║   ██║██████╔╝█████╗      ██║███████╗██║     ███████║██╔██╗ ██║██║  ██║
   ██║   ██╔══██╗██╔══╝  ██╔══██║╚════██║██║   ██║██╔══██╗██╔══╝      ██║╚════██║██║     ██╔══██║██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗██║  ██║███████║╚██████╔╝██║  ██║███████╗    ██║███████║███████╗██║  ██║██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝\n""")



print("\nWelcome to Treasure Island.\n")

gameon = input("Would you like to play?\n\nType 'y' or 'n': ")

while(gameon == "y"):
  print("Your mission is to find the treasure.\n")

  firstInput = input("You're at a cross road.\n\nWhere do you want to go?\n\nType 'left' or 'right'.\n\n")

  if(firstInput == "left"):
    lakeInput = input("\nYou come to a lake.\n\nThere is an island in the middle of the lake.\n\nType 'wait' to wait for a boat.\nType 'swim' to swim across.\n\n")
    if(lakeInput == "wait"):
      doorInput = input("\nYou arrive at the island unharmed.\n\nThere is a house with 3 doors.\n\nOne red, one yellow and one blue.\n\nWhich color do you choose?\n\n")
      if(doorInput == "blue"):
        print("\nYou enter the blue door.\nThe room is dark and cold.\nThe door closes behind you and you hear something running towards you.\n\nYou die.\n\n")
        gameover = print(""" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝\n""")
      elif(doorInput == "red"):
        print("\nYou enter the room and the door closes behind you.\nYou're suddenly blinded by a bright flash of light.\n\nWhen you come to your senses, you see a mountain of treasure in front of you.\n\n")
        print(r"""                            _.--.
                          _.-'_:-'||
                      _.-'_.-::::'||
                _.-:'_.-::::::'  ||
              .'`-.-:::::::'     ||
              /.'`;|:::::::'      ||_
            ||   ||::::::'     _.;._'-._
            ||   ||:::::'  _.-!oo @.!-._'-.
            \'.  ||:::::.-!()oo @!()@.-'_.|
              '.'-;|:.-'.&$@.& ()$%-'o.'\U||
                `>'-.!@%()@'@_%-'_.-o _.|'||
                ||-._'-.@.-'_.-' _.-o  |'||
                ||=[ '-._.-\U/.-'    o |'||
                || '-.]=|| |'|      o  |'||
                ||      || |'|        _| ';
                ||      || |'|    _.-'_.-'
                |'-._   || |'|_.-'_.-'
                  '-._'-.|| |' `_.-'
                      '-.||_/.-'""")
      elif(doorInput == "yellow"):
        print("\nAs you reach for the door, you feel a sharp pain in your side.\n\nYou die.\n\n")
        gameover = print(""" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝\n""")
    elif(lakeInput == "swim"):
      print("You feel something brush your feet as you swim. The water is too dark to see what it could be.\nYou're suddenly dragged to the bottom of the lake and cannot breathe.\n\nYou die.\n\n")
      gameover = print(""" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝\n""")

  elif(firstInput == "right"):
    print("\nYou come to a dark forest.\n\nEnter the forest or go back?\n\nType 'enter' or 'go back'.\n\n")
    print("\nBefore you can even make a decision, something rushes out of the forest and mauls you to death.\n\nYou die.\n\n")
    gameover = print(""" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝\n""")
  gameon = input("Would you like to try again?\n\nType 'y' or 'n': ")
if(gameon == 'n'):
  print("\nExiting...")