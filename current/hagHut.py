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

  

    if Choice == "the old hags hut":

        
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
            print("The old hag thank you for your help and wish you the best in your quest.")
            

    if quest1 == False and goblin == True:

            print("As you approach the old hag's hut, you see an old hag smiling at you. ")
                
            print("she thank you for saving her pet goblin and is willing to help your quest.")
                
            print("she tells you that there is a magical potion in the Fortress of Doom. ")
                
            print("It will cure the King. She provides you with a map and the location.  ")
                
            print("Before you leave she informs you of the fortress password 'DARKSTONE'")
            quest1 = True

    if quest1 == False and goblin == False:
            print("As you approach the old hag's hut, an army of crows chase you away.")
