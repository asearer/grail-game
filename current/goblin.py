if goblin == False:
            print("You see a goblin trapped in some bramble do you help (YES OR NO) ")
            Help = input()
            Help.lower()

            if Help == "yes" or Help == "YES":
                print("You help the goblin, the goblin runs back home.")
                goblin = True

        else:
            print("You see nothing of importance here, maybe you will go hunting later")