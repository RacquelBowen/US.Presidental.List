import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Presidents                 |
# Racquel Miller                        |
# Last Modified: October 3rd, 2021      |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

#creates the class 'President'
class President:
#defines the parameters for '__init__' to correspond to the 'pres_listing' sequence
    def __init__(self, first, last, number, year, term, occupation):
        self.first = first
        self.last = last
        self.number = number
        self.year = year
        self.term = term
        self.occupation = occupation
#initializes 'self.full_name' to append the 'first' parameter and 'last' parameter
#to be the Presidents' full name
        self.full_name = str(first) + " " + str(last)
#defines the 'get_name' method
    def get_name(self):
        return self.full_name
#defines the 'get_number' method
    def get_number(self):
        return self.number
#defines the 'get_occupation' method
    def get_occupation(self):
        return self.occupation
#defines the 'get_time_in_office' method       
    def get_time_in_office(self):
        return self.term
#defines the '__str__' method to be set to return the string
    def __str__(self):        
        return("No. " + str(self.number) + " (" + str(self.year) + ") " + str(self.full_name))


# ---------------------------------------
def print_menu():
    print ("""
1. Print all presidents
2. Print president by name
3. Print president by number
4. Count presidents with occupation
5. Print average term length
6. Quit
    """)
# ---------------------------------------


def print_all_presidents(pres_listing):
#prints each president from the list 'pres_listing'
    for president in pres_listing:
        print(president)

def print_by_name(pres_listing, name):
#while the length of the input 'name' is less than 3 characters, the code displays
#the input "Enter more than two characters:" to keep popping up
    while len(name) < 3:
        name = input("Enter more than two characters: ")
    else:
        print("\n")
        true = "no"
#checks to see if the string of the president has the inputted 'name' in each
#pres_lising, and makes sure that the strings are the same, making 'partly' lower
#case
        for president in pres_listing:
            partly = president.get_name()
            lower_case = partly.lower()
            in_name = lower_case.find(name)
#since the 'lower_case.find()' returns -1 if the item is not found, but returns the
#length of the 'president.get_name' so it must be greater than 0, if so, it prints the
#'president' and makes 'true' to be the string "yes"
            if in_name > 0:
                print(president)
                true = "yes"
#if 'true' equivalent to the string "no", it prints the string "No president's name
#contains 'name' "
        if true == "no":
            print("No president's name contains '" + name +"'" )

def print_by_number(pres_listing, number):
#if the 'number' is less than 47 and the 'presidency' is equal to the number typed in,
#it returns the 'president' string
    if number < 47:
        for president in pres_listing:
            presidency = president.get_number()
            if presidency == number:
                print("\n" + str(president))
#else if the 'number' is the same as 'number', it prints the string "President number
#must be between 1 and 46"
    elif number == number:
        print("\nPresident number must be between 1 and 46")

def count_by_occupation(pres_listing, occupation):
    count = 0
    names = ""
    doub = []
#goes through all the items in the list 'pres_listing'
    for president in pres_listing:
#gets the function 'get_occupation' from the class 'President'and assigns that string
#to then be 'hobby'
        hobby = president.get_occupation()
        for i in range(0, len(hobby)):
#checks to see if the 'hobby' list index of 'i' matches the occupation string
            if hobby[i] == occupation:
#if there is noting in the list 'doub', it adds one to 'count'
                if len(doub) == 0:
                    count = count + 1
#checks to see if 'count' is equivalant to 1, if so then it makes the 'name' become
#the presidents name and appends the name to 'doub'
                    if count == 1:
                        names = president.get_name()
                        doub.append(president.get_name())
                else:
                    for i in range(0, len(doub)):
#checks to see if the president is already in the list 'doub'
                        if president.get_name() not in doub:
#adds 1 to 'count', and assigns 'names' to add the president name to 'names', then,
#it appends the presidents name to the list 'doub'
                            count = count + 1
                            names = names + ", " + president.get_name()
                            doub.append(president.get_name())
#on a new line it prints the sting type of 'count' and 'occupation', the string
#presidents: and 'names'        
    print("\n"  + str(count) + " " + occupation + " presidents: " + names)
    
def average_term_length(pres_listing):
    term = 0
    for president in pres_listing:
#gets the float type from the class 'President' and the return value from the function
#'get_time_in_office' and adds the previous 'term' number to get the value 'term'
        term = float(president.get_time_in_office()) + term
#prints the value of 'term' divided by the length of the 'pres_listing', rounding it
#to the nearest tenth
    print("Average term length, about " + str(round(term/len(pres_listing), 1)) + " years")
                
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pres_listing(filename):
    pres_listing = []
    file = open(filename, "r")
    
    for president in file:
        presilist = president.strip().split(",")
        number = int(presilist[0])               # number
        last = presilist[1]                      # last name
        first = presilist[2]                     # first name
        start_in = int(presilist[3])             # first year in office
        term = float(presilist[4])               # years in office
        occupations = []
        for position in range(5, len(presilist)):
            occupations += [presilist[position]] # occupation
        pres_listing += [President(first, last, number, start_in, term, occupations)]

    file.close()
    return pres_listing

# ---------------------------------------

def get_choice(low, high, message):
    
    legal_choice = False
    answer = input(message)
    while answer == "":
        answer = input(message)
    for char in answer:
        if char not in string.digits:
            print('ERROR: ', answer, "is not a number")
            return 0
    answer = int(answer)
    if (low > answer) or (answer > high):
        print('ERROR: ', answer, "is not a choice")
    return answer

# ---------------------------------------

def main():
    pres_listing = create_pres_listing("pres_listing.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_all_presidents(pres_listing)
        elif choice == 2:
            name = input("Enter a president name: ").lower()
            print_by_name(pres_listing, name)
        elif choice == 3:
            number = get_choice(1, 46, "Enter a president number: ")
            print_by_number(pres_listing, number)
        elif choice == 4:
            occupation = input("Enter a president occupation: ").lower()
            count_by_occupation(pres_listing, occupation)
        elif choice == 5:
            average_term_length(pres_listing)
        elif choice == 6:
            print("Thank you.  Goodbye!")

# ---------------------------------------

main()
