while True:
    print("==========================================================================")
    print("             Welcome to Personal Journal Manager             ")
    print("==========================================================================")
    print(" * Please select an Option ")
    print("1. Add a New Entry:")
    print("2. View All Entries:")
    print("3. Search for an Entries:")
    print("4. Delete an Entry:")
    print("5. Exit")

    choice=int(input("Select an opyion from (1-5): "))
    if choice==1:
        file=open("journal.txt","a")
        entry=input("Write your journal entry:\n")
        file.write(entry+"\n")
        file.close()
        print("Entry added successfully!")
    elif choice==2:
        file=open("journal.txt","r")
        print("Your Journal Entries:")
        print(file.read())
        file.close()
    elif choice==3:
        keyword=input("Enter a keyword to search for: ")
        file=open("journal.txt","r")
        entries=file.readlines()
        found=False
        print("Search Results:")
        for entry in entries:
            if keyword.lower() in entry.lower():
                print(entry.strip())
                found=True
        if not found:
            print("No entries found with the given keyword.")
        file.close()
    elif choice==4:
        keyword=input("Enter a keyword to delete entries: ")
        file=open("journal.txt","r")
        entries=file.readlines()
        file.close()
        file=open("journal.txt","w")
        deleted=False
        for entry in entries:
            if keyword.lower() not in entry.lower():
                file.write(entry)
            else:
                deleted=True
        file.close()
        if deleted:
            print("Entries containing the keyword have been deleted.")
        else:
            print("No entries found with the given keyword.")
    elif choice==5:
        print("Exiting the Journal Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")