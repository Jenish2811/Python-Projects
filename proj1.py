while True:
    print("=============================================================")
    print("-----  WELCOME TO THE INTERACTIVE PERSONAL DATA COLLECTOR 1 -----")
    print("=============================================================")
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    email=input("Enter your email address: ")
    phone=input("Enter your phone number: ")
    address=input("Enter your address: ")
    print("\nPlease confirm your details:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Address: {address}")
    confirm=input("Are these details correct? (yes/no): ").strip().lower()
    if confirm=="yes":
        print("Thank you! Your details have been recorded.")
        break
    else:
        print("Let's re-enter your details.\n")
        

