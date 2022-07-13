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
game_is_on = True
input_msg = " "
name = " "
 
def prompt_user():
       reply = input("lease choose what would fit with you by entering a matching number!  >>  ")
       return reply
 
def check_answer(input):
       global name
       input_msg = input
 
       if "help" in input_msg:
           print("Here are some commands you can try: .....")
           print("help, end, greet")
 
       elif "end" in input_msg:
           global game_is_on
           game_is_on = False
           print("Thank you for playing, goodbye!")
           
       elif "greet" in input_msg:
           print("Hello " + name)
 
       else:
           print("Sorry, I don't know what that means.")

def start():
    global name
    name = input("What is your name? ")
    print ("Welcome, " + name + "!")
    print ("Your parent has to go to work at 6am and come home at 5pm. You were playing video games last night, so you slept really late and woke up at 10 am and didn't come to class on time.")
    print ("Your mom: 'Didn't I tell u to sleep early? Why don't you listen to me?' (insert angry emoji)")
    gender = input ("1. female, 2. male")
    personality_choice = input ("1. Careful but stubborn or 2. Active but reckless")
    if personality_choice == 1 and gender == 1:
      print ("Your dad: 'The kid is too preserving, she will forever be that selfish.'")
    elif personality_choice == 2 and gender == 1:
      print ("Your dad: 'The kid is too ignorant, she will never understand any of our thoughts.'")
    elif personality_choice == 1 and gender == 2:
      print ("Your dad: 'The kid is too preserving, he will forever be that selfish.'")
    elif personality_choice == 2 and gender == 2:
      print ("Your dad: 'The kid is too ignorant, he will never understand any of thoughts'")
    else:
      print ("Please enter a valid input!")
    
    check_answer(prompt_user())
start()