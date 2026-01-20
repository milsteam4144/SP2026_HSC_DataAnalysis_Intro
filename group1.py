# Create a program that lists all the names of the passengers that survived and another list that shows all the names of the passengers that survived.
# Create a plot to show the number of females that survived vs the number of males that survived.

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("Titanic-Dataset.csv")

# List of passengers who survived
survived_names = df[df["Survived"] == 1]["Name"].tolist()

# List of passengers who did NOT survive
not_survived_names = df[df["Survived"] == 0]["Name"].tolist()

plt.plot(df['Sex'], df['Number of Passengers'])
plt.title('Survived vs Not Survived by Sex')
plt.xlabel('Sex')
plt.ylabel('Number of Passengers')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.savefig('output.pnt')
plt.show()

print("Survivors: ")
print(survived_names)

print("\nDid not survived: ")
print(not_survived_names)

# Plot: Female vs Male survives
sns.countplot(data=df[df["Survived"] == 1], x="Sex")
plt.title("Number of Survivors by Sex")
plt.xlabel("Sex")
plt.ylabel("Number of Survivors")
plt.show()