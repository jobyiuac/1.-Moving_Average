

# Importing necessary libraries
import pandas as pd 
from matplotlib import pyplot as plt


# Read data from csv
dataset = pd.read_csv('sinewave.csv')
print (dataset)



#___ Rolling Statistics: simplistic approach to make data stationary(Equal weightage)_____

for i in range (2,10):

    # Create new data using Rolling statistics on the original time series data
    rolling_series= dataset[1:110].rolling(window=i) # 1st 110 data as rolling series
    rolling_mean = rolling_series.mean() # MA for window = 10
    print(rolling_mean.head(10))
  
    #Plot the data   
    plt.plot(dataset, color='b', label='original data') # Plot the csv file
    plt.legend()
    plt.plot(rolling_mean, color='r', label ='Moving AVG') # Plot Rolling Mean
    plt.legend()
    plt.text(0,0.5,'window= ' + str(i))
    plt.show()
