from die import Die

import plotly.express as px

#create two d6 dice
die1=Die()
die2=Die()

#make some rolls and return the results
results=[]
for roll_num in range(1000):
    result=die1.roll()+die2.roll()
    results.append(result)

#Analyze the results
frequencies=[]
max_result=die1.num_sides + die2.num_sides
poss_results=range(2,max_result+1)
for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)
    
#visualize the results
title="Results of Rolling Two D6 1,000 Times"
labels={'x':'Result','y':'Frequency of Result'}
fig=px.bar(x=poss_results,y=frequencies,title=title,labels=labels)

#further customise chart
fig.update_layout(xaxis_dtick=1)

fig.show()