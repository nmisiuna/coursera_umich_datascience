import pandas as pd

data = pd.read_csv('./olympics.csv', sep = ',', header = 1, index_col = 0)

for col in data.columns:
    if col[:2] == '01':
        data.rename(columns = {col:'Gold' + col[4:]}, inplace = True)
    if col[:2] == '02':
        data.rename(columns = {col:'Silver' + col[4:]}, inplace = True)
    if col[:2] == '03':
        data.rename(columns = {col:'Bronze' + col[4:]}, inplace = True)
    if col[:1] == '№':
        data.rename(columns = {col:'#' + col[1:]}, inplace = True)

names_ids = data.index.str.split('\s\(')

data.index = names_ids.str[0]
data['ID'] = names_ids.str[1].str[:3]

data.drop('Totals', inplace = True)
print(data.head())

#Q0
#What is the first country in data?
#Return the first row

#print(data.iloc[0])
print(data.loc['Afghanistan'])

#Q1
#Which country has won the most gold metals in summer games?
row_for_max_of_column = lambda data, col: data[data[col] == max(data[col])]
print(row_for_max_of_column(data, 'Gold.1'))

#Just the index corresponding to that one
index_for_max_of_column = lambda data, col: data.index[data[col] == max(data[col])][0]
print(index_for_max_of_column(data, 'Gold.1'))

#Q2
#Which country has the biggest difference between summer/winter gold count?
def winter_summer_dif(data, type):
    difference = (data[type] - data[type + '.1'])
    difference = difference.abs()
    return data[difference == max(difference)]
print(winter_summer_dif(data, 'Gold'))

#Q3
#Max dif between summer/winter gold medals rel. to total gold?
def winter_summer_dif_ratio(data, type):
    x = data[type] > 0
    y = data[type + '.1'] > 0
    z = []
    index = 0
    for item in x:
        z.append(x[index] and y[index])
        index += 1
    ratio = data[z].apply(lambda x: (x[type] - x[type + '.1']) / x[type + '.2'], axis = 1)
    return ratio[ratio == max(ratio)].index
#print(winter_summer_dif_ratio(data, 'Gold')[0])
print(data.loc[winter_summer_dif_ratio(data, 'Gold')])

#Q4
#Make a function that creates a Series called "Points" which is a weighted value
#where each Gold.2 counts as 3, Silver.2 as 2, Bronze.2 as 1
#Function should return column (Series object) with country names as indices
def medal_points(data):
    return data.apply(lambda x: x['Gold.2'] * 3 + x['Silver.2'] * 2 + x['Bronze.2'] * 1, axis = 1)
print (medal_points(data))
