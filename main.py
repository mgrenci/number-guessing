import random 

#User inputs a number 
def user_input():
    set_number = int(input("Enter how many numbers you want the computer to guess through: "))
    user_number = int(input("Enter a number for the program to guess between 1 and " + str(set_number) + ": "))
    return set_number, user_number
#Program determines the number in a structured way. 

def get_list(number):
    possible_guesses = []
    for x in range(number):
        possible_guesses.append(x+1)
    return possible_guesses


def main():
    set_number, user_number = user_input()
    possible_guesses = get_list(set_number)
    guess = random.randint(1, set_number)
    count = 0
    valid = False
    while valid == False:
        count += 1
        print("The program guesses " + str(guess) + ".")
        if guess == user_number:
            print("The program guessed your number in " + str(count) + " tries. \nYour number was... " + str(user_number))
            valid = True 
        else:     
            index = possible_guesses.index(guess)
            if guess > user_number:
                possible_guesses = possible_guesses[:index]
                guess = random.choice(possible_guesses)   
            else:
                possible_guesses = possible_guesses[index+1:]
                guess = random.choice(possible_guesses)
    
main()

