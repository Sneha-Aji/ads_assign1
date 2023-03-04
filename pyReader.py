import pandas as pd
import matplotlib.pyplot as plt

# function for reading contents from xlsx file
def readDataFile():
    df = pd.read_excel('Data2.xlsx', sheet_name = "Data")
    return df;

# function for plotting line graph
def plotLineGraph():
    
    df = readDataFile()
    x = list(df['Year'])
    y = list(df['Runs'])
    z = list(df['Average'])
    
    # for adding title
    plt.title("MS Dhoni Playing Statics")
    plt.plot(x, y, marker = 'o', label = "Runs")
    plt.plot(x, z, marker = 's', label = "Average")
    
    # set labels and show the legend
    plt.xlabel("YEAR")
    plt.ylabel("RUNS")
    plt.legend()
    plt.savefig("line.png", bbox_inches = "tight")
    plt.show()
    
#function for plotting pie chart
def plotPieChart():
    df = readDataFile()
    x = list(df['Year'])
    y = list(df['Runs'])
    z = list(df['Average'])
    dfNew = pd.DataFrame({'Runs':x, 'Average':z} , index = x)
    dfNew.plot.pie(subplots = True, figsize = (25, 25))
    plt.title("RUNS vs YEAR, AVERAGE vs YEAR")
    plt.savefig("pie.png", bbox_inches = "tight")
    plt.show()

# for plotting bar grpah
def plotBarGraph():
    df = readDataFile()
    x = list(df['Year'])
    y = list(df['Runs'])
    z = list(df['Average'])
    data = { "Runs":y,"Average":z};
    index = x;
    dfNew = pd.DataFrame(data = data, index = index);
    dfNew.plot.bar(rot = 15, title="Total Runs Scored Vs Average");
    
    # set labels and show the legend
    plt.xlabel("YEAR")
    plt.ylabel("RUNS")
    plt.legend()
    plt.savefig("bar.png", bbox_inches = "tight")
    plt.show(block = True);
    

#prompting for user input and showing graph conditionally
def promptInput():
    print('Please find the list of options available.')
    print('Press 1 for Player Statics( Line Chart)')
    print('Press 2 for Player Statics( Pie Chart)')
    print('Press 3 for Player Statics( Bar Chart)')
    userInput = int(input("Enter Input "))
    if(userInput == 1):
        plotLineGraph()
    elif(userInput == 2):
        plotPieChart()
    elif(userInput == 3):
        plotBarGraph()
    else:
        promptInput()

if __name__ == "__main__":
    # input prompt
    promptInput() 


    
