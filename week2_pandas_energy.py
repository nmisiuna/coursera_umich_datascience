import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('Energy Indicators.xls')
df = df.drop(df.index[0:16])
df = df.drop(df.iloc[:, 0:2], axis = 1)
df.reset_index(inplace = True)
df.columns = ['index', 'Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
df = df.drop(columns = 'index')
df.dropna(inplace = True)

#Convert missing values '...' to 'np.NaN
df[df == '...'] = np.NaN

#Convert petajoules to gigajoules
df['Energy Supply'] *= 1000000

#Remove parenthesis from country names
df['Country'] = df['Country'].str.split('(', expand = True)[0]
df['Country'] = df['Country'].apply(lambda x: ''.join([i for i in x if not i.isdigit()]))

#Fix trailing white space at end of country names
df['Country'] = df['Country'].map(lambda x: x.rstrip())

#Renaming 4 countries
def replace_value(df, col, old_value, new_value):
    df.loc[df[df[col] == old_value].index, col] = new_value

replace_value(df, 'Country', 'Republic of Korea', 'South Korea')
replace_value(df, 'Country', 'United States of America', 'United States')
replace_value(df, 'Country', 'United Kingdom of Great Britain and Northern Ireland', 'United Kingdom')
replace_value(df, 'Country', 'China, Hong Kong Special Administrative Region', 'Hong Kong')

#print(df.loc[20:100, 'Country'])

#Read in GDP dataset
GDP = pd.read_csv('world_bank.csv', sep = ',', header = 4)
replace_value(GDP, 'Country Name', 'Korea, Rep.', 'South Korea')
replace_value(GDP, 'Country Name', 'Iran, Islamic Rep.', 'Iran')
replace_value(GDP, 'Country Name', 'Hong Kong SAR, China', 'Hong Kong')
GDP.rename(columns = {'Country Name': 'Country'}, inplace = True)

#Read in scimago dataset
ScimEn = pd.read_excel('scimagojr-3.xlsx')

#Get the labels for columns to take from GDP
z = '20'
GDP_labels = ['Country']
for i in range(6, 16):
    if i < 10:
        GDP_labels.append(z + '0' + str(i))
    else:
        GDP_labels.append(z + str(i))

#Get the subset to take from ScimEn (top 15 rank)
#ScimEn_subset = ScimEn.sort_values(by = 'Rank', ascending = True).iloc[0:15]

#Merge
merged = pd.merge(ScimEn, GDP[GDP_labels], how = 'inner', left_on = 'Country', right_on = 'Country')
merged = pd.merge(merged, df, how = 'inner', left_on = 'Country', right_on = 'Country')
merged = merged.set_index('Country')
#Get the subset to take from ScimEn (top 15 rank)
z = merged.sort_values(by = 'Rank', ascending = True).iloc[0:15]
print(z)

#Q2
#How many entries did we lose?
print(len(merged.index) - 15)

#Q3
new_df = z.copy()
#Only consider new_df
#What is the average GDP over last 10 years for each country?
#Exclude missing values
labels = []
for i in range(6, 16):
    if i < 10:
        labels.append('200' + str(i))
    else:
        labels.append('20' + str(i))

ave_GDP = new_df[labels].mean(axis = 1, skipna = True).sort_values(ascending = False)
print(ave_GDP)

#Q4
#By how much had the GDP changed over 10 years for country with 6th largest
#average GDP?
#Get the 6th country
change = new_df.loc[ave_GDP.index[5], '2015'] - new_df.loc[ave_GDP.index[5], '2006']
print(change)

#Q5
#What is the mean energy supply per capita?
print(new_df['Energy Supply per Capita'].mean(axis = 0))

#Q6
#Which country has the maximum % Renewable and what is the percentage?
print(new_df['% Renewable'].sort_values(ascending = False).index[0])
print(new_df['% Renewable'].sort_values(ascending = False)[0])

#Q7
#Ratio of self-citations to total citations.  Max + country
z = new_df.loc[:, ['Self-citations', 'Citations']]
z['Ratio'] = (z['Self-citations'] + z['Citations']) / z['Citations']
print(z['Ratio'].sort_values(ascending = False).index[0])
print(z['Ratio'].sort_values(ascending = False)[0])


#Q8
#Create a column that estimates population using Energy Supply and Energy Supply
#per Capita.  What is the third most populous country?
z = new_df.loc[:, ['Energy Supply', 'Energy Supply per Capita']]
z['Pop Est'] = z['Energy Supply'] / z['Energy Supply per Capita']
print(z['Pop Est'].sort_values(ascending = False).index[2])
print(z['Pop Est'].sort_values(ascending = False)[2])

#Q9
#Create a column that estimates the number of citable documents per person
#What is the correlation between citable docs per capita and energy supply per
#capita?
z = new_df.loc[:, ['Citable documents', 'Energy Supply', 'Energy Supply per Capita']]
z['Citable Documents per Capita'] = z['Citable documents'] / (z['Energy Supply'] / z['Energy Supply per Capita'])
#z['Citable Documents per Capita'] = np.float64(z['Citable Documents per Capita'])
for col in list(z):
    z[col] = np.float64(z[col])
print(z.corr())

#Q10
#Create a new column with a 1 if % Renewable value is >= median
#Use top 15 only
z = new_df.copy()
z['HighRenew'] = pd.Series(range(0, len(z.index)))
z.loc[z['% Renewable'] >= z['% Renewable'].median(), 'HighRenew'] = 1
z.loc[z['% Renewable'] < z['% Renewable'].median(), 'HighRenew'] = 0
print(z['HighRenew'].sort_values(ascending = False))

#Q11
#Use the following dictionary to group Countries by Continent
#Then create a dataframe that displays sample size (number in each continent bin)
#Display sum, mean, and std dev for estimated population of each continent
ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}

z = new_df.copy()
y = z.groupby(by = ContinentDict, axis = 1)
#print(y.sum())
#z['sum'] = summed
#print(z)
