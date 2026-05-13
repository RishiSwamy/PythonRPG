#Rishi Swamy Python RPG 5/10/26
#Version 1.0 5/10/26
import random
import time
#enemy 1 Trojan
def Trojan(health,damage):
    print("You walk into the room. A powerful trojan stands in front of you.")
    trojanhealth=random.randint(1,3)
    time.sleep(2)
    while True:
        trojandamage=random.randint(1,2)
        print("1. Attack 2. Defend and observe")
        choice = input("Enter choice: ")

        if choice == "1":
            print("Attacking Trojan!")
            trojanhealth=trojanhealth-damage
            time.sleep(2)
            print("Trojan Attacked")
            health=health-trojandamage
            time.sleep(2)
            print("Health is now " + str(health))
            print("Trojan health is now " + str(trojanhealth))

        elif choice == "2":
            print("You deflect the trojan attack!. He grazes you.")
            health=health-max(0, trojandamage-1)
            time.sleep(2)
            print("Health is now " + str(health))
            print("Trojan health is" + str(trojanhealth))
            print("Trojan damage is" + str(trojandamage))
        
        if trojanhealth <= 0:
            print("Trojan defeated!")
            return health,damage
        elif health<=0:
            print("You died game over!")
            return health,damage
        else:
            continue


#Enemy 2 VIRUS
def Virus(health,damage):
    print("You walk into the room. A powerful virus stands in front of you.")
    virushealth=random.randint(1,10)
    time.sleep(2)
    special= False
    while True:
        virusdam=random.randint(1,10)
        print("1. Attack 2. Defend and observe")
        choice = input("Enter choice: ")

        if choice == "1":
            print("Attacking Virus!")
            virushealth=virushealth-damage
            time.sleep(2)
            print("Virus Roars and brutally attacks you")
            health=health-virusdam
            time.sleep(2)
            print("Health is now " + str(health))
            print("Virus health is now " + str(virushealth))

        elif choice == "2":
            special=True
            print("You deflect the virus attack!. He grazes you.")
            health=health-max(0, virusdam-1)
            print("Your keen eye analyzes a weakness. Antinvirus enabled.")
            print("Hopefully this works. Attack now!")
            time.sleep(2)
            print("Health is now " + str(health))
            print("Virus health is" + str(virushealth))
            print("Virus damage is" + str(virusdam))
        
        if virushealth <= 0:
            if special:
                resurrection=random.randint(1,5)
                if resurrection <=4:
                    print("Virus defeated!")
                    return health,damage
                else:
                    print("That antivirus struggled but at least stopped mutation")
                    virushealth=random.randint(1,10)
                    time.sleep(2)
            else:
                resurrection=random.randint(1,2)
                if resurrection <=1:
                    print("Virus defeated! You were lucky this time")
                    return health,damage
                else:
                    print("The virus grows and mutates. Brute force is not enough")
                    print("Perhaps there is a weakness I can observe")
                    virushealth=random.randint(10,20)
                    time.sleep(2)
        elif health<=0:
            print("You died game over!")
            return health,damage
        else:
            continue





character=input("Hello weary traveler, what is your name? ")
print("Welcome " + character + " to the world of Code wher you navigate the monsters of the internet. Viruses and ransomware await!")
health = 100
damage = 1
time.sleep(2)
print("This is a Rougelike. You start with 100 Health. And a damage counter of 1. The more rooms you go through the more powerful you become. Good Luck.")
roomnum=0
while True:
    print("Lets walk you through your journey. First take down this trojan! Ready Up")
    time.sleep(5)
    health,damage=Trojan(health,damage)
    if health<=0:
        print("You died game over!")
        break
    print("Nice you survived this time. Lets see how you did!")
    time.sleep(2)
    print(health)
    print(damage)
    print("Great you can now buff your damage or your health. Choose wisely!")
    time.sleep(2)
    print("Buff Damage or Buff Health")
    choice = int(input("1 for damage and 2 for health "))
    if choice == 1:
        print("Upgrading Damage")
        damage=damage+random.randint(1,5+roomnum)
        print("Damage is now " + str(damage))
    elif choice == 2:
        print("Upgrading Health")
        health=health+random.randint(1,20+roomnum)
        print("Health is now " + str(health))
    roomnum=roomnum+1
    print("You passed the first part of the tutorial now for the next battle.")
    time.sleep(2)
    print("Deal with this virus. Hint brain beats brawn now!")
    time.sleep(2)
    health,damage=Virus(health,damage)
    if health<=0:
        print("You died game over!")
        break
    roomnum=roomnum+1
    print("Surprising, you seem to be excelling in this. Take another gift. On the house!")
    time.sleep(2)
    print("Buff Damage or Buff Health")
    time.sleep(2)
    choice = int(input("1 for damage and 2 for health "))
    if choice == 1:
        print("Upgrading Damage")
        damage=damage+random.randint(1,5+roomnum)
        print("Damage is now " + str(damage))
    elif choice == 2:
        print("Upgrading Health")
        health=health+random.randint(1,20+roomnum)
        print("Health is now " + str(health))
    print("I suppose you might wonder why you are here.")
    time.sleep(2)
    print("After the accident, the world colapsed")
    time.sleep(2)
    print("Rather than destroying itself with a bang, the world simply fell into a Windows 10 update")
    time.sleep(2)
    print("You are the last protocol in place.")
    time.sleep(2)
    print("You are in what is known as the void. It is protected. Those who leave... ")
    time.sleep(2)
    print("Well we never see them again")
    time.sleep(2)
    print("Who I am is none of your concern. All you need to know is you need to make it to the Deep Archtecture")
    time.sleep(2)
    print("There are two enemies. The vast trojans and the Viral king")
    time.sleep(2)
    print("Destroying them will take a lot of time. And luck")
    time.sleep(2)
    print("Currently your health is " + str(health) + "you will fall into corruption if you die")
    time.sleep(2)
    print("Defeat 5 trojans to continue the lore")
    
    health,damage=Trojan(health,damage)
    if health<=0:
        print("You died game over!")
        break
    roomnum = roomnum+1
    print("Buff Damage or Buff Health")
    choice = int(input("1 for damage and 2 for health "))
    if choice == 1:
        print("Upgrading Damage")
        damage=damage+random.randint(1,5*roomnum)
        print("Damage is now " + str(damage))
    elif choice == 2:
        print("Upgrading Health")
        health=health+random.randint(1,(7*roomnum))
        print("Health is now " + str(health))

    health,damage=Trojan(health,damage)
    if health<=0:
        print("You died game over!")
        break
    print("Buff Damage or Buff Health")
    choice = int(input("1 for damage and 2 for health "))
    if choice == 1:
        print("Upgrading Damage")
        damage=damage+random.randint(1,5*roomnum)
        print("Damage is now " + str(damage))
    elif choice == 2:
        print("Upgrading Health")
        health=health+random.randint(1,(7*roomnum))
        print("Health is now " + str(health))
    
    health,damage=Trojan(health,damage)
    if health<=0:
        print("You died game over!")
        break
    print("Buff Damage or Buff Health")
    choice = int(input("1 for damage and 2 for health "))
    if choice == 1:
        print("Upgrading Damage")
        damage=damage+random.randint(1,5*roomnum)
        print("Damage is now " + str(damage))
    elif choice == 2:
        print("Upgrading Health")
        health=health+random.randint(1,(7*roomnum))
        print("Health is now " + str(health))

    health,damage=Trojan(health,damage)
    if health<=0:
        print("You died game over!")
        break
    print("Buff Damage or Buff Health")
    choice = int(input("1 for damage and 2 for health "))
    if choice == 1:
        print("Upgrading Damage")
        damage=damage+random.randint(1,5*roomnum)
        print("Damage is now " + str(damage))
    elif choice == 2:
        print("Upgrading Health")
        health=health+random.randint(1,(7*roomnum))
        print("Health is now " + str(health))

    health,damage=Trojan(health,damage)
    if health<=0:
        print("You died game over!")
        break
    print("Buff Damage or Buff Health")
    choice = int(input("1 for damage and 2 for health "))
    if choice == 1:
        print("Upgrading Damage")
        damage=damage+random.randint(1,5*roomnum)
        print("Damage is now " + str(damage))
    elif choice == 2:
        print("Upgrading Health")
        health=health+random.randint(1,(7*roomnum))
        print("Health is now " + str(health))

    print("Good. You killed them all. You might be the chosen one.")
    time.sleep(2)
    print("Now fight your first boss. Leader of trojans. King Horse")
    time.sleep(2)
    print("A massive trojan steps ahead. He roars at you.")
    print("The horse health is 1,000")
    print("The horse damage is a meager 1")
    horse=1000
    hdam=1
    while True:
        choice = input("Attack or defend")
        if choice == "1":
            print("You attacked")
            horse=horse-damage*random.randint(1,3)
            print("Horse strikes back.")
            health=health-1
            print("Horse falls back. Throws out reinforcements")
            for i in range(random.randint(0,3)):
                health,damage=Trojan(health,damage)
                health,damage=Virus(health,damage)
            print("Health: " + str(health))
            print("Trojan health: " + str(horse))
        elif choice == "2":
            print("You observe the horse. Do 5 x damage")
            horse=horse-damage*5
            print("Horse grazes you!")
            health=health-1
        if horse<=0:
            print("Horse destroyed. Victory... For now")
            break
        elif health<=0:
            print("You died. I really thought you were the chosen one")
            break
    if health <= 0:
        print("YOU FAILED TRY AGAIN")
        break
    print("Congrats hero!. You passed the demo!")
    print("The continuation is comming soon")
    print("Hoped you liked the game!")   
    print("Time to play again. But this time, stronger!")     
print("If you are out here you died!. GAME OVER!")
            

