import pandas as pd

def load_co2_data(filename="owid-co2-data.csv"):
   return pd.read_csv(filename)

def select_columns(df, columns=None):
    if columns is None:
        columns = ['co2', 'gdp', 'population', 'year']
    return df[columns]

def rename_columns(df, rename_dict=None):
    if rename_dict is None:
        rename_dict = {'co2':'co2_emissions', 'gdp':'gdp_per_capita'}
    return df.rename(columns=rename_dict)

def describe_data(df):
    return df.describe()

def describe_selected(df, columns=None):
    selected_df = select_columns(df, columns)
    return selected_df.describe()

def describe_renamed(df, rename_dict=None):
    df_renamed = rename_columns(df, rename_dict)
    return df_renamed.describe()
