from colorama import init, Fore, Style
init(autoreset=True)
print("\n" + "="*40)
print(Fore.CYAN + "welcome to the Inner Peace Quiz!")
print("\n" + "="*40)
print("Answer the following questions to find out how peaceful you are.")
score = 0
print(Style.BRIGHT + Fore.BLUE + """1. how do you react when plans suddenly change?
    a) I get frustrated and upset
    b) I try to adapt and find a new solution
    c) I accept it and move on
    d) I see it as an opportunity for something new""")
answer1 = input("your answer (a/b/c/d):  ")
if answer1 == 'a':
    score += 0
elif answer1 == 'b':
    score += 1
elif answer1 == 'c':
    score += 2
elif answer1 == 'd':
    score += 3
else:
    print("Invalid answer. Please enter a, b, c, or d.")
print("""2. how do you handle stress?
    a) I feel overwhelmed and anxious
    b) I try to manage it with relaxation techniques
    c) I find healthy outlets like exercise or hobbies
    d) I embrace it as a part of life""")
print("choose a, b, c, or d")
answer2 = input("your answer (a/b/c/d):  ")
if answer2 == 'a':
    score += 0
elif answer2 == 'b':
    score += 1
elif answer2 == 'c':
    score += 2
elif answer2 == 'd':
    score += 3
else:
    print("Invalid answer. Please enter a, b, c, or d.")
print("""3. how do you feel about change?
    a) I resist it and prefer stability
    b) I accept it but find it challenging
    c) I see it as an opportunity for growth
    d) I actively seek it out""")
answer3 = input("your answer (a/b/c/d):  ")
if answer3 == 'a':
    score += 0
elif answer3 == 'b':
    score += 1
elif answer3 == 'c':
    score += 2
elif answer3 == 'd':
    score += 3
else:
    print("Invalid answer. Please enter a, b, c, or d.")
# Evaluate the final score and display the result
if score <= 2:
    print(Fore.RED + "You may need to work on finding more inner peace.")
elif score <= 5:
    print(Fore.YELLOW + "You have some peaceful qualities, but there's room for growth.")
elif score <= 7:
    print(Fore.GREEN + "You are quite peaceful and handle life well!")
else:
    print(Fore.CYAN + "You radiate inner peace! Keep it up!")
input("\Press Enter to exit the quiz.")
