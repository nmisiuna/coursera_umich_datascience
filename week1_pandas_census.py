import pandas as pd

data = pd.read_csv('./census.csv')#, sep = ',', header = 0)

print(data.head())

#Some county names are shared between states
#I did not consider this and I need to redo everything
#Maybe append state name to county name?
#That would be easy and would solve the whole problem
data['CTYNAME renamed'] = data['CTYNAME'] + ' ' + data['STNAME']

#Q5
#Which state has the most counties in it?
print(data.groupby('STNAME')['CTYNAME'].count().sort_values(ascending = False).index[0])

#Q6
#Only looking at the three most populous counties for each state
#What are the three most populous states?
#First find the three most populous counties for each state
#output: list of indices of three most populous counties per state
output = []
#Iterate through the states
for i in data['STNAME'].unique():
    #Seperate based on state
    #z: subset of data for ith state
    z = data[data['STNAME'] == i]
    #Sort the counties
    #1:4 index because top county name is same as state name, or sum for state
    output += list(z.sort_values(['CENSUS2010POP', 'CTYNAME'], ascending = False)[1:4].index)
#Now grab data of indices within output, groupby state name, then sum by census
#Sort and then grab top three.  Convert to list and done
populous = list(data.loc[output].groupby('STNAME')['CENSUS2010POP'].sum().sort_values(ascending = False).index[0:3])
print(populous)

#Q7
#Which county had the largest absolute change in population?
#Use POPESTIMATE2010 through POPESTIMATE2015 (6 columns)
#Ex: 100, 120, 80, 105, 100, 130 then it's 130 - 80 = 50
popestimates = []
for i in range(2010, 2016):
    popestimates.append('POPESTIMATE' + str(i))

#Only consider counties which don't have same name as state
counties = []
for i in data['CTYNAME'].unique():
    #Don't get this if county is same name as a state
    if i not in data['STNAME'].unique():
        counties += list(data[data['CTYNAME'] == i].index)
#Now using the indices of the counties compute different between the max and min
#of the popestimates columns
#Then return the county name of the highest one
data['pop_change'] = data.loc[counties][popestimates].max(axis = 1) - data.loc[counties][popestimates].min(axis = 1)
print(data.sort_values(['pop_change', 'CTYNAME'], ascending = False).iloc[0]['CTYNAME'])

#Q8
#US broken into four REGIONS.  Find counties that belong to regions 1 or 2
#whose names start with 'Washington'
#whose POPESTIMATE2015 > POPESTIMATE2014
z = data.copy()
#Use counties data from before
z = z.loc[counties]
#Get regions 1 and 2
z = z[z['REGION'].isin([1, 2])]
#Split the string and expand because I just want the first name
z['CTYNAME'] = z['CTYNAME'].str.split(' ', expand = True)[0]
#Grab only those counties with this = Washington
z = z[z['CTYNAME'] == 'Washington']
#Now 2015 pop estimate > 2014
z = z[z['POPESTIMATE2015'] > z['POPESTIMATE2014']]
print(z[['STNAME', 'CTYNAME']])
