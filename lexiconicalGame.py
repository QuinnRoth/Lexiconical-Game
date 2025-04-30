import re


"""
Game Rules:
    Goal: Enter a word that follows as many rules as possible.
    There are 5ish rules for the word to follow
    No googling
    Game starts by only showing you the first rule
    When you enter a word that follows the new rule a new rule appears
"""
score = 0
word = "insouciance"

def checkRules(input):
    rule1 = re.search("")


def printRules():
    if score > 4:
        print("rule 5")
    if score > 3:
        print("rule 4")
    if score > 2:
        print("rule 3")
    if score > 1:
        print("rule 2")
    print("rule 1")




while 1:
    printRules()
    print("Enter a word that follows the rules")
    answer = input()
    checkRules(answer)


