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
    print("Where do you want to go ? (Castle, The Wild Forest )")
    print(" Castle   The Wild Forest ")
    Choice = input()
    Choice = Choice.lower()

  

    if Choice == "the wild forest":
        print("You enter the wild forest....")

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

        