import csv
import pandas as pd
import matplotlib.pyplot as plt


def viewData(data):
    userInput = ""
    while userInput != "5":
        print("\t\tSelect an option for viewing the data.")
        print("\t\t1. Display all data")
        print("\t\t2. Display specific rows (by index range)")
        print("\t\t3. Display specific columns (by names)")
        print("\t\t4. Filter rows")
        print("\t\t5. Go back")
        userInput = input("Enter a number option: ")
        if userInput == "5":
            break
        elif userInput == "1":
            print(data)
        elif userInput == "2":
            start = int(input("Enter the starting index: "))
            end = int(input("Enter the ending index: "))
            print(f"Displaying rows {start} - {end}")
            print(data.iloc[start:end])
        elif userInput == "3":
            columns = input("Enter the column names separated by commas: ").split(",")
            columns = [col.strip() for col in columns]
            print("Displaying columns selected:")
            print(data[columns])


def readFile():
    try:
        fileName = input("Enter file name (include the .csv extension): ")
        print()
        data = pd.read_csv(fileName)
        userInput = ""
        while userInput != "5":
            print("\tFile was found. How would you like to analyze the file?")
            print("\t1. View the data")
            print("\t2. Summarize the data")
            print("\t3. Filter the data")
            print("\t4. Create/view a graph")
            print("\t5. Go back")
            userInput = input("\tEnter a number option:")
            if userInput == "5":
                break
            elif userInput == "1":
                viewData(data)
            elif userInput == "2":
                print("Summarize the data")
            elif userInput == "3":
                print("Filter the data")
            elif userInput == "4":
                print("Create a graph")
            else:
                print("Option not found!")
    except OSError:
        print("Could not find csv file.")

def readOptionInput():
    print("Music Data Analyzer")
    print("This program can analyze and create graphs on music popularity data")
    userInput = ""
    while userInput.lower() != "q":
        print("Options: ")
        print("1. Analyze a new csv file: ")
        print("2. Access an existing graph")
        userInput = input("Enter a number option: ")
        if userInput.lower() == "q":
            break
        elif userInput == "1":
            readFile()
        else:
            print("Error: Not a valid option.")

def main():
    readOptionInput()

if __name__ == "__main__":
    main()