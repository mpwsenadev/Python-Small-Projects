from colorama import Fore, Style

def calculate_dog_age(dog_age):
    human_age = 0
    
    if dog_age <= 2:
        human_age = dog_age * 10.5
    else:
        human_age = 21 + (dog_age - 2) * 4
        
    return human_age

def main():
    print("")
    print(Fore.GREEN + "Dog Age Calculator\n" + Style.RESET_ALL)
    
    dog_age = float(input(Fore.YELLOW + "Enter the dog's age in years: " + Style.RESET_ALL))
    
    human_age = calculate_dog_age(dog_age)
    
    print(Fore.CYAN + "The dog's age in human years is:", human_age, Style.RESET_ALL)

if __name__ == "__main__":
    main()
