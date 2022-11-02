# Python Setup Link https://code.visualstudio.com/docs/python/python-tutorial
import os
from tkinter.messagebox import YES
import openai

# Initial message to explain the application and how to use it
print("This application will take your answers and randomly pull locations that match what you wanted.")
print("For the best results when answering questions, follow the examples shown at the end of each message.")

# Initialize Query String
# Will be sent to GPT-3
qString = "Give me a list of "

# input() method prints whatever string you have in the parenthesis
# and returns whatever input was provided in the terminal
# Also storing the location type input to be used later in the code 
location = input(
    "What type of location would you like to stay at?(E.G. hotel): ")

# The repeated qString += is concatenating the input from the user to the end of the Query String
qString += location + "s in "
qString += input("Where do you want to go? (E.G. city, state or state, country): ")

# GPT-3 seems to use daily price of staying for one person, 
# so the program requests the amount of days the user will be staying,
# the amount of people they are paying for, and their budget.
days = float(input("How many days do you wish to stay? (E.G. 1,2,3,etc.): "))
people = float(
    input("How many people are you paying for? (E.G. 1,2,3,etc.): "))
cost = float(input("What is your budget in US dollars?(E.G. 1000): "))

# perDayCost is the max price the user can spend for each person every day and stay in budget
perDayCost = str(round(cost/people/days, 2))
qString += " that cost less than $" + perDayCost + " per day and have a "
qString += input("What rating(stars specifically) would you like the establishment to have?(E.G. 1,2,3-5,etc.): ") + " star rating."

# Optional Questions below that can be answered with a yes or no response. 
if input("Would you like to answer additional questions to make the search more accurate?(E.G. yes or no): ") == "yes":
    print("For the following questions, answer with yes or no.")
    questions = ["Wifi", "Breakfast", "Cable",
                 "24 hour check in", "a Gym", "a Pool"]
    optionalString = ""
    atLeastOne = False
    loopIndex = 0
    yesResponses = []
    for x in questions:
        if input("Do you want " + x + "?: ").lower() == "yes":
            yesResponses.append(x)
            atLeastOne = True
    if len(yesResponses) > 1:
        for x in yesResponses:
            if loopIndex == len(yesResponses)-1:
                optionalString += "and " + x + "."
            else:
                optionalString += x + ", "
            loopIndex += 1
    elif len(yesResponses) == 1:
        optionalString += yesResponses[0] + "."
    if (atLeastOne):
        qString += " The " + location + "s should have " + optionalString

print(qString)

openai.api_key = "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"
searchRequest = qString
response = openai.Completion.create(
    model="text-davinci-002",
    prompt=searchRequest,
    max_tokens=256,
    temperature=0.7
)

print(response["choices"][0]["text"])
print(" ")

