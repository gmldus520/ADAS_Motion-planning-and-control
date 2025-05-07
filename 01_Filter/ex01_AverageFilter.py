import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AverageFilter:
    def __init__(self, window_size=5):
        # Code
        self.window_size = window_size
        self.buffer = []
                 
    def estimate(self, y_measure):
        # Code
        self.buffer.append(y_measure)
        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)
        return np.mean(self.buffer)
    
if __name__ == "__main__":
    signal = pd.read_csv("D:/IVS_Project/01_Motion_planning/99_Release/01_filter/Data/example_Filter_1.csv")
    #signal = pd.read_csv("01_filter/Data/example_Filter_2.csv")

    signal["y_estimate"] = 0.0

    avg_filter = AverageFilter(window_size=5)

    for i in range(len(signal)):
        signal.loc[i, "y_estimate"] = avg_filter.estimate(signal.loc[i, "y_measure"])

    plt.figure()
    plt.plot(signal.time, signal.y_measure,'k.',label = "Measure")
    plt.plot(signal.time, signal.y_estimate,'r-',label = "Estimate")
    plt.xlabel('time (s)')
    plt.ylabel('signal')
    plt.legend(loc="best")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


#for i, row in signal.iterrows():
#    #print(signal.time[i])
#    if (i==0):
#        signal.y_estimate[i] = signal.y_measure[i]
#    else:
#        signal.y_estimate[i] = (signal.y_estimate[i-1])*(num_average-1)/num_average + (signal.y_measure[i])/num_average




