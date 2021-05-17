import csv
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv('medium_data.csv')
data = df["id"].tolist()



def RamdonSetOfMeans(counter):
    list1 = []

    for i in range(0,counter):
        ramdonIndex = random.randint(0,len(data) - 1 )
        value = data[ramdonIndex]
        list1.append(value)
    mean = statistics.mean(list1)
    return mean

meanList = []
for i in range(0,1000):
    SetOfMeans = RamdonSetOfMeans(100)
    meanList.append(SetOfMeans)

population_mean = statistics.mean(meanList)
print(population_mean)

std = statistics.stdev(meanList)
print(std)

first_std_deviation_start, first_std_deviation_end = population_mean-std, population_mean+std
second_std_deviation_start, second_std_deviation_end = population_mean-(2*std), population_mean+(2*std)
third_std_deviation_start, third_std_deviation_end = population_mean-(3*std), population_mean+(3*std)

df = pd.read_csv("medium_data.csv")
data = df["id"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([meanList], ["id"], show_hist=False)
fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (population_mean - mean_of_sample1)/std
print("The z score is = ",z_score)