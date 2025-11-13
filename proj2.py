while True:
        print("=============================================================")
        print("-----   WELCOME TO THE PATTERN GENERATOR AND NUMBER ANALYZER.  -----") 
        print("=============================================================")
        print("1. Pattern Generator.")
        print("2. Number Analyzer.")
        print("3. Exit")
        choice=int(input("enter your choice from (1 to 3):"))

        if (choice==1):
                rows=int(input("enter numbers of rows:"))
                print("\ntriangle pattern:\n")
                for i in range(1, rows +1):
                        for j in range(i):
                                print("*",end=" ")
                        print()

        elif choice==2:
                start=int(input("enter a starting range:"))
                end=int(input("enter a ending range:"))
                total=0
                for i in range(start,end +1):
                        j="even" if i%2==0 else "odd"
                        print(f"number {i} is {j}")
                        total+=i
                print(f"sum of all intergers from {start} to {end} is: {total}")

        elif choice==3:
                print("Thank you for using PATTERN GENRATOR AND NUMBER ANALYZER😇.")
                print("BYE👋🏻")
                break
        else:
                print("invalid choice.")