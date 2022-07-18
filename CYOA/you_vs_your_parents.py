#are you a daughter or a son? 1=daughter, 2=son
# type of personality for your character, 1=careful but preserve, 2=active but reckless
#Agrument
#Your parent go to work at 6am and come home at 5pm. You were playing video games, you slept really late so you woke up at 3pm and didn't come to class on time. 
#Your mom: "Didn't I tell u to sleep early? Why don't you listen to me?"
#choose the type of Personality to argue with your parent
#if chose 1, Your dad:"the kid is too stubborn and preserving , he/she will not listen to anyone"
#if == 2, Your dad: "the kid is to ignorant,he/she will never think anything straight!"
#Begining
#Choose your way of replying, 1 ==sorry, 2==it is not a big deal, 3==saying nothing and go to your room
#if 1, "Sorry isn't enough..."
from time import sleep
input_count=0
game_is_on=True
input_msg = ""
first_question = True


class Person():
  def __init__(self, name, points):
    self.name = name
    self.points = points

mom=Person
mom.name="Karen"
mom.points = 0 

dad=Person
dad.name="Suuga"
dad.points = 0 

child= Person
child.name="Max"
child.points = 0
 


def check_answer(user_input):
  global game_is_on
  global input_count
  global game_is_on

  if "help" in user_input:
    print("You just need to enter a number! Remember avoiding the argument is the way to win.")

  #asking for the first input
  first_rxn = user_input

  if first_rxn == str(1):
    print ("Your mom: 'Sorry isn't enough, you do this every single day.' 😩'")
    sec_rxn  = input("1. I know, I know but tomorrow will be different. I swear, I will sleep early and wake up on time. 2. � I don't do that everyday but I will show  youthat I can wake up on time tomorrow!")
    print ("Do whatever you want with your life, we just want twhat'sbest for you.🤏x100000 (Conflict solved but you tied with your parents ~*U*")
    input_count+=2

  if first_rxn == str(2):
    print ("Your mom look at you with eyes of bullets, she says: 'hen, what's the big deal? We work early just so that you can be fulfilled. What you just said devaluates all the efforts we had to put out. I think it 'sis best to send you back home.")
    sec_rxn = input ("1. Have I ever asked for any of this'2. ' think you get it wrong, I only missed a PE class so it won't do anything.")
    if sec_rxn == str(1):
      print ("You have hurt your parents'feeling sand won 💔. Woohoo!" )
      input_count+=2
    elif sec_rxn == str(2):
      print ("Your mom: 'Do not repeat, this ok?'(AYYY, you wio! You have successfully avoided an argument as well as prevented hurting your loved ones feelings🎉)")
      input_count+=2
    else:
      print ("Please enter a valid input!")

  if first_rxn == str(3):
    print ("Your mom: " + ", why don't you answer me? What is  withthat attitude? Do you still view us as your parents, " + "? Come out here!!!!!!!")
    sec_rxn = input ("1. No reply again 2. Lose your cool and act out by throwing and breaking objects 🤬")
    if sec_rxn == str(1):
      print("Parents barge into your room, what is wrong with you? you can't disrespect me like that in MY house.(You lost!😑✌️)")
      input_count=2
    elif sec_rxn == str(2):
      print("Your parents are stunned by your decision and you are surprised yourself. You run out of the house, your parents call mutiple times and leave multiple viocemails. While crossing the street, a car runs you over. Ambulance siren sounds  likedeath, your parents go to the hospital after someone called from your phone. You are losing consciousness. When your parents arrive, only your dad can control his emotions while your mom can't keep her tears from coming out. You see your mom crying in your subconsciousness and wake up. You and your parents are still able to see each other.")
      input_count=2
    else:
      print ("Please enter a valid input!")   
    

def prompt_user():
  global first_question
  if first_question == True:
       reply = input ("Time to reply: 1. Tell them you're sorry 2. Angrily say: It's not a big deal!' 3. Say nothing and go to your room ")
       first_question = False
  else:
       reply = input("Choose something that fits you by entering a matching number (type 'help' if you struggle): >>  ")
  return reply

def start():
  name = input("What is your name? ")
  print ("Hi, " + name)
  print ("You can type 'help' when struggling.")
  print ("Your parent go to work at 6am and come home at 5pm. You were playing video games last night, so you slept really late and woke up at 3pm and didn't go to class on time. You must win your parents in the argument or avoid it.")
  print("Choose something that fits you by entering a matching number: ")
  gender = input ("1. female, 2. male ")
  personality_choice = input ("1. Careful but stubborn or 2. Active but reckless ")
  if personality_choice == str(1) and gender == str(1):
    print ("Your dad: The kid is too preserving, she will forever be that selfish. Why did you miss class?")
  elif personality_choice == str(2) and gender == str(1):
    print ("Your dad: The kid is too ignorant, she will never understand any of our thoughts. Why did you miss class?")
  elif personality_choice == str(1) and gender == str(2):
    print ("Your dad: The kid is too preserving, he will forever be that selfish. Why did you miss class?")
  elif personality_choice == str(2) and gender == str(2):
    print ("Your dad: The kid is too ignorant, he will never understand any of our thoughts. Why did you miss class?")
  else:
    print ("Please enter a valid input!")
 

  while game_is_on:

    if input_count==2:
      game_is_on == False
      print("        GGGGGGGGGGGGG                                                                        OOOOOOOOO                                                                   ")
      sleep(0.2)
      print("     GGG::::::::::::G                                                                      OO:::::::::OO                                                                 ")
      sleep(0.2)
      print("   GG:::::::::::::::G                                                                    OO:::::::::::::OO                                                               ")
      sleep(0.2)
      print("  G:::::GGGGGGGG::::G                                                                   O:::::::OOO:::::::O                                                              ")
      sleep(0.2)
      print(" G:::::G       GGGGGG  aaaaaaaaaaaaa      mmmmmmm    mmmmmmm       eeeeeeeeeeee         O::::::O   O::::::Ovvvvvvv           vvvvvvv eeeeeeeeeeee    rrrrr   rrrrrrrrr   ")
      sleep(0.2)
      print("G:::::G                a::::::::::::a   mm:::::::m  m:::::::mm   ee::::::::::::ee       O:::::O     O:::::O v:::::v         v:::::vee::::::::::::ee  r::::rrr:::::::::r  ")
      sleep(0.2)
      print("G:::::G                aaaaaaaaa:::::a m::::::::::mm::::::::::m e::::::eeeee:::::ee     O:::::O     O:::::O  v:::::v       v:::::ve::::::eeeee:::::eer:::::::::::::::::r ")
      sleep(0.2)
      print("G:::::G    GGGGGGGGGG           a::::a m::::::::::::::::::::::me::::::e     e:::::e     O:::::O     O:::::O   v:::::v     v:::::ve::::::e     e:::::err::::::rrrrr::::::r")
      sleep(0.2)
      print("G:::::G    G::::::::G    aaaaaaa:::::a m:::::mmm::::::mmm:::::me:::::::eeeee::::::e     O:::::O     O:::::O    v:::::v   v:::::v e:::::::eeeee::::::e r:::::r     r:::::r")
      sleep(0.2)
      print("G:::::G    GGGGG::::G  aa::::::::::::a m::::m   m::::m   m::::me:::::::::::::::::e      O:::::O     O:::::O     v:::::v v:::::v  e:::::::::::::::::e  r:::::r     rrrrrrr")
      sleep(0.2)
      print("G:::::G        G::::G a::::aaaa::::::a m::::m   m::::m   m::::me::::::eeeeeeeeeee       O:::::O     O:::::O      v:::::v:::::v   e::::::eeeeeeeeeee   r:::::r            ")
      sleep(0.2)
      print(" G:::::G       G::::Ga::::a    a:::::a m::::m   m::::m   m::::me:::::::e                O::::::O   O::::::O       v:::::::::v    e:::::::e            r:::::r            ")
      sleep(0.2)
      print("  G:::::GGGGGGGG::::Ga::::a    a:::::a m::::m   m::::m   m::::me::::::::e               O:::::::OOO:::::::O        v:::::::v     e::::::::e           r:::::r            ")
      sleep(0.2)
      print("   GG:::::::::::::::Ga:::::aaaa::::::a m::::m   m::::m   m::::m e::::::::eeeeeeee        OO:::::::::::::OO          v:::::v       e::::::::eeeeeeee   r:::::r            ")
      sleep(0.2)
      print("     GGG::::::GGG:::G a::::::::::aa:::am::::m   m::::m   m::::m  ee:::::::::::::e          OO:::::::::OO             v:::v         ee:::::::::::::e   r:::::r            ")
      sleep(0.2)
      print("        GGGGGG   GGGG  aaaaaaaaaa  aaaammmmmm   mmmmmm   mmmmmm    eeeeeeeeeeeeee            OOOOOOOOO                vvv            eeeeeeeeeeeeee   rrrrrrr            ")
      sleep(0.2)
      print("                                                                                                                                                                         ")
      break
    else:
      check_answer(prompt_user())

start()