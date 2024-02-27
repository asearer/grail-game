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
        print("SIR BEDEVERE: And that, my liege, is how we know the earth to be banana-shaped.")
        print("ARTHUR: This new learning amazes me, Sir Bedevere. Explain again how sheep's bladders may be employed to prevent earthquakes. ")
        print("BEDEVERE: Oh, certainly, sir.")
        print("SIR LANCELOT: Look, my liege! ")
        print("ARTHUR: Camelot!")
        print("SIR GALAHAD: Camelot!")
        print("LANCELOT: Camelot!")
        

         

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
        
        print("PATSY: It's only a model.")
        print("ARTHUR: Shh! Knights, I bid you welcome to your new home. Let us ride... to... Camelot!")
        print("[in medieval hall]")
        print("KNIGHTS: [singing] ")
        #add mp3 knights of roundtable
        print("[outdoors]")
        print("ARTHUR: Well, on second thought, let's not go to Camelot. It is a silly place.")
        print("KNIGHTS: Right. Right.")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

       

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


