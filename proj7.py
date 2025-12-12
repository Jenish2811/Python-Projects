while True:  
    print("=================================================")
    print("         Welcome to the Multi-Utikity Toolkit       ")
    print("=================================================")
    print("Choose an option to proceed:")
    print("1. Date and Time Operations:")
    print("2. Mathematical Calculations:")
    print("3. Random Data Generation:")
    print("4. Generate Unique Identifier:")
    print("5. File Operations:")
    print("6. Explore Module Attributes:")
    print("7. Exit")
    choice=int(input("Select an option from (1-7): "))

    if choice==1:
        print("Date and Time Operations Selected.")
        print("1. Display Current Date and Time:")
        print("2. Calculate Difference Between Two Dates or time:")
        print("3. Custom Date Formatting:")
        print("4. Stopwatch:")
        print("5. Countdown Timer:")
        print("6. Return to Main Menu:")
        sub_choice=int(input("Select an option from (1-6): "))
        if sub_choice==1:
            from datetime import datetime
            now=datetime.now()
            print("Current Date and Time:", now)
        elif sub_choice==2:
            from datetime import datetime
            date_format="%Y-%m-%d"
            date1_str=input("Enter the first date (YYYY-MM-DD): ")
            date2_str=input("Enter the second date (YYYY-MM-DD): ")
            date1=datetime.strptime(date1_str, date_format)
            date2=datetime.strptime(date2_str, date_format)
            difference=abs((date2-date1).days)
            print(f"The difference between {date1_str} and {date2_str} is {difference} days.")
        elif sub_choice==3:
            from datetime import datetime
            now=datetime.now()
            custom_format=input("Enter the desired date format (e.g., %Y-%m-%d %H:%M:%S): ")
            formatted_date=now.strftime(custom_format)
            print("Formatted Date and Time:", formatted_date)
        elif sub_choice==4:
            import time
            input("Press Enter to start the stopwatch...")
            start=time.time()
            input("Press Enter to stop the stopwatch...")
            end=time.time()
            print(f"Elapsed Time:", round(end-start, 2), "seconds")
        elif sub_choice==5:
            import time
            seconds=int(input("enter the number of seconds for the countdown:"))
            for i in range(seconds, 0, -1):
                print(i, "seconds remaining")
                time.sleep(1)
            print("Countdown finished!")
        elif sub_choice==6:
            print("Returning to Main Menu.")
        else:
            print("Invalid choice. Please select a valid option (1-6).")

    elif choice==2:
        print("Mathematical Calculations Selected.")
        print("1. Arithmetic Operations:")
        print("2. Trigonometry Operations:")
        print("3. Logarithmic Calculations:")
        print("4. Factorial Calculation:")
        print("5. Compound Interest Calculation:")
        print("6. Geometric shapes Area:")
        print("7. Return to Main Menu:")
        sub_choice=int(input("Select an option from (1-7): "))
        if sub_choice==1:
            num1=float(input("Enter the first number: "))
            num2=float(input("Enter the second number: "))
            print("Addition:", num1 + num2)
            print("Subtraction:", num1 - num2)
            print("Multiplication:", num1 * num2)
            print("Division:", num1 / num2)
            print("Modulus:", num1 % num2)
            print("Power:", num1 ** num2)
            print("Floor Division:", num1 // num2)
        elif sub_choice==2:
            import math
            angle=float(input("Enter the angle in degrees: "))
            radians=math.radians(angle)
            print("Sine:", math.sin(radians))
            print("Cosine:", math.cos(radians))
            print("Tangent:", math.tan(radians))
        elif sub_choice==3: 
            import math
            value=float(input("enter a positive number to calculate its logarithm:"))
            print("Natural Logarithm (base e):", math.log(value))
            print("Logarithm (base 10):", math.log10(value))
        elif sub_choice==4:
            import math
            num=int(input("enter a number:"))
            result=math.factorial(num)
            print(f"The factorial of {num} is {result}.")
        elif sub_choice==5:
            principal=float(input("enter the amount:"))
            rate=float(input("enter the rate of interest(%):"))
            time=float(input("enter the time in years:"))
            amount= principal *(1 + rate/100) ** time
            print(f"The compound interest after {time} years is: {amount - principal}")
        elif sub_choice==6: 
            import math
            print("1. Area of circle:")
            print("2. Area of rectangle:")
            print("3. Area of triangle:")
            shape_choice=int(input("Select a shape (1-3): "))
            if shape_choice==1:
                radius=float(input("Enter the radius of the circle: "))
                area=math.pi * radius ** 2
                print(f"The area of the circle is: {area}")
            elif shape_choice==2:
                l=float(input("Enter the length of the rectangle: "))
                b=float(input("Enter the breadth of the rectangle: "))
                area=l * b
                print(f"The area of the rectangle is: {area}")
            elif shape_choice==3:
                b=float(input("Enter the base of the triangle: "))
                h=float(input("Enter the height of the triangle: "))
                area=0.5 * b * h
                print(f"The area of the triangle is: {area}")
            else:
                print("Invalid shape choice.")
        elif sub_choice==7:
            print("Returning to Main Menu.")
        else:
            print("Invalid choice. Please select a valid option (1-7).")
    elif choice==3:
        print("Random Data Generation Selected.")
        import random
        print("1. Generate Random Number:")
        print("2. Generate Random List:")
        print("3. Generate Random Password:")
        print("4. Generate Random Dataset:")
        print("5. Generate Random OTP:")
        print("6. Generate Rock-Paper-Scissors Game simulation::")
        print("7. Generate Dice Roll Game simulations:")
        print("8. Return to Main Menu:")
        sub_choice=int(input("Select an option from (1-8): "))
        if sub_choice==1:
            import random
            print("Random Number between 1 and 100:", random.randint(1, 100))
            print("Random Float:", random.random())
            print("Random Float (1-20):", random.uniform(1, 20))
        elif sub_choice==2:
            import random
            list_size=int(input("Enter the size of the list: "))
            random_list=[random.randint(1, 100) for _ in range(list_size)]
            print("Random List:", random_list)
        elif sub_choice==3:
            import random
            import string
            length=int(input("Enter the desired password length: "))
            characters=string.ascii_letters + string.digits + string.punctuation
            password=''.join(random.choice(characters) for i in range(length))
            print("Generated Password:", password)
        elif sub_choice==4:
            import random
            dataset_size=int(input("Enter the size of the dataset: "))
            sample= random.sample(range(1, 100), dataset_size)
            print("Random Dataset:", sample)
        elif sub_choice==5:
            import random
            otp= random.randint(100000, 999999)
            print("Generated OTP:", otp)
        elif sub_choice==6:
            import random
            choices = ['Rock', 'Paper', 'Scissors']
            user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")
            if user_choice == computer_choice:
                print("It's a tie!")
            elif user_choice == 'Rock' and computer_choice == 'Scissors' or \
                 user_choice == 'Paper' and computer_choice == 'Rock' or \
                 user_choice == 'Scissors' and computer_choice == 'Paper':
                print("You win!")
            else:
                print("Computer wins!")
        elif sub_choice==7:
            import random
            user_roll = random.randint(1, 6)
            computer_roll = random.randint(1, 6)
            print(f"You rolled: {user_roll}")
            print(f"Computer rolled: {computer_roll}")
            if user_roll > computer_roll:
                print("You win!")
            elif user_roll < computer_roll:
                print("Computer wins!")
            else:
                print("It's a tie!")
        elif sub_choice==8:
            print("Returning to Main Menu.")
        else:
            print("Invalid choice. Please select a valid option (1-8).")
    elif choice==4:
        print("Generate Unique Identifier Selected.")
        import uuid
        unique_id= uuid.uuid4()
        print("Generated Unique Identifier (UUID4):", unique_id)
    elif choice==5:
        print("File Operations Selected:")
        print("1. Read File:")
        print("2. Write File:")
        print("3. Append to File:")
        print("4. Delete File:")
        print("5. Return to Main Menu:")
        sub_choice=int(input("Select an option from (1-5): "))
        if sub_choice==1:
            file=input("Enter the file name to read: ")
            try:
                with open(file, 'r') as f:
                    content=f.read()
                    print("File Content:\n", content)
            except FileNotFoundError:
                print("File not found.")
        elif sub_choice==2:
            file=input("Enter the file name to write: ")
            content=input("Enter the content to write to the file: ")
            with open(file, 'w') as f:
                f.write(content)
            print("Content written to file.")
        elif sub_choice==3:
            file=input("Enter the file name to append: ")
            content=input("Enter the content to append to the file: ")
            with open(file, 'a') as f:
                f.write(content)
            print("Content appended to file.")
        elif sub_choice==4:
            import os
            file=input("Enter the file name to delete: ")
            try:
                os.remove(file)
                print("File deleted successfully.")
            except FileNotFoundError:
                print("File not found.")
        elif sub_choice==5:
            print("Returning to Main Menu.")
        else:
            print("Invalid choice. Please select a valid option (1-5).")
    elif choice==6:
        print("Explore Module Attributes Selected.")
        module_name=input("Enter the module name to explore (e.g., math, datetime): ")
        try:
            module=__import__(module_name)
            attributes=dir(module)
            print(f"Attributes and Methods in module '{module_name}':")
            for attr in attributes:
                print(attr)
        except ImportError:
            print("Module not found.")
    elif choice==7:
        print("Exiting the Multi-Utility Toolkit. Goodbye!")
        break   
           