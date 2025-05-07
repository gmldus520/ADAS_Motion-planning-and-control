import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class MovingAverageFilter:
    def __init__(self, y_initial_measure, num_average=2):
        self.num_average = int(num_average)
        self.window = [y_initial_measure]

    def estimate(self, y_measure):
        self.window.append(y_measure)
        if len(self.window) > self.num_average:
            self.window.pop(0)
        self.y_estimate = np.mean(self.window)
        return self.y_estimate

    
if __name__ == "__main__":
    # CSV 파일 경로를 문자열로 정확히 지정 (백슬래시는 두 번 \\ 또는 r'문자열')
    signal = pd.read_csv("D:/Workspace/ADAS_motion_planning_and_control\01_Filter\Data\example_Filter_2.csv")

    # y_estimate 컬럼 초기화
    signal["y_estimate"] = 0.0

    filter_instance = MovingAverageFilter(signal.y_measure[0], num_average=5)
    for i in range(len(signal)):
        est = filter_instance.estimate(signal.y_measure[i])
        signal.loc[i, "y_estimate"] = est  # loc를 사용하여 경고 방지

    # 시각화
    plt.figure()
    plt.plot(signal.time, signal.y_measure, 'k.', label="Measure")
    plt.plot(signal.time, signal.y_estimate, 'r-', label="Estimate")
    plt.xlabel('time (s)')
    plt.ylabel('signal')
    plt.legend(loc="best")
    plt.grid(True)
    plt.title("Moving Average Filter Result")
    plt.ylim(-5, 15)
    plt.show()


