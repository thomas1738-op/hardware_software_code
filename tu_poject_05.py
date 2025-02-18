def main():
    print("wlecome to the number adding programs! This program adds whole numbers until you say exit.")

    while True :
        try:
            num1 =int(input("enter the first whole number"))
            num2 =int(input("enter the second whole number"))
            result = num1 + num2
            print(f"the sum of {num1} and {num2} is {result}.")
        except ValueError:
            print( "invalid input. please enter a vaild whole number.")
            continue

        exit_choice = input("would you like to keep going? (yes to continue, no to exit)")
        if exit_choice== "no" :
            print("thank you for using the adding program. goodbye!!")
            break
if __name__ == "__main__":
    main()
