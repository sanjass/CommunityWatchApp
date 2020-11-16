import pandas as pd
from sqlalchemy import create_engine

# connect to local sqllite Database
engine = create_engine('sqlite:///../crimedb.db')
conn = engine.connect()

# prepare dataframe to write to sql
crimes = pd.read_csv('Crime_Reports.csv')
# remove the crime record where Neighborhood is NaN
cleaned_crimes = crimes.dropna()
cleaned_crimes = cleaned_crimes[['File Number', 'Date of Report', 'Crime', 'Neighborhood']]
cleaned_crimes.columns = ['fileNumber', 'reportDate', 'crimeType', 'neighborhoodName']
Neighborhood = cleaned_crimes['neighborhoodName'].unique()
Neighborhood_index_dict = {}
Neighborhood_index_list = []
for i in range(1, len(Neighborhood) + 1):
    Neighborhood_index_dict[Neighborhood[i-1]] = i
    Neighborhood_index_list.append([i, Neighborhood[i-1]])
cleaned_crimes['neighborhoodId'] = cleaned_crimes['neighborhoodName'].map(Neighborhood_index_dict)
# crimes dataframe ready
cleaned_crimes = cleaned_crimes.drop(['neighborhoodName'], axis=1)
# neighborhoods dataframe ready
neighborhoods = pd.DataFrame(Neighborhood_index_list, columns=['id', 'neighborhood'])


# write the dataframe to SQL
# insert neighborhoods table first
neighborhoods.to_sql('neighborhoods', conn, index=False, if_exists='append')
print(engine.execute("SELECT COUNT(*) FROM neighborhoods").fetchall())
# insert crimes table
cleaned_crimes.to_sql('crimes', conn, index=False, if_exists='append')
print(engine.execute("SELECT COUNT(*) FROM crimes").fetchall())