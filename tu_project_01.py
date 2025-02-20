def greeting():
    print("hello we would like to learn a few things about you.")
    print("answer the questions as follow.")

    name = input("what is your name?")
    college = input(f"{name}, what college are you attending?")
    high_school = input(f"{name}, what high school did you attending?")
    institution = input(f"{name} which institution is more fun?")
    food = input(f"{name} what is your favorite food.")

    print("\nit was nice to speak with you,"+ name +".")
    print(f"you are currently attending {college}.")
    print(f" i learned that your high school name is {high_school}.")
    print(f"you think {institution} is a better institution.")
    print(f"{food} is your favorite food.")
    print("it was fun getting to know a little about you.")
    print("lets do this again")

greeting()
