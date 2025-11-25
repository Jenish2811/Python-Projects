while True:

    print("=========================================================")
    print("WELCOME TO THE DATA ANALYZER AND TRANSFORMER PROGRAM")
    print("=========================================================")
    print("MAIN MENU:")
    print("1. INPUT DATA:")
    print("2. BUILT-IN FUNCTION:")
    print("3. RECURSION:")
    print("4. LAMABDA FUNCTION:")
    print("5. SORT DATA:")
    print("6. DISPLAY DATASET STATISTICS:")
    print("7. EXIT PROGRAM")
    ch=(int(input("enter your choice from (1-7):")))


    if(ch==1):
        print("A 1D Array")
        print("B 2D Array")
        array_type=input("enter your choice from(A to B):")
        if array_type=="A":
            choice=input("enter 'M' for manual input or 'S' for sample data:")

            if choice=='M':
                j=int(input("enter number of elements:"))
                arr=[input(f"enter element {i+1}:") for i in range (j)]
            else:
                arr=[10,20,30,40]

            print("\n your 1D array:", arr) 
            print("Data has been stored compeletly!")

        elif array_type=="B":
            choice=input("enter 'M' for manual input or 'S' for sample data:")

            if choice=='M':
                rows=int(input("enter numbers of rows:"))
                columns=int(input("enter numbers of columns:"))
                arr=[ ]
                for i in range(rows):
                    print("enter row", i+1, "values:")
                    row=[ ]
                    for j in range(columns):
                        value=int(input(f"enter value for [{i}][{j}]:"))
                        row.append(value)
                    arr.append(row)
                    
                print("\nyour 2D array:")
                for row in arr:
                    print(row)
            else:
                arr=[
                    [1,2,3],
                    [4,5,6],
                    [7,8,9]
                ]
                print("\n your 2D array:")
                for rows in arr:
                    print(rows)
        else:
            print("Data has been stored completly!")
            print("Invalid choice!")



    if(ch==2):
        print("A 1D Array")
        print("B 2D Array")
        array_type=input("enter your choice from(A to B):")
        if array_type=="A":
            choice=input("enter 'M' for manual input or 'S' for sample data:")

            if choice=='M':
                j=int(input("enter number of elements:"))
                arr=[float(input(f"enter element {i+1}:")) for i in range (j)]
            else:
                arr=[10,20,30,40]
                print("using sample data:", arr)

            print("\n your 1D array:", arr) 
            print("n\---  BASIC STATISTICS  ---")
            print("total elements:", len(arr))
            print("sum of all elements:", sum(arr))
            print("max value:", max(arr))
            print("min value:", min(arr))
            print("Average value:", sum(arr)/ len(arr))

        elif array_type=="B":
            choice=input("enter 'M' for manual input or 'S' for sample data:")

            if choice=='M':
                rows=int(input("enter numbers of rows:"))
                columns=int(input("enter numbers of columns:"))
                arr=[ ]
                for i in range(rows):
                    print("enter row", i+1, "values:")
                    row=[ ]
                    for j in range(columns):
                        value=int(input(f"enter value for [{i}][{j}]:"))
                        row.append(value)
                    arr.append(row)
                    
                print("\nyour 2D array:")
                for row in arr:
                    print(row)

            else:
                arr=[
                    [1,2,3],
                    [4,5,6],
                    [7,8,9]
                ]
                print("\n your 2D array:")
                for rows in arr:
                    print(rows)

            flat=[num for sublist in arr for num in sublist]
            print("\n--- BASIC STATISTICS FOR 2D ARRAY ---")
            print("total elements:", len(flat))
            print("sum of all elements:", sum(flat))
            print("max value:", max(flat))
            print("min value:", min(flat))
            print("Average value:", sum(flat)/ len(flat))
        else:

            print("Invalid choice!")


    if(ch==3):
        print("data analyzer program")
        print("1. analyze array data")
        print("2. recursive factorial")
        print("3. recursive fibonacci")
        choice=input("chosse an option from (1,2,3):")
        if choice=="1":
            arr=list(map(int, input("enter numbers:").split()))
            print("your array:", arr)
            print("--- BASIC STATISTICS ---")
            print("total elements:", len(arr))
            print("sum of all elements:", sum(arr))
            print("max value:", max(arr))
            print("min value:", min(arr))
            print("Average value:", sum(arr)/ len(arr))
        elif choice=="2":
            def factorial(n):
                if n==0 or n==1:
                    return 1
                else:
                    return n * factorial(n-1)
            num=int(input("enter a number to find factorial:"))
            result=factorial(num)
            print(f"Factorial of {num} is {result}")
        elif choice=="3":
            def fibonacci(n):
                if n<=0:
                    return 0
                elif n==1:
                    return 1
                else:
                    return fibonacci(n-1) + fibonacci(n-2)
            terms=int(input("enter number of terms for fibonacci series:"))
            print("Fibonacci series:")
            for i in range(terms):
                print(fibonacci(i), end=" ")    
    if (ch==4):
        data=[10,20,30,40,50,60,70]
        print("original data:",data)
        
        doubled=list(map(lambda x: x * 2, data))
        print("doubled values:", doubled)

        threshold=int(input("enter threshold value:"))
        above=list(filter(lambda x: x> threshold, data))
        below=list(filter(lambda x:x< threshold, data))

        print("Values above threshold:", above)
        print("Values below threshold:", below)

    if(ch==5):
        print("Chosse sorting option:")
        print("1. Ascending")
        print("2. Descending")
        choice=input("enter your choice from (1 or 2):")
        numbers=[1,3,5,2,6,7,4]
        print("orginal numbers", numbers)

        if choice=="1":
         numbers=[1,3,5,2,6,7,4]
         numbers.sort()
         print("Ascending order:", numbers)

        elif choice=="2":
            numbers=[1,3,5,2,6,7,4]
            numbers.sort(reverse=True)
            print("Descending order:", numbers)

    if(ch==6):
        print("Data Set Statistics Program")
        numbers=input("enter numbers separated by spaces:").split()
        numbers=[float(num) for num in numbers]
        print("Data Set:", numbers)
        print("Total Numbers:", len(numbers))
        print("Sum:", sum(numbers))
        print("Maximum:", max(numbers))
        print("Minimum:", min(numbers))
        print("Average:", sum(numbers)/ len(numbers))



    if(ch==7):
        print("Exiting the program. Goodbye!")
        break
