import pandas as pd


def date_int_to_year(date):
    return str(date)[:4]

homicide_data = pd.read_csv('homicide-data.csv', encoding = "ISO-8859-1")
homicide_data['year'] = homicide_data['reported_date'].apply(date_int_to_year)

year_state = homicide_data.groupby(['year', 'state']).count()['uid']
year_state.to_csv('count_by_year_and_state.csv')

year_state_disposition = homicide_data.groupby(['year','state','disposition']).count()['uid']
year_state_disposition.to_csv('count_by_year_state_and_disposition.csv')