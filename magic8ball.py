#Saisha Kapoor
#Period 3
#1/24/25

import random
magic_list = [] #maic 8 ball responses
responses = ("Yes", "No", "Maybe", )

#introduction
#prompt user to ask a question
#randomly select and display a response
#Create a loop so that the user can ask again

#Init
import random
responses = ["Yes", "Of course", "It's Likely", "Very Likely", "Very Probable", "Surely", "Possibly", "Could be", "Maybe", "Could happen", "No", "Definately Not", "Very unlikely", "Not At All", "Not Happening"]

#Functions
def Magicball():
    print("Welcome to the Magic 8 Ball Game!")
    keepGoing = "yes"
    while keepGoing != "no":
        question = (input("Give me a yes or no question"))
        print(question)
        if question.endswith("?"):
            print(random.choice(responses))
        else:
            print("Error! Give me a yes or no question with a question mark")
        keepGoing = (input("Do you want to keep playing?"))
        print(keepGoing)
        if keepGoing == "yes":
            question2 = (input("Please give me another yes or no question"))
            print(question2)
            if question.endswith("?"):
                print(random.choice(responses))
            else:
                print("Error! Give me a yes or no question with a question mark")
        if keepGoing == "no":
            print("Thank you for playing the Magic 8 Ball Game!")
            break
