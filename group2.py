# Create a program that creates age categories. Then create a plot or chart that shows how many individuals of each age group survived and did not survive.

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("Titanic-Dataset.csv")

age = df["Age"]
survivors = df["Survived"]

data_list = ["age"]
print(data_list)

if age <= 20 and survivors == 1:
    print("hi")

    



