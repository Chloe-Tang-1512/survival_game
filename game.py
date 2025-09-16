import random

class GameState:
    def __init__(self):
        self.tasks = [1, 2, 3, 4, 5]
        self.ammo = 5
        self.hunger = 5
        self.health = 5
        self.power = 5
        self.friendship = False
        self.protection = 0
        self.money = 100
        self.enemy_power = random.randint(1, 7)

def check_health(state):
    if state.health <= 0:
        print("You have died of your injuries. Game over.")
        game_over(state)

def check_hunger(state):
    if state.hunger <= 0:
        print("You have starved to death. Game over.")
        game_over(state)
    else:
        state.hunger -= 1

def food(state):
    print("You can:")
    print('''
    1. Not get any extra food
    2. Go to the supermarket
    3. Go to the secret store shared by your friends
    4. Steal
    5. Eat all your food now
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        print("You didn't get any extra food. You might starve during the purge.")
        state.tasks.remove(1)
    elif place == "2":
        print("You went to the supermarket. It was crowded, but you managed to get some food.")
        state.hunger += 1
        state.tasks.remove(1)
    elif place == "3":
        print("You went to the secret store. You got a lot of food and water.")
        state.hunger += 5
        state.tasks.remove(1)
    elif place == "4":
        print("You tried to steal food, but got caught and arrested. Enjoy prison life.")
        prison(state)
        state.tasks.remove(1)
    else:
        print("You ate all your food now. You might starve during the purge.")
        state.hunger = 1
        state.tasks.remove(1)

def game_over(state):
    print("Game Over")
    print("Final stats:")
    print("Hunger:", state.hunger)
    print("Health:", state.health)
    print("Power:", state.power)
    print("Friendship:", state.friendship)
    print("Protection:", state.protection)
    print("Money:", state.money)
    exit()

def weapons(state):
    print("You can:")
    print('''
    1. Go to the guns store
    2. Go to the ammo store
    3. Go to knife store
    4. Steal lots of weapons and ammo
    5. Use your fists
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        print("You went to the gun store. There, you bought a very powerful gun, however, ammo is limited.")
        state.power += 5
        state.tasks.remove(2)
    elif place == "2":
        print("You went to the ammo store. You bought a lot of ammo, but no weapons.")
        state.ammo += 10
        state.tasks.remove(2)
    elif place == "3":
        print("You went to the knife store. You bought a very sharp knife, but knives can only be used in close combat.")
        state.power += 2
        state.tasks.remove(2)
    elif place == "4":
        print("You tried to steal weapons and ammo, but got caught and arrested. Enjoy prison.")
        prison(state)
        state.tasks.remove(2)
    else:
        print("You decided to use your fists. Good luck with that.")
        state.power = 1
        state.tasks.remove(2)

def prison(state):
    print("You are in prison. You lost all your weapons and ammo. If you want a chance, escape.")
    print('''
    1. Try to break the lock(risk)
    2. Bribe the guard(lose all your money)
    3. Wait for your lawyer(lose all your money)
    4. Escape through the vent(lose weapons and ammo)
    5. Do nothing
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        print("You tried to break the lock, but failed and got punished. Game over.")
        game_over(state)
    elif place == "2":
        print("You bribed the guard and escaped. You lost all your money.")
        state.health -= 1
        state.tasks.remove(2)
        state.money -= state.money
        check_health(state)
    elif place == "3":
        print("Your lawyer came and got you out. You lost all your money.")
        state.health -= 1
        state.tasks.remove(2)
        state.money -= state.money
        check_health(state)
    elif place == "4":
        print("You escaped through the vent. You lost weapons and ammo.")
        state.health -= 1
        state.ammo -= 1
        state.power -= 1
        state.tasks.remove(2)
        check_health(state)
    else:
        print("You decided to do nothing. Game over.")
        game_over(state)

def house(state):
    print("You can:")
    print('''
    1. Board up the windows and doors
    2. Set up traps around the house
    3. Clean the house
    4. Stock up on supplies
    5. Do nothing
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        print("You boarded up the windows and doors. Your house is now safer.")
        state.protection += 5
        state.tasks.remove(3)
    elif place == "2":
        print("You set up traps around the house. Your house is now safer.")
        state.protection += 4
        state.tasks.remove(3)
    elif place == "3":
        print("You cleaned the house. It looks nice, but it won't help you during the purge.")
        state.tasks.remove(3)
    elif place == "4":
        print("You stocked up on supplies. You are now better prepared for the purge.")
        state.protection += 2
        state.tasks.remove(3)
    else:
        print("You decided to do nothing. Your house is not prepared for the purge.")
        state.tasks.remove(3)

def plan(state):
    print("You can:")
    print('''
    1. Make a list of emergency contacts
    2. Plan your escape route
    3. Plan your defense strategy
    4. Do nothing
    5. Panic
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        print("You made a list of emergency contacts. This will help you during the purge.")
        state.protection += 1
        state.tasks.remove(4)
    elif place == "2":
        print("You planned your escape route. This will help you during the purge.")
        state.protection += 2
        state.tasks.remove(4)
    elif place == "3":
        print("You planned your defense strategy. This will help you during the purge.")
        state.protection += 3
        state.tasks.remove(4)
    elif place == "4":
        print("You decided to do nothing. You are not prepared for the purge.")
        state.tasks.remove(4)
    else:
        print("You panicked and did nothing useful. You are not prepared for the purge.")
        state.tasks.remove(4)

def friends(state):
    print("You can:")
    print('''
    1. Call your friends
    2. Text your friends
    3. Invite your friends over
    4. Do nothing
    5. Argue with your friends
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        print("You called your friends. They will help you during the purge.")
        state.friendship = True
        state.tasks.remove(5)
    elif place == "2":
        print("You texted your friends. They will help you during the purge.")
        state.friendship = True
        state.tasks.remove(5)
    elif place == "3":
        print("You invited your friends over. They will help you during the purge.")
        state.friendship = True
        state.tasks.remove(5)
    elif place == "4":
        print("You decided to do nothing. You are alone during the purge.")
        state.tasks.remove(5)
    else:
        print("You argued with your friends and they won't help you during the purge.")
        state.tasks.remove(5)

def intro(state):
    name = input("What is your name? > ")
    print("HELLO_WORLD")
    print("Hello", name)
    print("It is 12 hours before the first day of purge. You need to prepare yourself. ")
    print("There are some things your can do now:")
    print('''
    1. Stock up on food and water
    2. Stock up on weapons and ammo
    3. Prepare your house
    4. Make plans
    5. Contact your friends
    ''')
    print("Good luck!")
    choice = input("What would you like to do first?(1,2,3,4,5) > ")
    if choice == "1":
        food(state)
    elif choice == "2":
        weapons(state)
    elif choice == "3":
        house(state)
    elif choice == "4":
        plan(state)
    elif choice == "5":
        friends(state)
    else:
        print("Invalid choice. Your time is wasted.")
        game_over(state)

def voices(state):
    print("You hear voices outside your house. It might be dangerous to ignore them.")
    print('''
    1. Ignore the voices
    2. Look through the window
    3. Go outside to check
    4. Call the police
    5. Hide
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        print("You ignored the voices. They got in your house and killed you.")
        game_over(state)
    elif place == "2":
        print("You looked through the window. You saw some people trying to break in.")
        state.health -= 1
        check_health(state)
        window(state)
    elif place == "3":
        print("You went outside to check. You got attacked and killed. Game over.")
        game_over(state)
    elif place == "4":
        print("You called the police. They are on their way, but it might be too late.")
        state.health -= 1
        check_health(state)
        state.protection += 1
    else:
        print("You hid. The voices went away, but they might come back.")

def window(state):
    print("You can:")
    print('''
    1. Request police backup
    2. Try to scare them away
    3. Prepare to defend yourself
    4. Request help from friends
    5. Panic
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        print("You called the police. They are on their way, but it might be too late.")
        state.health -= 1
        check_health(state)
        state.protection += 1
    elif place == "2":
        print("You tried to scare them away. They are not afraid.")
        state.health -= 1
        check_health(state)
    elif place == "3":
        print("You prepared to defend yourself. You feel more secure.")
        state.health += 1
        check_hunger(state)
    elif place == "4":
        print("You requested help from friends.")
        if state.friendship == True:
            print("Your friends are coming to help you.")
            state.protection += 2
        else: 
            print("But you have no friends to help you.")
            state.health -= 1
            check_health(state)
    else:
        print("You panicked and did nothing useful.")
        game_over(state)

def bomb(state):
    print("Someone set a bomb outside your house. You need to act fast.")
    print('''
    1. Try to defuse the bomb
    2. Run away from the house
    3. Take cover in the basement
    4. Hide in the house
    5. Panic
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        if state.protection >= 5:
            print("You successfully defused the bomb. You are safe.")
            state.hunger -= 1
            check_hunger(state)
        else:
            print("You are not powerful enough to defuse the bomb. It exploded and killed you. Game over.")
            game_over(state)
    elif place == "2":
        print("You ran away from the house. You got injured, but managed to escape.")
        state.health -= 1
        check_health(state)
        state.hunger -= 1
        check_hunger(state)
    elif place == "3":
        print("You took cover in the basement. You are safe for now.")
        state.hunger -= 1
        check_hunger(state)
    elif place == "4":
        print("You hid in the house. You only took some damage.")
        state.health -= 1
        check_hunger(state)
    else:
        print("You panicked and did nothing useful.")
        game_over(state)

def friend_request(state):
    print("Your friend is requesting help from you. You need to decide how to help them.")
    print('''
    1. Send them supplies
    2. Give them advice
    3. Go to help them
    4. Ignore them
    5. Tell them to come to your house
    ''')
    choice = input("What do you want to do? > ")
    if choice == "1":
        if state.money >= 20:
            print("You sent them supplies. They are grateful.")
            state.money -= 20
            print("They sent you a gift in return.")
            state.power += 1
        else:
            print("You don't have enough money to send them supplies.")
            state.friendship = False
    elif choice == "2":
        print("You gave them advice. They are grateful.")
        state.power += 1
    elif choice == "3":
        if state.power > state.enemy_power:
            print("You went to help them. You successfully helped them and returned safely.")
            state.health -= 5
            check_health(state)
            state.protection += 1
        else:
            print("You don't have enough power to go help them. You got killed on the way. Game over.")
            game_over(state)
    elif choice == "4":
        print("You ignored them. They are disappointed.")
        state.friendship = False
    else:
        if state.protection > 3:
            print("You told them to come to your house. They are grateful and came safely.")
            state.protection += 1
        else:
            print("You don't have enough protection to let them come to your house. They got killed on the way.")
            state.friendship = False

def weak(state):
    print("Very powerful people are in your house. You need to act fast.")
    print('''
    1. Use your weapons to defend yourself
    2. Use your traps to defend yourself
    3. Hide and wait for them to leave
    4. Call the police
    5. Surrender
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        if state.ammo > 0 and state.power > 7:
            print("You used your weapons to defend yourself. You killed the intruders.")
            state.health -= 1
            check_health(state)
            state.ammo -= 1
            state.hunger -= 1
            check_hunger(state)
        else:
            print("You have no ammo or are not powerful enough. You got killed by the intruders. Game over.")
            game_over(state)
    elif place == "2":
        if state.protection > 3:
            print("You used your traps to defend yourself. You killed the intruders.")
            state.health -= 1
            check_health(state)
            state.protection -= 1
        else:
            print("You have no traps. You got killed by the intruders. Game over.")
            game_over(state)
    elif place == "3":
        print("You hid and waited for them to leave. They eventually left, but took all your supplies.")
        state.ammo = 0
        state.power = 1
        state.protection = 1
    elif place == "4":
        print("You called the police. They are on their way, but it is too late.")
        game_over(state)
    else:
        print("You surrendered. The intruders had no mercy. They took all your supplies and killed you.")
        game_over(state)

def war(state):
    print("A full scale war is happening outside. You need to act fast.")
    print('''
    1. Fight
    2. Hide
    3. Escape
    4. Fight with friends
    5. Surrender
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        if state.power > 7 and state.ammo > 3:
            print("You fought bravely and survived the war.")
            state.health -= 1
            check_health(state)
            state.hunger -= 1
            check_hunger(state)
            win(state)
        else:
            print("You are not powerful enough or have no ammo. You got killed in the war. Game over.")
            game_over(state)
    elif place == "2":
        print("You hid and waited for the war to end. YOU CANNOT HIDE FROM WAR!")
        game_over(state)
    elif place == "3" and state.protection > 2:
        print("You tried to escape the war zone. You got injured, but managed to escape.")
        state.health -= 1
        check_health(state)
        state.hunger -= 1
        check_hunger(state)
        win(state)
    elif place == "4":
        if state.friendship == True:
            print("You fought with your friends. Together, you were able to survive the war.")
            state.health -= 1
            state.hunger -= 1
            check_health(state)
            check_hunger(state)
            win(state)
        else:
            print("You tried to fight with friends, but they abandoned you. You got killed.")
            game_over(state)
    else:
        print("You surrendered. The enemy showed no mercy. You got killed.")
        game_over(state)

def main():
    state = GameState()
    intro(state)
    while len(state.tasks) > 0:
        print("You have", len(state.tasks), "tasks left.")
        print("You can:")
        if 1 in state.tasks:
            print("1. Stock up on food and water")
        if 2 in state.tasks:
            print("2. Stock up on weapons and ammo")
        if 3 in state.tasks:
            print("3. Prepare your house")
        if 4 in state.tasks:
            print("4. Make plans")
        if 5 in state.tasks:
            print("5. Contact your friends")
        choice = input("What would you like to do now?(1,2,3,4,5) ")
        if choice == "1" and 1 in state.tasks:
            food(state)
        elif choice == "2" and 2 in state.tasks:
            weapons(state)
        elif choice == "3" and 3 in state.tasks:
            house(state)
        elif choice == "4" and 4 in state.tasks:
            plan(state)
        elif choice == "5" and 5 in state.tasks:
            friends(state)
        else:
            print("Invalid choice or task already completed. Your time is wasted.")
    print("You have completed all your tasks. The purge is starting now.")
    print("You hear voices outside your house.")
    voices(state)
    bomb(state)
    friend_request(state)
    weak(state)
    war(state)
    print("Congratulations! You survived the purge.")

def win(state):
    print("You survived the purge. You are a true survivor.")
    print("Final stats:")
    print("Hunger:", state.hunger)
    print("Health:", state.health)
    print("Power:", state.power)
    print("Friendship:", state.friendship)
    print("Protection:", state.protection)
    print("Money:", state.money)

main()
