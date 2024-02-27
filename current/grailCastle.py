grail = False
goblin = False
quest1 = False
potion = False


print("")
print("")
print
print("""  

       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'



""")


Name = input("What is your name brave Sir Knight ? ")

print("Hello "+Name)

print("I seek the finest and the bravest knights in the land to join me in my court at Camelot. ")

answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

while grail == False:

    print("                                    ")
    print("Where do you want to go ? (Castle, The Old Hags Hut )")
    print(" Castle   The Old Hags Hut ")
    Choice = input()
    Choice = Choice.lower()

  

    if Choice == "castle":
        print("You arrive at a lone castle in the highlands")


         

        print("""

                                -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )






              """)
        
        print("FRENCH GUARD: Allo! Who is eet?")
        print("ARTHUR: It is King Arthur, and these are my Knights of the Round Table. Whose castle is this?")
        print("FRENCH GUARD: This is the castle of my master, Guy de Loimbard.")
        print("ARTHUR: Go and tell your master that we have been charged by God with a sacred quest. If he will give us food and shelter for the night, he can join us in our quest for the Holy Grail.")
        print("FRENCH GUARD: Well, I'll ask him, but I don't think he'll be very keen. Uh, he's already got one, you see.")
        print("ARTHUR: What?")
        print("GALAHAD: He says they've already got one!")
        print("ARTHUR: Are you sure he's got one?")
        print("FRENCH GUARD: Oh, yes. It's very nice-a. (I told him we already got one.)")
        print("FRENCH GUARDS: [chuckling]")
        print("ARTHUR: Well, u-- um, can we come up and have a look?")
        print("FRENCH GUARD: Of course not! You are English types-a!")
        print("ARTHUR: Well, what are you, then?")
        print("FRENCH GUARD: I'm French! Why do think I have this outrageous accent, you silly king-a?!")
        print("GALAHAD: What are you doing in England?")
        print("FRENCH GUARD: Mind your own business!")

        print("Do you threaten the Frenchman with force? (Yes / No")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("ARTHUR: If you will not show us the Grail, we shall take your castle by force!")
        print("FRENCH GUARD: You don't frighten us, English pig-dogs! Go and boil your bottom, sons of a silly person. I blow my nose at you, so-called Arthur King, you and all your silly English k-nnnnniggets. Thpppppt! Thppt! Thppt!")
        print("GALAHAD: What a strange person.")
        print("ARTHUR: Now look here, my good man--")
        print("FRENCH GUARD: I don't wanna talk to you no more, you empty headed animal food trough wiper! I fart in your general direction! Your mother was a hamster and your father smelt of elderberries!")
        print("GALAHAD: Is there someone else up there we could talk to?")
        print("FRENCH GUARD: No. Now, go away, or I shall taunt you a second time-a!")


        print("Do you stand your ground? (Yes / No)")
        
    elif ans2 in answer_no:
       
        print("We must leave this place.")
        print("You depart from the castle with empty hands.")

#        
    ans3 = input(">>")

    if ans3 in answer_yes:
            print("ARTHUR: Now, this is your last chance. I've been more than reasonable.")
            print("FRENCH GUARD: (Fetchez la vache.)")
            print("OTHER FRENCH GUARD: Quoi?")
            print("FRENCH GUARD: (Fetchez la vache!)")
            print("[mooo]")
            print("ARTHUR: If you do not agree to my commands, then I shall--")
            print("[twong]")
            print("[mooooooo]")
            print("Jesus Christ!")
            print("KNIGHTS: Christ!")
            print("[thud]")
            print("Ah! Ohh!...")

            print("Will you stay and fight? (Yes / No)")

    elif ans3 in answer_no:
       
            print("We must leave this place.")
            print("You depart from the castle with empty hands.")


    ans4 = input(">>")



    if ans4 in answer_yes:
       
            print("ARTHUR: Right! Charge!")
            print("KNIGHTS: Charge!")
            print("[mayhem]")
            print("FRENCH GUARD: Hey, this one is for your mother! There you go.")
            print("[mayhem]")
            print("FRENCH GUARD: And this one's for your dad!")
            print("ARTHUR: Run away!")
            print("ARTHUR: Run away!")
            print("LANCELOT: Fiends! I'll tear them apart!")
            print("ARTHUR: No, no. No, no.")
            print("BEDEVERE: Sir! I have a plan, sir.")
            print("Will you use Sir Bedivere's plan? (Yes / No)")

    elif ans4 in answer_no:
       
            print("We must leave this place.")
            print("You depart from the castle with empty hands.")
    ans5 = input(">>")



    if ans5 in answer_yes:
        
            print("Later...")
            print("[wind]")
            print("[saw saw saw saw saw saw saw saw saw saw saw saw saw saw saw saw]")
            print("[clunk]")
            print("[bang]")
            print("[rewr!]")
            print("[squeak squeak squeak squeak squeak squeak squeak squeak squeak squeak]")
            print("FRENCH GUARDS: [whispering] C'est un lapin, lapin de bois. Quoi? Un cadeau. What? A present. Oh, un cadeau. Oui, oui. Allons-y. What? Let's go. Oh. On y va. Bon magne. Over here...")
            print("ARTHUR: What happens now?")
            print("BEDEVERE: Well, now, uh, Lancelot, Galahad, and I, uh, wait until nightfall, and then leap out of the rabbit, taking the French, uh, by surprise. Not only by surprise, but totally unarmed!")
            print("ARTHUR: Who leaps out?")
            print("BEDEVERE: U-- u-- uh, Lancelot, Galahad, and I, uh, leap out of the rabbit, uh, and uh...")
            print("ARTHUR: Ohh.")
            print("BEDEVERE: Oh. Um, l-- look, i-- i-- if we built this large wooden badger--")
            print("[clank]")
            print("[twong]")
            print("ARTHUR: Run away!")
            print("KNIGHTS: Run away! Run away! Run away! Run away! Run away! Run away! Run away!")
            print("You depart from the castle with empty hands and great haste!.")

    elif ans4 in answer_no:
       
            print("We must leave this place.")
            print("You depart from the castle with empty hands and great haste!.")