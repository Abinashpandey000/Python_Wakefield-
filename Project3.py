########
#import modules
#######

########
#define functions
#######

yourChoices = 0

def start():
    print("Welcome!")
    bed_room()

 

def bed_room():
    print("You are in your bedroom")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tbathroom\n\tkitchen\n\tlivingroom\n\tgym\n")
    if move.lower() == "bathroom":
        bath_room()       
    elif move.lower() == "kitchen":
        kitchen_()
    elif move.lower() == "livingroom":
        living_room()
    elif move.lower()=="gym":
        gym_()  
    else:
        print("You don't have this room in your house.")
        

def bath_room():
    global yourChoices

    yourChoices += 1
    print(yourChoices)

    print()
    print("You are in bathroom")
    print()
    print("You need to take shower and brush your teeth")
    print()
    
    take_bathroom=input("What would you like to do?\n\tshower\n\tbrush\n")
    if take_bathroom=="shower":
        print()
        print("You took a shower")
        print()
        print("now you need to brush your teeth")
        print()
        brush_enter=input("Type b and enter to brush your teeth ")
        if brush_enter=="b":
            print()
            print("You have brushed your teeth")
        else:
            print()
            print("Invalid input")
 
    elif take_bathroom=="brush":
        print()
        print("You brushed your teeth")
        print()
        print("Now you need to take a shower")
        print()
        shower_enter=input("Type s and enter to take a shower ")
        if shower_enter=="s":
            print()
            print("You have taken shower")
        else:
            print()
            print("Invalid input")
    else:
        print("Invalid input")

    move = input("\nWhere would you like to go? Say one of these choices:\n\tkitchen\n\tlivingroom\n\tgym\n\t")
    if move.lower() == "kitchen":
        kitchen_()
    elif move.lower() == "livingroom":
        living_room()
    elif move.lower()=="gym":
        gym_()
    else:
        print("You don't have this room in your house.")
        
        

def kitchen_():
    global yourChoices

    yourChoices += 1
    print(yourChoices)

    print("You are in kitchen")
    print()
    drink_=input("What would you like to drink?\n\twater\n\tcoffee\n")
    if drink_.lower()=="water":
        print("You are hydrated")
    if drink_.lower()=="coffee":
        print("You drank coffee")
        print('''(  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________''')

    move = input("\nWhere would you like to go? Say one of these choices:\n\tchangeroom\n\tgym\n\tlivingroom\n")
    if move.lower() == "changeroom":
        change_room()
    elif move.lower() == "gym":
        gym_()
    elif move.lower()=="livingroom":
        living_room()
    else:
        print("You don't have this room in your home")

def change_room():
    global yourChoices

    yourChoices += 1
    print(yourChoices)
    print('''  _   _
 /)`:'(\
//| : |\\
  |-'-|
  | | |
  |_|_|''')
    print("You're in change room and all set to go to school")
    print()
    press1=input("Enter c to change your clothes ")
    if press1.lower()==" c":
        print("You look super good today. Have a great day at school.")
        print()
    move=input("\nWhere would you like to go? \n\tmaindoor\n\tlivingroom\n")
    
    if move.lower()=="livingroom":
        living_room()
    if move.lower()=="maindoor":
         main_door()
    elif move.lower()=="livingroom":
        living_room()
    else:
        print("You don't have this room at your home")

def living_room():
    global yourChoices
    if yourChoices >= 3:
        print("You have completed all activities")
        main_door()
    else: 
        print("Your dad is there and he asks you to get ready for school")
        print( '''                    #############        
                                    ##         ##       
                                    #  ~~   ~~  #      
                                    #  ()   ()  #       
                                    (     ^     )       
                                    |         |       
                                    |  {===}  |      
                                        \       /       
                                    /  -----  \      
                                    ---  |%\ /%|  ---     
                                /     |%%%%%|     \    
                                        |%/ \%|            
                                                    ''')
        move=input("\nWhere would you like to go? \n\tMaindoor\n\tkitchen\n\tchangeroom\n")
        if move.lower()=="maindoor":
            main_door()
        elif move.lower()=="kitchen":
            kitchen_()
        elif move.lower()=="changeroom":
            change_room()
        else:
            print("You don't have this room in your house")

def gym_():
    global yourChoices
    print("The gym door is locked")
    print(''' __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|''')
    print("You are not strong enough to open the door, please go back to your room!")
    yourChoices = 0
    bed_room()
def main_door():
    global yourChoices
    if yourChoices >= 3:
        print("Have a great day at school")
    else:
        print("You are not ready for school!\n Plese go back to your bedroom")
        yourChoices = 0
        bed_room()



########
#main
#######
#TODO: Add some global variables

start()
 