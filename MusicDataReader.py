import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#Displays options for how the user wants to view the data.
def viewData(data):
    userInput = ""
    print()
    while userInput != "5":
        print("Select an option for viewing the data.")
        print("1. Display all data")
        print("2. Display specific rows (by index range)")
        print("3. Display specific columns (by names)")
        print("4. Display specific title")
        print("5. Display specific artist")
        print("6. Go back")
        userInput = input("Enter a number option: ")
        if userInput == "6":
            break
        elif userInput == "1":
            #Displays all data in the data file
            print(data)
        elif userInput == "2":
            #Displays the data for a specific row range that the user specifies.
            start = int(input("Enter the starting index: "))
            end = int(input("Enter the ending index: "))
            print(f"Displaying rows {start} - {end}")
            print(data.iloc[start:end])
        elif userInput == "3":
            #Displays columns of the data that the user specifies.
            columns = input("Enter the column names separated by commas: ").split(",")
            columns = [col.strip() for col in columns]
            print("Displaying columns selected:")
            print(data[columns])
        elif userInput == "4":
            #Displays the data for a specific song title
            title = input("Enter the title you're searching for: ")
            title_data = data.loc[data['title'] == title]
            print(title_data)
        elif userInput == "5":
            #Displays the data for a specific performer name
            artist = input("Enter the artist you're searching for: ")
            artist_data = data.loc[data['performer'].str.contains(artist)]
            print(artist_data)

#Give options for filtering data based on input
def filterData(data):
    print()
    try:
        print("How would you like to filter the data: ")
        print("1. By chart week: ")
        print("2. By title: ")
        print("3. By performer: ")
        print("4. By peak position: ")
        print("5. By weeks on chart: ")
        print("6. By Top # Songs (ex: Top 10 songs)")
        print("7. Go back")
        userInput = input("Enter a number: ")
        #Sends the user back to the previous menu with the data unfiltered.
        if userInput == "7":
            readDataOption(data)
        elif userInput == "1":
            #Filters the data by chart weeks that the user specifies
            start = input("Enter the start week (YYYY-MM-DD): ")
            end = input("Enter the end week: (YYYY-MM-DD): ")
            newData = data[(data["chart_week"] >= start) & (data["chart_week"] <= end)]
        elif userInput == "2":
            #Filters the data by song title
            title = input("Enter the song title: ")
            newData = data[data["title"] == title]
        elif userInput == "3":
            #Filters the data by performer name
            performer = input("Enter the performer name: ")
            newData = data[data["performer"].str.contains(performer)]
        elif userInput == "4":
            #Filters the data by peak positions that the user specifies.
            start = int(input("Enter the highest position: "))
            end = int(input("Enter the lowest position: "))
            newData = data[(data["peak_pos"] >= start) & (data["peak_pos"] <= end)]
        elif userInput == "5":
            #Filters the data by the range of weeks in the chart that the user specifies.
            start = int(input("Enter the minimum amount of weeks in the chart: "))
            end = int(input("Enter the maximum amount of weeks in the chart: "))
            newData = data[(data["wks_on_chart"] >= start) & (data["wks_on_chart"] <= end)]
        elif userInput == "6":
            #Filters the data by Top # Songs (ex: Top 10 Songs)
            num = int(input("Enter a number: "))
            newData = data.head(num)
        else:
            print("Invalid input, returning to previous menu...")
            newData = data
        #Sends user to the previous menu with the new filtered data.
        readDataOption(newData)
    except:
        print("Encountered error, returning to previous menu...")
        print()



#Displays options for the type of graph users want to create.
#ycoord is only applied to graphs that utilize it.
def graphData(data):
    while True:
        #User enters the xcoord and ycoord for a potential plot
        print("Column option: chart_week, current_week, title, performer, last_week, peak_pos, wks_on_chart")
        xcoord = input("Enter the column you'd like to graph for your x-axis (must be numeric for box plot): ")
        ycoord = input("Enter the column you'd like to graph for your y-axis: ")
        if xcoord in data.columns and ycoord in data.columns:
            break
        else:
            print("Error Occurred! The x-coord or y-coord you inputted is incorrect")
    try:
        while True:
            print("Graph Options")
            print("1. Bar Plots")
            print("2. Histogram")
            print("3. Boxplot")
            print("4. Scatter")
            print("5. Pie")
            print("6. Line")
            graphType = input("Enter the number corresponding for a specific graph type: ")
            if graphType == "1":
                #Creates a bar plot using xcoord and ycoord
                plt.bar(data[xcoord], data[ycoord])
                plt.xlabel(xcoord)
                plt.ylabel(ycoord)
                title = input("Enter chart title: ")
                plt.title(title)
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.show()
                break
            elif graphType == "2":
                #Creates a histogram, ycoord is replaced by frequency label
                binNum = int(input("Enter the number of bins"))
                title = input("Enter chart title: ")
                plt.hist(data[xcoord], bins=binNum)
                plt.title(title)
                plt.xlabel(xcoord)
                plt.ylabel("Frequency")
                plt.show()
                break
            elif graphType == "3":
                #Creates a boxplot, ycoord is not used
                #xcoord must be a numeric value, otherwise error is thrown
                title = input("Enter chart title: ")
                plt.boxplot(data[xcoord], vert=False, patch_artist=True)
                plt.xlabel(xcoord)
                plt.title(title)
                plt.show()
                break
            elif graphType == "4":
                #Creates a scatter plot.
                title = input("Enter chart title: ")
                plt.scatter(data[xcoord], data[ycoord], alpha=0.7)
                plt.xlabel(xcoord)
                plt.ylabel(ycoord)
                plt.title(title)
                plt.show()
                break
            elif graphType == "5":
                #Creates a pie chart.
                plt.pie(data[xcoord], labels=data[ycoord], autopct='%1.1f%%', startangle=90)
                titleInput = input("Enter chart title: ")
                plt.title(titleInput)
                plt.show()
                break
            elif graphType == "6":
                #Creates a line chart
                titleInput = input("Enter chart title: ")
                plt.plot(data[xcoord], data[ycoord])
                plt.xlabel(xcoord)
                plt.ylabel(ycoord)
                plt.title(titleInput)
                plt.grid(True)
                plt.show()
                break
            else:
                print("Error Occured! Type a valid entry.")
        userInput = input("Save plot? (Y/N): ")
        #Saves chart creates by user to the user's local machine
        if userInput.lower() == "y":
            title = input("Enter the name of the file (do not including extension): ")
            title = f"{title}.jpg"
            plt.savefig(title)
    except:
        print("Input error.")

#Displays options for how to analyze data
def readDataOption(data):
    try:
        print()
        userInput = ""
        while userInput != "4":
            print("How would you like to analyze the data?")
            print("1. View the data")
            print("2. Filter the data")
            print("3. Create/view a graph")
            print("4. Go back")
            userInput = input("Enter a number option: ")
            if userInput == "4":
                break
            elif userInput == "1":
                viewData(data)
            elif userInput == "2":
                filterData(data)
            elif userInput == "3":
                graphData(data)
            else:
                print("Option not found!")
    except OSError:
        print("Could not find csv file.")
    except:
        print("Encountered error, returning to previous menu...")
        print()

#Reads a data file to perform functions on
def readFile():
    try:
        fileName = input("Enter file name (include the .csv extension): ")
        print()
        data = pd.read_csv(fileName)
        readDataOption(data)
    except OSError:
        print("Error reading file, returning to previous menu...")
        readOptionInput()

#Called when user wants to access an existing chart.
#Asks user for the file name and displays the chart.
def accessPlot():
    try:
        title = input("Enter the name of the file (include the extension): ")
        img = mpimg.imread(title)
        plt.imshow(img)
        plt.axis("off")
        plt.show()
    except:
        print("Error trying to read file.")

#Default options displaying when the program first runs.
#Either access a new csv file or an existing graph.
def readOptionInput():
    print("Music Data Analyzer")
    print("This program can analyze and create graphs on music popularity data")
    userInput = ""
    while userInput.lower() != "q":
        print("Options: ")
        print("1. Analyze a new csv file: ")
        print("2. Access an existing graph")
        print("q. To Quit")
        userInput = input("Enter a number option: ")
        if userInput.lower() == "q":
            break
        elif userInput == "1":
            readFile()
        elif userInput == "2":
            accessPlot()
        else:
            print("Error: Not a valid option.")

def main():
    readOptionInput()

if __name__ == "__main__":
    main()