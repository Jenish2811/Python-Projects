while True:   
    print("==================================================================")
    print("             WELCOME TO THE NUMPY ANALYZER!                       ")
    print("==================================================================")
    print("CHOOSE AN OPTION:")
    print("1. Create a NumPy Array.")
    print("2. Perform Mathematical Operations.")
    print("3. Combine or split arrays.")
    print("4. Search, sort or filter arrays.")
    print("5. Compute Aggregate Statistics.")
    print("6. Exit.")
    choice = int(input("Enter your choice (1-6): "))
    if choice==1:
        import numpy as np
        array_type = input("Enter '1' for 1D array, '2' for 2D array: ")
        if array_type == '1':
            elements = list(map(int, input("Enter elements of 1D array separated by spaces: ").split()))
            arr = np.array(elements)
            print("Created 1D array:", arr)
        elif array_type == '2':
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            print("Enter the elements row-wise:")
            elements = []
            for i in range(rows):
                row_elements = list(map(int, input().split()))
                elements.append(row_elements)
            arr = np.array(elements)
            print("Created 2D array:\n", arr)
        else:
            print("Invalid input. Please try again.")
    elif choice==2:
        import numpy as np
        arr = np.array(list(map(int, input("Enter elements of the array separated by spaces: ").split())))
        print("Array:", arr)
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        operation = int(input("Enter your choice (1-4): "))
        scalar = int(input("Enter a scalar value: "))
        if operation == 1:
            result = arr + scalar
            print("Result after addition:", result)
        elif operation == 2:
            result = arr - scalar
            print("Result after subtraction:", result)
        elif operation == 3:
            result = arr * scalar
            print("Result after multiplication:", result)
        elif operation == 4:
            result = arr / scalar
            print("Result after division:", result)
        else:
            print("Invalid operation choice.")
    elif choice==3:
        import numpy as np
        arr1 = np.array(list(map(int, input("Enter elements of the first array separated by spaces: ").split())))
        arr2 = np.array(list(map(int, input("Enter elements of the second array separated by spaces: ").split())))
        print("Select operation:")
        print("1. Combine (Concatenate)")
        print("2. Split")
        operation = int(input("Enter your choice (1-2): "))
        if operation == 1:
            combined = np.concatenate((arr1, arr2))
            print("Combined array:", combined)
        elif operation == 2:
            num_splits = int(input("Enter number of splits: "))
            splits = np.array_split(arr1, num_splits)
            print("Split arrays:")
            for i, split in enumerate(splits):
                print(f"Part {i+1}:", split)
        else:
            print("Invalid operation choice.")
    elif choice==4:
        import numpy as np
        arr = np.array(list(map(int, input("Enter elements of the array separated by spaces: ").split())))
        print("Select operation:")
        print("1. Search for an element")
        print("2. Sort the array")
        print("3. Filter elements greater than a value")
        operation = int(input("Enter your choice (1-3): "))
        if operation == 1:
            element = int(input("Enter the element to search for: "))
            indices = np.where(arr == element)[0]
            if indices.size > 0:
                print(f"Element {element} found at indices:", indices)
            else:
                print(f"Element {element} not found in the array.")
        elif operation == 2:
            sorted_arr = np.sort(arr)
            print("Sorted array:", sorted_arr)
        elif operation == 3:
            threshold = int(input("Enter the threshold value: "))
            filtered = arr[arr > threshold]
            print(f"Elements greater than {threshold}:", filtered)
        else:
            print("Invalid operation choice.")
    elif choice==5:
        import numpy as np
        arr = np.array(list(map(int, input("Enter elements of the array separated by spaces: ").split())))
        print("Select statistic to compute:")
        print("1. Mean")
        print("2. Median")
        print("3. Standard Deviation")
        print("4. Sum")
        operation = int(input("Enter your choice (1-4): "))
        if operation == 1:
            mean = np.mean(arr)
            print("Mean:", mean)
        elif operation == 2:
            median = np.median(arr)
            print("Median:", median)
        elif operation == 3:
            std_dev = np.std(arr)
            print("Standard Deviation:", std_dev)
        elif operation == 4:
            total_sum = np.sum(arr)
            print("Sum:", total_sum)
        else:
            print("Invalid operation choice.")
    elif choice==6:
        print("Exiting the NumPy Analyzer. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).")
