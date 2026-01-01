while True:
    print("=============================================================")
    print("-----  DATA ANALYSIS & VISUALIZATION PROGRAM -----")
    print("=============================================================")
    print(" * Please select an Option ")
    print("1. Load Dataset:")
    print("2. Explore Data:")
    print("3. Perform DataFrame Operations:")
    print("4. Handle Missing Data:")
    print("5. Generate Descriptive Statistics:")
    print("6. Data Visualization:")
    print("7. Save Visualizations:")
    print("8. Exit")
    choice=int(input("Select an option from (1-8): "))
    if choice==1:
        import pandas as pd
        file_path = input("Enter the path to the dataset (CSV format): ")
        try:
            df = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading dataset: {e}")
    elif choice==2:
        try:
            print("First 5 rows of the dataset:")
            print(df.head())
            print("\nDataset Info:")
            print(df.info())
            print("\nDataset Description:")
            print(df.describe())
        except NameError:
            print("Please load a dataset first.")
    elif choice==3:
        try:
            print("Columns in the dataset:")
            print(df.columns)
            col_to_select = input("Enter column names to select (comma-separated): ").split(',')
            selected_df = df[col_to_select]
            print("Selected DataFrame:")
            print(selected_df.head())
        except NameError:
            print("Please load a dataset first.")
        except KeyError:
            print("One or more column names are invalid.")
    elif choice==4:
        try:
            print("Handling missing data...")
            df.fillna(method='ffill', inplace=True)
            print("Missing data handled using forward fill.")
        except NameError:
            print("Please load a dataset first.")
    elif choice==5:
        try:
            print("Descriptive Statistics:")
            print(df.describe())
        except NameError:
            print("Please load a dataset first.")
    elif choice==6: 
        try:
            import matplotlib.pyplot as plt
            col_to_plot = input("Enter the column name to visualize: ")
            plt.hist(df[col_to_plot].dropna(), bins=30, edgecolor='black')
            plt.title(f'Histogram of {col_to_plot}')
            plt.xlabel(col_to_plot)
            plt.ylabel('Frequency')
            plt.show()
        except NameError:
            print("Please load a dataset first.")
        except KeyError:
            print("Invalid column name.")
    elif choice==7:
        try:
            save_path = input("Enter the file path to save the visualization (e.g., histogram.png): ")
            plt.savefig(save_path)
            print(f"Visualization saved to {save_path}")
        except Exception as e:
            print(f"Error saving visualization: {e}")
    elif choice==8:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-8).")    
        
