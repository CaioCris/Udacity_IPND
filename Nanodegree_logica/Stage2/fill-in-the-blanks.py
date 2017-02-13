# All the phrases with blanks
very_easy = ("A common first thing to do in a language is display\n'Hello __1__!'  In __2__ this is particularly easy; all you have to do\nis type in:\n __3__ 'Hello __1__!'\nOf course, that isn't a very useful thing to do. However, it is an\nexample of how to output to the user using the __3__ command, and\nproduces a program which does something, so it is useful in that capacity.\n\nIt may seem a bit odd to do something in a Turing complete language that\ncan be done even more easily with an __4__ file in a browser, but it's\na step in learning __2__ syntax, and that's really its purpose.\n") #-world, python, print, 
easy = ("Almost all the __1__ languages provide a concept called __2__, which helps in executing one or more __3__ up to a desired number of times.\nAll high-level __1__ languages provide various forms of __2__, which can be used to execute one or more __3__ repeatedly.\nIn __4__ you have for __2__ and while __2__.\n") #-loop,-programming,-python,-statments
medium = ("A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by\nadding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you\ndon't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,\ntuple, and ___4___ or can be more complicated such as objects and lambda functions.\n")#-function,-arguments,-None,-
hard =  ("When you create a __1__, certain __2__s are automatically\ngenerated for you if you don't make them manually. These contain multipl\nunderscores before and after the word defining them.  When you writ\na __1__, you almost always include at least the __3__ __2__, definin\nvariables for when __4__s of the __1__ get made.  Additionally, you generall\nwant to create a __5__ __2__, which will allow a string representation\nof the method to be viewed by other developers.\n\nYou can also create binary operators, like __6__ and __7__, which\nallow + and - to be used by __4__s of the __1__.  Similarly, __8__,\n__9__, and __10__ allow __4__s of the __1__ to be compared\n(with <, >, and ==).\n")#-class,-method

#A list of the blanks to the filled
parts_in_blank  = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__", "__9__", "__10__"]

# Awnsers of each list
Awnser_very_easy = ["world", "Python", "print", "ok"]
Awnser_easy = [ "Programming", "loops", "statments", "python"]
Awnser_medium = ["function", "arguments", "None", "ok"]
Awnser_hard = ["class", "method", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok" ]

#Functions
#You can chose the level, and if the input is not value this will keep the while looping.
def chose_level(input):
    if input == "very easy":
        return very_easy
    elif input == "easy":
        return easy
    elif input == "medium":
        return medium
    elif input == "hard":
        return hard
    else:
        return "unvalid"


def fill_blank(blank, parts_in_blank):
    for gap in parts_in_blank :
        if gap in blank:
            return gap
    return None

def play_game(level, parts_in_blank):  
    replaced = []
    level = level.split()
    for blank in level:
        replacement = fill_blank(blank, parts_in_blank)
        if replacement != None:
            user_input = input("Take you guess on: " + replacement + " ")
            print(blank)
            for blank in level:
                blank = blank.replace(replacement, user_input)
                print(blank)
                replaced.append(blank)
                print(replaced)
            
            else:
                replaced.append(blank)
    replaced = " ".join(replaced)
    return replaced
    

print("Please select a game difficulty by typing it in!\n"
"Possible choices include very easy, easy, medium, and hard.")
level = input()

if level == "very easy" or level == "easy" or level == "medium" or level == "hard":
    print ("You've chosen",level,"!\n")
    print (chose_level(level))
else:
    while (chose_level(level) == "unvalid"):
        print ("This isn't a level of the game!\nPlease try very easy, easy, medium or hard.\nNote that all the examples are in lowercase letters.\n\nPlease select a game difficulty by typing it in!\nPossible choices include very easy, easy, medium, and hard.")
        level = input()
    print ("You've chosen",level,"!\n")    
    print (chose_level(level))

print (play_game(chose_level(level), parts_in_blank))








'''
def awnser(input):
    if input == "very easy":
        return Awnser_very_easy 
    elif input == "easy":
        return Awnser_easy 
    elif input == "medium":
        return Awnser_medium 
    elif input == "hard":
        return Awnser_hard 

print (awnser(level))

def fill_blank(blank, parts_in_blank):
    for gap in parts_in_blank :
        if gap in blank:
            return gap
    return None

def right(replacement, user_input):
    for right in awnser(level):
        print (right)
        if user_input == right:
            return ("correct")
        else:
            return "wrong"


def play_game(level, parts_in_blank):  
    replaced = []
    level = level.split()
    for blank in level:
        replacement = fill_blank(blank, parts_in_blank)
        if replacement != None:
            user_input = input("Take you guess on: " + replacement + " ")
            blank = blank.replace(replacement, user_input)
            replaced.append(blank)
        else:
            replaced.append(blank)
    replaced = " ".join(replaced)
    return replaced
    
print (play_game(chose_level(level), parts_in_blank))
'''

