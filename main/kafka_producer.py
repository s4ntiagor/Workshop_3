import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import time
from Kafka import kafka_producer

def ETL():
    df_2015 = pd.read_csv('C:/Users/valen/OneDrive/Documentos/ETL/workshop_3/Workshop_3/data/2015.csv')
    df_2016 = pd.read_csv('C:/Users/valen/OneDrive/Documentos/ETL/workshop_3/Workshop_3/data/2016.csv')
    df_2017 = pd.read_csv('C:/Users/valen/OneDrive/Documentos/ETL/workshop_3/Workshop_3/data/2017.csv')
    df_2018 = pd.read_csv('C:/Users/valen/OneDrive/Documentos/ETL/workshop_3/Workshop_3/data/2018.csv')
    df_2019 = pd.read_csv('C:/Users/valen/OneDrive/Documentos/ETL/workshop_3/Workshop_3/data/2019.csv')
    
    df_2018.loc[df_2018['Country or region'] == 'United Arab Emirates', 'Perceptions of corruption'] = df_2018.loc[df_2018['Country or region'] == 'United Arab Emirates', 'Perceptions of corruption'].fillna(0.182)

    column_mappings_2016 = {
        'Country': 'country', 
        'Region': 'region',
        'Happiness Rank': 'happiness_rank',
        'Happiness Score': 'happiness_score',
        'Lower Confidence Interval': 'lower_confidence_interval',
        'Upper Confidence Interval': 'upper_confidence_interval',
        'Economy (GDP per Capita)': 'economy_gdp_per_capita',
        'Family': 'social_support',
        'Health (Life Expectancy)': 'health_life_expectancy',
        'Freedom': 'freedom',
        'Trust (Government Corruption)': 'corruption',
        'Generosity': 'generosity',
        'Dystopia Residual': 'dystopia_residual'
    }
    df_2016.rename(columns=column_mappings_2016, inplace=True)
    df_2016.columns = [col.lower() for col in df_2016.columns]
    df_2016 = df_2016[['country', 'region', 'happiness_rank', 'happiness_score', 'lower_confidence_interval', 'upper_confidence_interval', 'economy_gdp_per_capita', 'social_support', 'health_life_expectancy', 'freedom', 'corruption', 'generosity', 'dystopia_residual']]
    
    column_mappings_15 = {
        'Country': 'country', 
        'Region': 'region',
        'Happiness Rank': 'happiness_rank',
        'Happiness Score': 'happiness_score',
        'Standard Error': 'standard_error',
        'Economy (GDP per Capita)': 'economy_gdp_per_capita',
        'Family': 'social_support',
        'Health (Life Expectancy)': 'health_life_expectancy',
        'Freedom': 'freedom',
        'Trust (Government Corruption)': 'corruption',
        'Generosity': 'generosity',
        'Dystopia Residual': 'dystopia_residual'
    }
    df_2015.rename(columns=column_mappings_15, inplace=True)
    df_2015.columns = [col.lower() for col in df_2015.columns]
    df_2015 = df_2015[['country', 'region', 'happiness_rank', 'happiness_score', 'standard_error', 'economy_gdp_per_capita', 'social_support', 'health_life_expectancy', 'freedom', 'corruption', 'generosity', 'dystopia_residual']]

    column_mappings_17 = {
        'Country': 'country',
        'Happiness.Rank': 'happiness_rank',
        'Happiness.Score': 'happiness_score',
        'Whisker.high': 'whisker_high',
        'Whisker.low': 'whisker_low',
        'Economy..GDP.per.Capita.': 'economy_gdp_per_capita',
        'Family': 'social_support',
        'Health..Life.Expectancy.': 'health_life_expectancy',
        'Freedom': 'freedom',
        'Generosity': 'generosity',
        'Trust..Government.Corruption.': 'corruption',
        'Dystopia.Residual': 'dystopia_residual'
    }
    df_2017.rename(columns=column_mappings_17, inplace=True)
    df_2017.columns = [col.lower() for col in df_2017.columns]
    df_2017 = df_2017[['country', 'happiness_rank', 'happiness_score', 'whisker_high', 'whisker_low', 'economy_gdp_per_capita', 'social_support', 'health_life_expectancy', 'freedom', 'generosity', 'corruption', 'dystopia_residual']]

    column_mappings_1819 = {
        'Overall rank': 'happiness_rank',
        'Country or region': 'country',
        'Score': 'happiness_score',
        'GDP per capita': 'economy_gdp_per_capita',
        'Social support': 'social_support',
        'Healthy life expectancy': 'health_life_expectancy',
        'Freedom to make life choices': 'freedom',
        'Generosity': 'generosity',
        'Perceptions of corruption': 'corruption'
    }
    df_2018.rename(columns=column_mappings_1819, inplace=True)
    df_2018.columns = [col.lower() for col in df_2018.columns]
    df_2018 = df_2018[['country', 'happiness_rank', 'happiness_score', 'economy_gdp_per_capita', 'social_support', 'freedom', 'health_life_expectancy', 'generosity', 'corruption']]

    df_2019.rename(columns=column_mappings_1819, inplace=True)
    df_2019.columns = [col.lower() for col in df_2019.columns]
    df_2019 = df_2019[['country', 'happiness_rank', 'happiness_score', 'economy_gdp_per_capita', 'social_support', 'freedom', 'health_life_expectancy', 'generosity', 'corruption']]

    df_2015 = df_2015.drop(['region', 'standard_error', 'dystopia_residual'], axis=1, errors='ignore')
    df_2016 = df_2016.drop(['region', 'lower_confidence_interval', 'upper_confidence_interval', 'dystopia_residual'], axis=1, errors='ignore')
    df_2017 = df_2017.drop(['whisker_high', 'whisker_low', 'dystopia_residual'], axis=1, errors='ignore')
    
    df = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], ignore_index=True)
    
    columns_to_drop = ['country', 'happiness_rank']
    df = df.drop(columns=columns_to_drop, errors='ignore')
    df = df.dropna()
    
    return df


def training(df):
    X = df[['economy_gdp_per_capita', 'social_support', 'health_life_expectancy', 'freedom', 'corruption', 'generosity']]
    y = df['happiness_score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=59)
    return df.loc[y_test.index]

if __name__ == "__main__":
    df = ETL()
    df = training(df)
    time_between_messages = 1
    for index, row in df.iterrows():
        kafka_producer(row)
    
    