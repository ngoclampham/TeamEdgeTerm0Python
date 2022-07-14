#############################################################################
 #                                                                  
 #  Team Edge dictionaries: Dictionaries CHALLENGES 
 # 
 #  For this activity, you will be building a dictionary and with properties
 #  and methods. You will access the properties, set new values, and use
 #  the methods to change your dictionary state. What dictionary? Ask your coach.
 # 
 #  1. DEFINE: Make a dictionary and set its properties, printing changes in between.
 #  2. MODIFY: Add 2 new properties and assing values. Change existing values,
 #     including adding or updating values inside lists
 #  3. METHODS: Now its time to make some methods tha can make a change
 #     to your values, like a boolean, or they can print something about
 #     the dictionary. Nothing fancy, unless you fancy it.
 #  4. LITERALLY: Use string literals to put it all together in one statement.
 # 
 # #########################################################################/

print("------------------- CHALLENGE 1 : DEFINE    -------------------")

#Below is a simple example of a dictionary implementaion. 
#-->TODO: Add at least 3 comments to the dictionary below to demonstrate you understand its usage

dictionary = {
    "name": "box",
    "is_empty": True
}
#working with the dictionary:
dictionary["length"] = 12
dictionary["width"] = 8
dictionary["contents"] = ["thing 1", "thing 2", "thing 3"]
print(f"{dictionary['name']} is {dictionary['length']} {dictionary['width']}")
#Add thing 4
dictionary["contents"].append("thing 4")
print(f"{dictionary['name']} has {dictionary['contents']}")
print(dictionary)

 

#-->TODO: Declare a new dictionary and set at least 4 properties to it including: string, boolean, number, list

##################################  MY dictionary ########################### #/
my_randomness = ["str", "boo", "num", "list"]
my_randomness_dict= {"str": ["pew pew", "chew chew", "pow pow"],
                     "cool?": [False],
                     "num": [1, 2],
                     "list": ["mlem mlem", "lji"]}
                    





########################################################################## #/



print("------------------- CHALLENGE 2 : MODIFY   -------------------")

#-->TODO: Print your dictionary you created above
print (my_randomness_dict)

#-->TODO: Update the dictionary you just created  by adding new properties and values, including list elements, in this section.
my_randomness_dict["cousins"] = "kwan"
my_randomness_dict["cool?"].remove(False)
my_randomness_dict["cool?"].append(True)

#-->TODO: Print your dictionary again and observe changes
print (my_randomness_dict)

print("------------------- CHALLENGE 3 : MEHTODS   -------------------")


#-->TODO: Make a method that will update your dictionary value. It should take in a dictionary and return it modified.
def update(anydict, key, value):
    anydict[key]=value
    print (anydict)

#-->TODO: Call the method.
update(my_randomness_dict, "name", "name1")

print("------------------- CHALLENGE 4 : LITERALLY   -------------------")

#-->TODO: Put it all together using a string literal to tell the story of your dictionary!
# def return_elements(list):
#     ret_string = ""
#     for l in list:
#         ret_string += str(l)+","
#         if(l==list[len(list)-1]):
#             ret_string += str(l)+""
#     return ret_string

# print("String:" + str(my_randomness_dict["string"])+ ".\n")
# + "Cool?" + str(my_randomness_dict["cool?"]) +".\n"
# +"My number: " + str(my_randomness_dict["num"])+"./n"
# +"My favorite drinks: " + return_elements (my_randomness_dict["Drinks"])

def stringlit(dict):
    stringlist=""
    for x, y in dict.items():
        stringlit+= str(x) + ","
        stringlit+= str(y) + ","
    return stringlit

print(stringlit(my_randomness_dict))
