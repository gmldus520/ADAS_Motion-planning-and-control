import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class LowPassFilter:
    def __init__(self, y_initial_measure, alpha=0.9):
        self.y_estimate = y_initial_measure
        self.alpha = alpha
        self.y_estimate = y_initial_measure
 
    def estimate(self, y_measure):
        self.y_estimate = self.alpha * self.y_estimate + (1 - self.alpha) * y_measure
        return self.y_estimate


if __name__ == "__main__":
    #signal = pd.read_csv("01_filter/Data/example_Filter_1.csv")
    #signal = pd.read_csv("01_filter/Data/example_Filter_2.csv")      
    signal = pd.read_csv("D:/Workspace/ADAS_motion_planning_and_control/01_Filter/Data/example_Filter_3.csv")
   
    # y_estimate 컬럼 초기화
    signal["y_estimate"] = 0.0

    filter_instance = LowPassFilter(signal.y_measure[0], alpha=0.9)
    for i in range(len(signal)):
        est = filter_instance.estimate(signal.y_measure[i])
        signal.loc[i, "y_estimate"] = est  # loc로 경고 방지

    # 시각화
    plt.figure()
    plt.plot(signal.time, signal.y_measure, 'k-', label="Measure")
    plt.plot(signal.time, signal.y_estimate, 'r-', label="Estimate")
    plt.xlabel('time (s)')
    plt.ylabel('signal')
    plt.legend(loc="best")
    plt.grid(True)
    plt.title("Low Pass Filter Result")
    plt.show()



