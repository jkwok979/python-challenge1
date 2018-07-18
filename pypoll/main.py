import pandas as pd
file = "election_data.csv"
election_data = pd.read_csv(file)

election_data.head()

votertotal = len(election_data["Voter ID"].unique())

votertotal

total_votes = election_data['Candidate'].value_counts()
total_votes

df = pd.DataFrame(total_votes)
df.head()

votes_percent = total_votes/votertotal
votes_percent

totalvotes = total_votes.copy().tolist()
totalvotes

percentages = votes_percent.copy().tolist()
percentages

names = ['Khan','Correy','Li',"O'Tooley"]
names

print("Election results")
print("---------------------------")
print("Total votes: " + str(votertotal))
print("---------------------------")
print(names[0] + ": " + "(" + str(round(percentages[0]*100,3))+"%) " + str(totalvotes[0]))
print(names[1] + ": " + "(" + str(round(percentages[1]*100,3))+"%) " + str(totalvotes[1]))
print(names[2] + ": " + "(" + str(round(percentages[2]*100,3))+"%) " + str(totalvotes[2]))
print(names[3] + ": " + "(" + str(round(percentages[3]*100,3))+"%) " + str(totalvotes[3]))
print("---------------------------")
print("Winner: " + names[0])
print("---------------------------") 