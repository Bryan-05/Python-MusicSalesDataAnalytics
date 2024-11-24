import csv
import matplotlib.pyplot as plt

x = []
y = []

with open('MusicSalesDataSample.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)

    for row in csvFile:
        x.append(row[0])
        y.append(int(row[2]))

plt.bar(x, y, color = 'g', width= 0.8, label = "Test")

plt.show()