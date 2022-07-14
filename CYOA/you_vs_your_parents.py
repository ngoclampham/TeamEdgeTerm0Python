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
input_count=0
input_msg =""
game_is_on = True
def check_answer(input):

  if "help" in input:
    print("Just enter a number only! Remember avoiding the argument is the way to win.")
  if game_is_on is False:
        print("Game Over")
    

def prompt_user():
       reply = input("Choose something that fit you by entering a matching number: >>  ")
       return reply

def start():
  name = input("What is your name? ")
  print ("Welcome, " + name)
  print ("You can type 'help' when struggling.")
  print ("Your parent go to work at 6am and come home at 5pm. You were playing video games last night, so you slept really late and woke up at 3pm and didn't go to class on time.")
  print("Choose something that fit you by entering a matching number: ")
  gender = input ("1. female, 2. male ")
  personality_choice = input ("1. Careful but stubborn or 2. Active but reckless ")
  if personality_choice == str(1) and gender == str(1):
    print ("Your dad: 'The kid is too preserving, she will forever be that selfish.'")
  elif personality_choice == str(2) and gender == str(1):
    print ("Your dad: 'The kid is too ignorant, she will never understand any of our thoughts.'")
  elif personality_choice == str(1) and gender == 2:
    print ("Your dad: 'The kid is too preserving, he will forever be that selfish.'")
  elif personality_choice == str(2) and gender == str(2):
    print ("Your dad: 'The kid is too ignorant, he will never understand any of our thoughts'")
  else:
    print ("Please enter a valid input!")

#asking for the first input
  first_rxn = input ("Time to reply: 1. Telling that I'm sorry 2. Angrily saying: 'It is not a big deal!' 3. Saying nothing and go to your room")
  global input_count
  input_count = 1
  if first_rxn == str(1):
    print ("Your mom: 'Sorry isn't enough, you do this every single day.' 😩'")
    sec_rxn  = input ("1. 'I know, I know but tomorrow will be different. I swear, I will sleep early and wake up on time.' 2. '😒 I don't do that everyday but I will show that I can wake up on time tomorrow!'")
    print ("Do whatever you want with your life, we just want the best for you.🤏x100000 (Conflict solved but you tied with your parents U) ")
    input_count=2
  if first_rxn == str(2):
    print ("Your mom looking at you with the eyes of bullets, she says: 'Then, what's the big deal? We work early just so that you can be fulfilled. What you just said devaluates all the efforts we had to put out. I think it is best to send you back home.'")
    sec_rxn = input ("1. 'Have I ever asked for any of this' 2. 'I think you get it wrong, I only missed a PE class so it won't do anything.'")
    input_count=2
    if sec_rxn == str(1):
      print ("You have hurted your parents' feeling and won 💔. Woohoo!")
    elif sec_rxn == str(2):
      print ("Your mom: 'Do not repeat, ok?' (Yeh, you win. You have successfully avoided an argument as well as prevented hurting your loved ones feelings🎉)")
    else:
      print ("Please enter a valid input!")
  if first_rxn == str(3):
    print ("Your mom: " + name + ", why don't you answer me? What is that attitude? Do you still view us as your parents, " + name + "? Come out here!!!!!!!")
    sec_rxn = input ("1. No reply again 2. Can't keep your cool anymore and act out by breaking stuffs 🤬")
    input_count=2
    if sec_rxn == str(1):
      print("Parents barge into your room, what is wrong with you? you can't disrespect me like that in MY house.(You lost!😑✌️)")
    elif sec_rxn == str(2):
      print("Your parents were stunned by your decision and you are surprised by it yourself. You run out of the house, your parents call mutiple times and leave multiple viocemails. While crossing the street, a car runs you over. Ambulance siren sounds death, your parents go to the hospital after someone called from your phone. You are losing consciousness. When your parents arrive, only your dad can control his emotions while your mom can't keep her tears from coming out. You see your mom crying in your subconsciousness and wake up. You and your parents are still able to see each other.")
    else:
      print ("Please enter a valid input!")

  while game_is_on and input_count == 2:
    check_answer(prompt_user())
start()