""" Pandas """
#Pandas reads csv into a dataframe
import pandas as pd 
df = pd.read_csv(
    'file.csv',
    index_col='Name', #changes index col name
    parse_dates=['Hire Date'], #YYYY-MM--DD
    header = 0,  #ignores existing col names
    names = ['a','b','c']) #changes names of columns

df.columns   #Shows all column names in a list
df.describe(  #summarizes data
    include = 'object')  #includes objects

       """ Accessing & searching rows """
#Access specific columns by their names
df.column  #one word column. Capitalize if necessary
df['column name'] #column name that has a space
df[['column1', 'column2']] #get multiple columns

df.column.unique() #returns list of unique column names

#Condition-based filtering. Get specific rows
df[df['column'] == "{value wanted}"] #get rows with certain values
df[(df['column'] == "{value1}") & (df['column'] == "{value1}")] #multiple values

#Indexing rows and columns with iloc
df.iloc[row] #get specific row. 0-indexed. all columns
df.iloc[row, column] #specific cell coordinates
df.iloc[rowx:rowy] #slices rows from rowx to rowy

#Searching by keywords with loc
#set index of dataframe to a specific column
keyword = df.copy()  #Copies entire dataframe
keyword.set_index('keyword', inplace=True) #changes index
keyword.loc['value'] #gets rows with the value


        """ Updating columns """
df.isnull().sum()  #total missing cells for each column
df.dropna(inplace=True) #drops rows with missing values
df.drop('column', axis=1) #drop a specific column
df['New column'] = df['column1'] + df['column2'] #adds in a combined column
df['columnName'] = x #change every value in column to x
df.iloc[row, column] = x #change specific cell to x
df["new column"] = df['column'].apply(lambda x: 1 if x==True else 0)
 #change the data type and conditions of multiple columns
 
         """ Deleting & Ouputting """
#CSV output
df.to_csv('file.csv', 
          na_rep = '(missing)', #replaces nan
          date_format = '%m%d%Y', #date format
          sep = ',',  #the delimiter
          header=False) #no header row

df.to_json()  #JSON output
df.to_html()  #HTML output

#Deleting dataframe
del df 


""" Excel files """
#Reading excel
df = pd.read_excel('data.xlsx', index_col = 0)

#Write an Excel file
df.to_excel('data.xlsx')
