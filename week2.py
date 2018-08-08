import pandas as pd

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])

#Add a new column of unique values
df['Date'] = ['December 1', 'January 1', 'mid-May']
#Add a new column of one value repeated for all
df['Delivered'] = True
#Add yet another column
df['Feedback'] = ['Positive', None, 'Negative']

#Reset the indices to a sequence
#Redo Date column and have none for second element
adf = df.reset_index()
adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

#Merging
#This method uses a common index, so James will be one row with entries in both
#columns
z = pd.merge(staff_df, student_df, how = 'outer', left_index = True, right_index = True)

#This method retains only those indices which are present in all columns
z = pd.merge(staff_df, student_df, how = 'inner', left_index = True, right_index = True)

#This method keeps indices of the first dataframes
#Entries in second dataframe with a matching index are added from columns in
#the second dataframe
z = pd.merge(staff_df, student_df, how = 'left', left_index = True, right_index = True)
#This method keeps indices of the second dataframes
#Entries in first dataframe with a matching index are added from columns in
#the first dataframe
z = pd.merge(staff_df, student_df, how = 'right', left_index = True, right_index = True)


#This merges the same as 'left' from before, but specifies the column name to
#merge on since the indices names aren't present
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
z = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])

#This will merge and make new columns for Location_x, Location_y for the shared
#entries present in the right dataframe while retaining only those values in
#Name column from left dataframe
z = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
#This merges and takes only shared rows which are in BOTH first and last name
z = pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])
