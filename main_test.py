cure = False
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
print("You must join me. ")

while cure == False:

    print("                                    ")
    print("Where do you want to go ? (A,B,C or D ")
    print("A) Castle  B) The Old Hags Hut  C) The Wild Forest  D) Fortress of Doom")
    Choice = input()
    Choice = Choice.lower()

    if Choice == "a":
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

    answer_yes = ["Yes", "Y", "yes", "y"]
    answer_no = ["No", "N", "no", "n"]
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

    if Choice == "b":

        print("""


        /^\ 
       // \\    ,@@@@@@@,
      //   \\ ,@@@\@@@@/@@,
     // === \\ @@\@@@/@@@@@
    // =-=-= \\@@@@\@@@@@@;%
   //   ===   \\@@@@@@/@@@%%%,
  //|         |\\@\\//@@%%%%%%
  ~ |         | ~ @|| %\\//%%%
    |  __ __  |    || %%||%%'
    | |  |  | |    ||   ||
    | | -|- | |    ||   ||
    |_|__|__|_|    ||   ||
  /`  =======  `\__||_._||
/`    =======            `\





""")

        if quest1 == True and goblin == True:
            print(
                "The old hag thank you for your help and wish you the best in your quest.")

        if quest1 == False and goblin == True:

            print(
                "As you approach the old hag's hut, you see an old hag smiling at you. ")
            print(
                "she thank you for saving her pet goblin and is willing to help your quest.")
            print(
                "she tells you that there is a magical potion in the Fortress of Doom. ")
            print(
                "It will cure the King. She provides you with a map and the location.  ")
            print("Before you leave she informs you of the fortress password 'DARKSTONE'")
            quest1 = True

        if quest1 == False and goblin == False:
            print("As you approach the old hag's hut, an army of crows chase you away.")

    if Choice == "c":
        print("You enter the forest....")

        print("""

           * *    
           *    *  *
      *  *    *     *  *
     *     *    *  *    *
 * *   *    *    *    *   *
 *     *  *    * * .#  *   *
 *   *     * #.  .# *   *
  *     "#.  #: #" * *    *
 *   * * "#. ##"       *
   *       "###
             "##
              ##.
              .##:
              :###
              ;###
            ,####.
/\/\/\/\/\/.######.\/\/\/\/\         


""")
        print("Upon your arrival in the forest your party encounters a large, imposing knight in black armor deuling with a knight in green armor")

        print("BLACK KNIGHT: Aaaagh!")
        print("BLACK KNIGHT: Aaagh!")
        print("GREEN KNIGHT: Ooh!")
        print("BLACK KNIGHT and GREEN KNIGHT: Agh!, oh!")
        print("GREEN KNIGHT: Aaaaaah! Aaaaaaaaah!")
        print("[BLACK KNIGHT kills GREEN KNIGHT]")
        print("ARTHUR: You fight with the strength of many men, Sir Knight.")
        print("ARTHUR: I am Arthur, King of the Britons.")
        print("ARTHUR: I seek the finest and the bravest knights in the land to join me in my court at Camelot. You have proved yourself worthy. Will you join me?")
        print("[SILENCE]")
        print("ARTHUR: You make me sad. So be it. Come, Patsy.")
        print("BLACK KNIGHT: None shall pass.")

        print("Do you cross the path and continue on your journey? (Yes / No")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("BLACK KNIGHT: None shall pass.")
        print("ARTHUR: I have no quarrel with you, good Sir Knight, but I must cross this bridge.")
        print("BLACK KNIGHT: Then you shall die.")
        print("ARTHUR: I command you, as King of the Britons, to stand aside!")
        print("BLACK KNIGHT: I move for no man.")
        print("ARTHUR: So be it!")
        print("ARTHUR and BLACK KNIGHT: Aaah!, hiyaah!")
        print("[ARTHUR chops the BLACK KNIGHT's left arm off]")
        print("ARTHUR: Now stand aside, worthy adversary.")
        print("BLACK KNIGHT: 'Tis but a scratch.")
        print("ARTHUR: A scratch? Your arm's off!")
        print("BLACK KNIGHT: No, it isn't.")
        print("ARTHUR: Well, what's that, then?")
        print("BLACK KNIGHT: I've had worse.")
        print("ARTHUR: You liar!")
        print("BLACK KNIGHT: Come on, you pansy!")
        print("[ARTHUR chops the BLACK KNIGHT's right arm off]")
        print("ARTHUR: Victory is mine!")
        print("[kneeling]")
        print("ARTHUR:")
        print("We thank Thee Lord, that in Thy mer--")
    
        print("Do you cross the path and continue on your journey? (Yes / No")
#rest for no, add delay?
    ans3 = input(">>")

    if ans3 in answer_yes:

        print("BLACK KNIGHT: Hah!")
        print("[kick]")
        print("BLACK KNIGHT: Come on, then.")
        print("ARTHUR: What?")
        print("BLACK KNIGHT: Have at you!")
        print("[kick]")
        print("ARTHUR: Eh. You are indeed brave, Sir Knight, but the fight is mine.")
        print("BLACK KNIGHT: Oh, had enough, eh?")
        print("ARTHUR: Look, you stupid bastard. You've got no arms left.")
        print("BLACK KNIGHT: Yes, I have.")
        print("ARTHUR: Look! ")
        print("BLACK KNIGHT: Just a flesh wound.")
        print("[kick]")
        print("ARTHUR: Look, stop that.")
        print("BLACK KNIGHT: Chicken!")
        print("ARTHUR: Look, I'll have your leg.")
        print("[ARTHUR chops the BLACK KNIGHT's right leg off]")
        print("BLACK KNIGHT: Right. I'll do you for that!")
        print("ARTHUR: You'll what?")
        print("BLACK KNIGHT: Come here!")
        print("ARTHUR: What are you going to do, bleed on me?")
        print("BLACK KNIGHT: I'm invincible!")
        print("ARTHUR: You're a looney.")
        print("BLACK KNIGHT: The Black Knight always triumphs! Have at you! Come on, then.")
        print("[whop]")
        print("[ARTHUR chops the BLACK KNIGHT's last leg off]")
        print("BLACK KNIGHT: Oh? All right, we'll call it a draw.")
        print("ARTHUR: Come, Patsy.")
        print("BLACK KNIGHT: Oh. Oh, I see. Running away, eh? You yellow bastards! Come back here and take what's coming to you. I'll bite your legs off! ")
        print("Your party leaves this place")
        print("You depart from the forest with empty hands.")

    elif ans3 in answer_no:
       
        print("BLACK KNIGHT: Hah!")
        print("[kick]")
        print("BLACK KNIGHT: Come on, then.")
        print("ARTHUR: What?")
        print("BLACK KNIGHT: Have at you!")
        print("[kick]")
        print("ARTHUR: Eh. You are indeed brave, Sir Knight, but the fight is mine.")
        print("BLACK KNIGHT: Oh, had enough, eh?")
        print("ARTHUR: Look, you stupid bastard. You've got no arms left.")
        print("BLACK KNIGHT: Yes, I have.")
        print("ARTHUR: Look! ")
        print("BLACK KNIGHT: Just a flesh wound.")
        print("[kick]")
        print("ARTHUR: Look, stop that.")
        print("BLACK KNIGHT: Chicken!")
        print("ARTHUR: Look, I'll have your leg.")
        print("[ARTHUR chops the BLACK KNIGHT's right leg off]")
        print("BLACK KNIGHT: Right. I'll do you for that!")
        print("ARTHUR: You'll what?")
        print("BLACK KNIGHT: Come here!")
        print("ARTHUR: What are you going to do, bleed on me?")
        print("BLACK KNIGHT: I'm invincible!")
        print("ARTHUR: You're a looney.")
        print("BLACK KNIGHT: The Black Knight always triumphs! Have at you! Come on, then.")
        print("[whop]")
        print("[ARTHUR chops the BLACK KNIGHT's last leg off]")
        print("BLACK KNIGHT: Oh? All right, we'll call it a draw.")
        print("ARTHUR: Come, Patsy.")
        print("BLACK KNIGHT: Oh. Oh, I see. Running away, eh? You yellow bastards! Come back here and take what's coming to you. I'll bite your legs off! ")
        print("Your party leaves this place")
        print("You depart from the forest with empty hands.")

    if Choice == "d":

        print("""

           `,.      .   .        *   .    .      .  _    ..          .
     \,~-.         *           .    .       ))       *    .
          \ *          .   .   |    *  . .  ~    .      .  .  ,
 ,           `-.  .            :               *           ,-
  -             `-.        *._/_\_.       .       .   ,-'
  -                 `-_.,     |n|     .      .       ;
    -                    \ ._/_,_\_.  .          . ,'         ,
     -                    `-.|.n.|      .   ,-.__,'         -
      -                   ._/_,_,_\_.    ,-'              -
      -                     |..n..|-`'-'                -
       -                 ._/_,_,_,_\_.                 -
         -               ,-|...n...|                  -
           -         ,-'._/_,_,_,_,_\_.              -
             -  ,-=-'     |....n....|              -
              -;       ._/_,_,_,_,_,_\_.         -
             ,-          |.....n.....|          -
           ,;         ._/_,_,_,_,_,_,_\_.         -
  `,  '.  `.  ".  `,  '.| n   ,-.   n |  ",  `.  `,  '.  `,  ',
,.:;..;;..;;.,:;,.;:,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;:
 ][  ][  ][  ][  ][  |_i_i_H_|_|_|_H_i_i_|  ][  ][  ][  ][  ][
                     |     //=====\\     |
                     |____//=======\\____|
                         //=========\\



""")
        if quest1 == True and potion == False:

            while potion == False:
                print("You stand at the entrance of the Fortress of Doom.")
                print("You hear a booming voice.. 'Halt, what is the password ?")
                Answer = input()
                Answer = Answer.lower()

                if Answer == "darkstone":
                    print(
                        "They allow you into the Fortress and you quickly locate the magical potion.")
                    potion = True

                else:

                    print(" INCORRECT !! NOW FEAR MY POWER !! ")
                    print("A great fireball consumes your body and ends your adventure")
                    print("                   GAME OVER                   ")
                    print("""


            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    


                           """)

                    print("Press any button to exit the game")
                    input()
                    exit()

        else:
            print(
                "You arrive at the Fortress of Doom but with no purpose, you quickly leave.")


print("You pour the magical potion over the King's stone body.")
print("It has worked, the curse is removed.")
print("You are rewarded with 10,000 gold !!! ")
print("                                       ")
print("             GAME OVER                      ")
print("                                       ")
print("                                       ")

print("""

             
           (_)
          .-'-.
          |   |
          |   |
          |   |
          |   |
        __|   |__   .-.
     .-'  |   |  `-:   :
    :     `---'     :-'
     `-._       _.-'
         '""""""

""")


input("press enter to exit")


