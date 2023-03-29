name = input("Enter your name?")
Wijziging pushen naar de server
name = input("What is your name?")
print(f"Your name is {len(name)} characters long")

Sentence
article = input("Enter an article?")
noun = input("Enter a noun?")
verb = input("Enter a verb?")
print(f"{article} {noun} {verb}")

score = int(input("enter your score: "))
if score < 60:
    print("Fail!")
else:
    print("Pass!!!!")


income = int(input("How much do you earn? "))
if income < 20000:
    print("You don't have to pay taxes!")
elif income < 50000:
    print("You have to pay 30%")
else:
    print("You have to pay 60%")
