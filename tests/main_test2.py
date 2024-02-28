import random
import time
from pygame import mixer

cure = False
goblin = False
quest1 = False
potion = False





Name = input("What is your name brave Sir Knight ? ")

print("Hello "+Name)

print("I seek the finest and the bravest knights in the land to join me in my court at Camelot. ")
print("You must join me. ")



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
        #loading part
        print('--------------------------------------')
        print('Now Loding...')
        time.sleep(0.5)
        print('Now loading the player setting...')
        time.sleep(2)
        print('Great Success!')
        time.sleep(0.5)
        print('Now loading the game setting...')
        time.sleep(2)
        print('Great Success!')
        time.sleep(0.5)
        print('.....................................')
        time.sleep(2)
        print('Very nice!')
        time.sleep(0.5)
        print('Now game is ready!')
        print('--------------------------------------')

                #         Audio

  
# Starting the mixer
        mixer.init()
  
# Loading the song
        mixer.music.load("Rick Astley.mp3")
  
# Setting the volume
        mixer.music.set_volume(0.7)
  
# Start playing the song
        mixer.music.play()



 #if player enters correct command when asked where they want to go it opens up the oregon trail
    elif Choice == "easter egg":


    #welcome player
        print('Welcome to the Oregon Trail ')


#asking name
player_name = input('What is your name:')
while len(player_name) >= 0:
  if len(player_name) > 1:
    print(str(player_name)+"? It is a good name, a little silly but still good.")
    break
  if len(player_name) == 1:
    player_name_choice = input(str(player_name)+"? Are you kidding me? Only one letter?(y/n):")
    if player_name_choice == "y" or player_name_choice == "Y":
      print("Ok...")
      break
    if player_name_choice == "n" or player_name_choice == "N":
      player_name = input('What is your name:')
  else:
    print("You do not type anything, try again")
    player_name = input('What is your name:')

#easter eggs for name
if player_name == 'Meriwether Lewis':
  year_set = 1803
  mode_choice = 'impossible'
else:
  year_set = input('Enter a year whatever you like:')
  if year_set.isdigit():
    return_num = 0
  else:
    return_num = 1
  while return_num == 1:
    print('Erro,please try again!')
    year_set = input('Enter a year whatever you like:')
    if year_set.isdigit():
      return_num = 0
    else:
      return_num = 1
  year_set = int(year_set)
  print('Which mode do you want to play?')
  mode_choice = input('(easy,normal,hard,impossible,customize):')

#leap year function

'''
if (year_set % 4) == 0:
   if (year_set % 100) == 0:
       if (year_set % 400) == 0:
           print('leap year')
       else:
           print('no leap year')
   else:
       print('leap year')
else:
   print('no leap year')
'''

while len(mode_choice) >= 0: 
#easy mode:
  if mode_choice == 'easy':
    food_num = 1000
    health_num = 10
    break
#noraml mode:
  elif mode_choice == 'normal':
    food_num = 500
    health_num = 5
    break
#hard mode:
  elif mode_choice == 'hard':
    food_num = 300
    health_num = 4
    break
#impossible mode:
  elif mode_choice == 'impossible':
    food_num = 150
    health_num = 3
    break
#customize mode:
  elif mode_choice == 'customize':
    #food number take in
    food_num = input('How much food do you want:')
    if food_num.isdigit():
      return_cm_num = 0
    else:
      return_cm_num = 1
    while return_cm_num == 1:
      print('Erro,please try again!')
      food_num = input('How much food do you want:')
      if food_num.isdigit():
        return_cm_num = 0
      else:
        return_cn_num = 1
    food_num = int(food_num)
    #health number take in
    health_num = input('How much health do you want:')
    if health_num.isdigit():
      return_cm_num2 = 0
    else:
      return_cm_num2 = 1
    while return_cm_num2 == 1:
      print('Erro,please try again!')
      health_num = input('How much health do you want:')
      if health_num.isdigit():
        return_cm_num2 = 0
      else:
        return_cn_num2 = 1
    health_num = int(health_num)
    break
#erro?
  else:
    print("Bad input, try again!")
    mode_choice = input('(easy,normal,hard,impossible,customize):')
    

#other basic strating value setting
player_move_distance = 0
month_num = 3
days_pass = 1
total_days = 0
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
random_result = 0
health_d1 = random.randint(1, 31)
health_d2 = random.randint(1, 31)
acident_appear = random.randint(1, 30)
travel_total_num = 0
rest_total_num = 0
hunt_total_num = 0
status_total_num = 0
month_appear = 'March'

#add days:
def add_days(min, max):
  global days_pass
  global month_num
  global MONTHS_WITH_31_DAYS
  global random_result
  global food_num
  global health_num
  global health_d1
  global health_d2
  global total_days
  global acident_appear

  random_result = random.randint(min, max)
  print('Now',random_result,"days passed..")
  days_pass_min = days_pass
  check_big = days_pass + random_result

  #acident
  if acident_appear >= days_pass and acident_appear <= check_big:
    a_number = random.randint(1, 3)
    a_health_num = random.randint(1, 2)
    if a_number == 1:
      print('During this time, you crossed a river.')
    if a_number == 2:
      print('During this time, you had a dysentery.')
    if a_number == 3:
      print('During this time, you saw a beautiful girl and had a good time with her.')
    random_result2_food = random.randint(1, 10)
    random_result2_day = random.randint(1, 10)
    print('As a result, you eat '+str(random_result2_food)+' lbs extra food.')
    print('It also took up eatra '+str(random_result2_day)+' days.')
    if a_health_num == 1:
      print('And you also lose 1 health')
      health_num -= 1
    food_num = food_num - random_result2_food - random_result2_day*5
    days_pass += random_result2_day
    total_days += random_result2_day
  #health decrease randomly  
  check_big = days_pass + random_result
  if health_d1 >= days_pass_min and health_d1 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')
  if health_d2 >= days_pass_min and health_d2 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')


  days_pass += random_result
  total_days += random_result
  food_num -= random_result * 5

  if days_pass >= 30:
    if month_num not in MONTHS_WITH_31_DAYS:
      if days_pass > 30:
        days_pass -= 30
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)
    else:
      if days_pass > 31:
        days_pass -= 31
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)

#function part
def travle1(movedistance):
  global days_pass
  global travel_total_num
  add_days(3,7)
  movedistance = movedistance + random.randint(30, 60)
  travel_total_num += 1
  return movedistance

def rest(health):
  global days_pass
  global rest_total_num
  add_days(2,5)
  health = health + 1
  rest_total_num += 1
  return health

def hunt(hunting_food):
  global days_pass
  global hunt_total_num
  add_days(2,5)
  hunting_food = hunting_food + 100
  print('Gain: 100 lbs food')
  hunt_total_num += 1
  return hunting_food

#month_appear
def month_appear_fun():
  global month_appear
  if month_num == 1:
    month_appear = 'January'
  elif month_num == 2:
    month_appear = 'February'
  elif month_num == 3:
    month_appear = 'March'
  elif month_num == 4:
    month_appear = 'April'
  elif month_num == 5:
    month_appear = 'May'
  elif month_num == 6:
    month_appear = 'June'
  elif month_num == 7:
    month_appear = 'July'
  elif month_num == 8:
    month_appear = 'August'
  elif month_num == 9:
    month_appear = 'September'
  elif month_num == 10:
    month_appear = 'October'
  elif month_num == 11:
    month_appear = 'November'
  elif month_num == 12:
    month_appear = 'December'
  return month_appear

#loading part
print('--------------------------------------')
print('Now Loding...')
time.sleep(0.5)
print('Now loading the player setting...')
time.sleep(2)
print('Great Success!')
time.sleep(0.5)
print('Now loading the game setting...')
time.sleep(2)
print('Great Success!')
time.sleep(0.5)
print('Prepearing the trip for Oregon...')
time.sleep(2)
print('Very nice!')
time.sleep(0.5)
print('Now game is ready!')
print('--------------------------------------')

#main
while player_move_distance < 2000 and food_num > 0 and health_num > 0 and month_num < 13:
  month_appear_fun()
  if food_num <= 50:
    print('Warning! You only have '+ str(food_num) + " lbs food now.")
    print('You need hunt now.')
  if health_num <= 2:
    print('Warning! You only have '+ str(health_num) + " health now.")
    print('You need a rest.')
  print(str(player_name) + ', now it is ' + month_appear + ' '+str(days_pass) + ', ' + str(year_set) + ", and you have travled " + str(player_move_distance) + " miles.")
  choice = input('Your choice:')
  if choice == 'travel':
    player_move_distance = travle1(player_move_distance)
  elif choice == 'rest':
    if health_num < 5:
      print("You get 1 heath!")
      health_num = rest(health_num)
    if health_num >= 5:
      print("Your health is full, the maximum number for health is 5!")
  elif choice == 'hunt':
    food_num = hunt(food_num)
  elif choice == 'status':
    print('-Dear ' + str(player_name) + ', now is '+str(month_num)+'/'+str(days_pass)+'/'+str(year_set)+".")
    print('-Food:',food_num,"lbs")
    print('-Health:',health_num)
    print('-Distance traveled:',player_move_distance)
    distance_left = 2000 - player_move_distance
    print('-'+str(total_days) +' days have passed.')
    print('-You have travled ' + str(player_move_distance) + " miles, there is still " + str(distance_left) + ' miles left.')
    status_total_num += 1
  elif choice == 'help':
    print('[travel]: moves you randomly between 30-60 miles and takes 3-7 days (random).')
    print('[rest]: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).')
    print('[hunt]: adds 100 lbs of food and takes 2-5 days (random).')
    print('[status]: lists food, health, distance traveled, and day.')
    print('[quit]: will end the game.')
  elif choice == 'quit':
    quit_choice = input('Are you sure that you want to quit?(y/n)')
    if quit_choice == 'y':
      print('Game over...I cannot believe that you quit...')
      break
  elif choice == 'suicide':
    quit_choice2 = input('Are you sure?(y/n)')
    if quit_choice2 == 'y':
      print('Game over...You kill youslf...')
      break
#  elif choice == 'easter egg':
 
  else:
    print("This Choice is not available, please try again.")
  print('--------------------------------------')
#succeed!
if player_move_distance >= 2000:
  print('Nice job! you have arrived in Oregon')

#game over
if food_num <= 0:
  print('Game over, you have no food now.')

if health_num <= 0:
  print('Game over, you have no health now.')

if month_num >= 13:
  print('Game over, you run out of time!')
  
print('During the whole game, you:')
print('Travel ' + str(travel_total_num) +' times.')
print('Rest ' + str(rest_total_num) +' times.')
print('Hunt ' + str(hunt_total_num) +' times.')
print('Status ' + str(status_total_num) +' times.')

#restart
#restart_choice = input('Do you want to restart the game?')
#end oregon trail   

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
#add easter egg        

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
#add easter egg
#         
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
#add easter egg

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

#    if quest1 == True and goblin == True:
#    print("The old hag thank you for your help and wish you the best in your quest.")
                

 #   if quest1 == False and goblin == True:

    print("As you approach the old hag's hut, you see an old hag smiling at you. ")
                
    print("she then instructs you to go into the wood for what you seek.")
                
    print("she tells you that there is a place there that you may get more information. ")
                
    print("It will be a journey full of danger so be wary she warns before providing you with a map and the location.  ")
                
    print("Will you heed her warnings and follow the map? (Yes / No)")

    answer_yes = ["Ni","NI","yes","YES","Yes" "ni"]
    ans6 = input(">>")

    if ans6 in answer_yes:
          
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
          print("Your party enters the forest")

          print("HEAD KNIGHT OF NI: Ni!")
          print("KNIGHTS OF NI: Ni! Ni! Ni! Ni! Ni!")
          print("ARTHUR: Who are you?")
          print("HEAD KNIGHT: We are the Knights Who Say... 'Ni'!")
          print("ARTHUR: No! Not the Knights Who Say 'Ni'!")
          print("HEAD KNIGHT: The same!")
          print("BEDEVERE: Who are they?")
          print("HEAD KNIGHT: We are the keepers of the sacred words: 'Ni', 'Peng', and 'Neee-wom'!")
          print("ARTHUR: Those who hear them seldom live to tell the tale.")
          print("HEAD KNIGHT: The Knights Who Say 'Ni' demand a sacrifice.")
          print("ARTHUR: Knights of Ni, we are but simple travellers who seek the enchanter who lives beyond these woods.")
          print("HEAD KNIGHT: Ni!")
          print("KNIGHTS OF NI: Ni! Ni! Ni! Ni! Ni!...")
          print("ARTHUR: Ow! Ow! Ow! Agh!")
          print("HEAD KNIGHT: We shall say 'ni' again to you if you do not appease us.")
        
          print("ARTHUR: Well, what is it you want?")
          print("HEAD KNIGHT: We want... a shrubbery!")
          print("ARTHUR: A what?")
          print("KNIGHTS OF NI: Ni! Ni! Ni! Ni!")
          print("ARTHUR: Please! Please! No more! We will find you a shrubbery.")
          print("HEAD KNIGHT: You must return here with a shrubbery, or else, you will never pass through this wood... alive.")
          print("ARTHUR: O Knights of Ni, you are just and fair, and we will return with a shrubbery.")
          print("HEAD KNIGHT: One that looks nice.")
          print("ARTHUR: Of course.")
          print("HEAD KNIGHT: And not too expensive.")
          print("HEAD KNIGHT: Now... go!")
       

          print("Your party leaves this place")
          print("You depart from the forest with empty hands, but but return with a shubbery.")
#add easter egg
        
#            quest1 = True

#        if quest1 == False and goblin == False:
#    print("As you approach the old hag's hut, an army of crows chase you away.")

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
#add easter egg
#choice d is rick
if Choice == "d":

        #         Audio

  
# Starting the mixer
#mixer.init()
  
# Loading the song
#mixer.music.load("Rick Astley.mp3")
  
# Setting the volume
#mixer.music.set_volume(0.7)
  
# Start playing the song
#mixer.music.play()

       

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
        
                    

print("Press any button to exit the game")
input()
exit()

        
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



