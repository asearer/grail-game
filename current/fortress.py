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
    print("Where do you want to go ? (Castle, Fortress )")
    print(" Castle   Fortress ")
    Choice = input()
    Choice = Choice.lower()

  

    if Choice == "fortress":
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