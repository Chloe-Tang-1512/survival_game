import random
tasks = [1,2,3,4,5]
global ammo
ammo  = 5
global hunger
hunger = 5
global health
health = 5
global power
power = 5
global friendship
friendship = False
global protection
protection = 0
global money
money = 100
global enemy_power
enemy_power = random.randint(1,7)
def food():
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
    elif place == "2":
        print("You went to the supermarket. It was crowded, but you managed to get some food.")
        hunger += 1
        tasks.remove(1)
    elif place == "3":
        print("You went to the secret store. You got a lot of food and water.")
        hunger += 5
        tasks.remove(1)
    elif place == "4":
        print("You tried to steal food, but got caught and arrested. Enjoy prison life.")
        prison()
    else:
        print("You ate all your food now. You might starve during the purge.")
        hunger = 0
def game_over():
    print("Game Over")
    print("Final stats:")
    print("Hunger:", hunger)
    print("Health:", health)
    print("Power:", power)
    print("Friendship:", friendship)
    print("Protection:", protection)
    print("Money:", money)
    exit()
def weapons():
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
        power += 5
        tasks.remove(2)
    elif place == "2":
        print("You went to the ammo store. You bought a lot of ammo, but no weapons.")
        ammo += 10
        tasks.remove(2)
    elif place == "3":
        print("You went to the knife store. You bought a very sharp knife, but knives can only be used in close combat.")
        power += 2
        tasks.remove(2)
    elif place == "4":
        print("You tried to steal weapons and ammo, but got caught and arrested. Enjoy prison.")
        prison()
    else:
        print("You decided to use your fists. Good luck with that.")
        power = 1
        tasks.remove(2)
def prison():
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
        game_over()
    elif place == "2":
        print("You bribed the guard and escaped. You lost all your money.")
        tasks.remove(2)
        money -= money
    elif place == "3":
        print("Your lawyer came and got you out. You lost all your money.")
        tasks.remove(2)
        money -= money
    elif place == "4":
        print("You escaped through the vent. You lost weapons and ammo.")
        ammo -= 1
        power -= 1
        tasks.remove(2)
    else:
        print("You decided to do nothing. Game over.")
        game_over()
def house():
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
        protection += 5
        tasks.remove(3)
    elif place == "2":
        print("You set up traps around the house. Your house is now safer.")
        protection += 4
        tasks.remove(3)
    elif place == "3":
        print("You cleaned the house. It looks nice, but it won't help you during the purge.")
    elif place == "4":
        print("You stocked up on supplies. You are now better prepared for the purge.")
        protection += 2
        tasks.remove(3)
    else:
        print("You decided to do nothing. Your house is not prepared for the purge.")
def plan():
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
        protection += 1
        tasks.remove(4)
    elif place == "2":
        print("You planned your escape route. This will help you during the purge.")
        protection += 2
        tasks.remove(4)
    elif place == "3":
        print("You planned your defense strategy. This will help you during the purge.")
        protection += 3
        tasks.remove(4)
    elif place == "4":
        print("You decided to do nothing. You are not prepared for the purge.")
    else:
        print("You panicked and did nothing useful. You are not prepared for the purge.")
def friends():
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
        friendship = True
        tasks.remove(5)
    elif place == "2":
        print("You texted your friends. They will help you during the purge.")
        friendship = True
        tasks.remove(5)
    elif place == "3":
        print("You invited your friends over. They will help you during the purge.")
        friendship = True
        tasks.remove(5)
    elif place == "4":
        print("You decided to do nothing. You are alone during the purge.")
    else:
        print("You argued with your friends and they won't help you during the purge.")
def intro():
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
    print('''
    Tips:
    - Spend your time wisely
    - Always be cautious: better safe than sorry
    - Don't trust any strangers
    - Your house is the safest
    - Do not go outside when purge starts, unless it's an emergency
    ''')
    print("Remember those tips, and good luck!")
    print("")
    print('''
    1. Stock up on food and water
    2. Stock up on weapons and ammo
    3. Prepare your house
    4. Contact your friends
    5. Make plans
    ''')
    choice = input("What would you like to do first?(1,2,3,4,5)")
    if choice == "1":
        food()
    elif choice == "2":
        weapons()
    elif choice == "3":
        house()
    elif choice == "4":
        plan()
    elif choice == "5":
        friends()
    else:
        print("Invalid choice. Your time is wasted.")
        game_over()
def voices():
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
        game_over()
    elif place == "2":
        print("You looked through the window. You saw some people trying to break in.")
        protection -= 1
        window()
    elif place == "3":
        print("You went outside to check. You got attacked and killed. Game over.")
        game_over()
    elif place == "4":
        print("You called the police. They are on their way, but it might be too late.")
        protection += 1
    else:
        print("You hid. The voices went away, but they might come back.")
def window():
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
        protection += 1
    elif place == "2":
        print("You tried to scare them away. They are not afraid.")
        protection -= 1
    elif place == "3":
        print("You prepared to defend yourself. You feel more secure.")
        protection += 2
    elif place == "4":
        print("You requested help from friends.")
        if friendship == True:
            print("Your friends are coming to help you.")
            protection += 2
        else: 
            print("But you have no friends to help you.")
            protection -= 1
    else:
        print("You panicked and did nothing useful.")
        game_over()
def intruders():
    print("Some intruders are trying to break into your house. You need to act fast.")
    print('''
    1. Use your weapons to defend yourself
    2. Use your traps to defend yourself
    3. Hide and wait for them to leave
    4. Call the police
    5. Surrender
    ''')
    place = input("What do you want to do now? > ")
    if place == "1":
        if ammo > 0 and power > enemy_power:
            print("You used your weapons to defend yourself. You killed the intruders.")
            ammo -= 1
        else:
            print("You have no ammo or weapons. You got killed by the intruders. Game over.")
            game_over()
    elif place == "2":
        if protection > 0:
            print("You used your traps to defend yourself. You killed the intruders.")
            protection -= 1
        else:
            print("You have no traps. You got killed by the intruders. Game over.")
            game_over()
    elif place == "3":
        print("You hid and waited for them to leave. They eventually left, but you are not safe.")
        protection -= 1
    elif place == "4":
        print("You called the police. They are on their way, but it might be too late.")
        protection += 1
    else:
        print("You surrendered. The intruders took all your supplies and left you alive, but barely.")
        ammo = 0
        power = 0
        protection = 0
def friend_request():
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
        if money >= 20:
            print("You sent them supplies. They are grateful.")
            money -= 20
            print("They sent you a gift in return.")
            power += 1
        else:
            print("You don't have enough money to send them supplies.")
    elif choice == "2":
        print("You gave them advice. They are grateful.")
        power += 1
    elif choice == "3":
        if power > enemy_power:
            print("You went to help them. You successfully helped them and returned safely.")
            protection -= 2
        else:
            print("You don't have enough power to go help them. You got killed on the way. Game over.")
            game_over()
    elif choice == "4":
        print("You ignored them. They are disappointed.")
        friendship = False
    else:
        if protection > 3:
            print("You told them to come to your house. They are grateful and came safely.")
            protection += 1
        else:
            print("You don't have enough protection to let them come to your house. They got killed on the way. Game over.")
            game_over()
def weak():
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
        if ammo > 0 and power > 7:
            print("You used your weapons to defend yourself. You killed the intruders.")
            ammo -= 1
        else:
            print("You have no ammo or are not powerful enough. You got killed by the intruders. Game over.")
            game_over()
    elif place == "2":
        if protection > 3:
            print("You used your traps to defend yourself. You killed the intruders.")
            protection -= 1
        else:
            print("You have no traps. You got killed by the intruders. Game over.")
            game_over()
    elif place == "3":
        print("You hid and waited for them to leave. They eventually left, but took all your supplies.")
        ammo = 0
        power = 1
        protection = 1
    elif place == "4":
        print("You called the police. They are on their way, but it is too late.")
        game_over()
    else:
        print("You surrendered. The intruders had no mercy. They took all your supplies and killed you.")
        game_over()
def war():
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
        if power > 7 and ammo > 3:
            print("You fought bravely and survived the war.")
            win()
        else:
            print("You are not powerful enough or have no ammo. You got killed in the war. Game over.")
            game_over()
    elif place == "2":
        print("You hid and waited for the war to end. YOU CANNOT HIDE FROM WAR!")
        game_over()
    elif place == "3" and protection > 2:
        print("You tried to escape the war zone. You got injured, but managed to escape.")
        win()
    elif place == "4":
        if friendship == True:
            print("You fought with your friends. Together, you were able to survive the war.")
            win()
        else:
            print("You tried to fight with friends, but they abandoned you. You got killed.")
            game_over()
    else:
        print("You surrendered. The enemy showed no mercy. You got killed.")
        game_over()
def main():
    intro()
    while len(tasks) > 0:
        print("You have", len(tasks), "tasks left.")
        print("You can:")
        if 1 in tasks:
            print("1. Stock up on food and water")
        if 2 in tasks:
            print("2. Stock up on weapons and ammo")
        if 3 in tasks:
            print("3. Prepare your house")
        if 4 in tasks:
            print("4. Make plans")
        if 5 in tasks:
            print("5. Contact your friends")
        choice = input("What would you like to do now?(1,2,3,4,5) ")
        if choice == "1" and 1 in tasks:
            food()
        elif choice == "2" and 2 in tasks:
            weapons()
        elif choice == "3" and 3 in tasks:
            house()
        elif choice == "4" and 4 in tasks:
            plan()
        elif choice == "5" and 5 in tasks:
            friends()
        else:
            print("Invalid choice or task already completed. Your time is wasted.")
    print("You have completed all your tasks. The purge is starting now.")
    print("You hear voices outside your house.")
    voices()
    intruders()
    friend_request()
    weak()
    war()
    print("Congratulations! You survived the purge.")
def win():
    print("You survived the purge. You are a true survivor.")
    print("Final stats:")
    print("Hunger:", hunger)
    print("Health:", health)
    print("Power:", power)
    print("Friendship:", friendship)
    print("Protection:", protection)
    print("Money:", money)
main()
