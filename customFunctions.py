import pandas as pd
import numpy as np


def handleNull(dataset):
    dataset['Lat'].fillna(np.round((dataset['Lat'].mean()), 2), inplace=True)
    dataset['Long'].fillna(np.round((dataset['Long'].mean()), 2), inplace=True)

    return dataset

def loadData(urls):
    datasets = []
    for url in urls:
        if url:
            dataset = pd.read_csv(url, header=0)
            datasets.append(dataset)
    concatedDataset = pd.concat(datasets, axis=0, ignore_index=True)
    return concatedDataset

def checkMissingValues(data):
    # Calculate the count of missing values for each column
    missing_values_count = data.isnull().sum()

    # Print the count of missing values for each column
    for column, count in missing_values_count.items():
        print(f'{column}: {count}')



def replaceDistrictNames(dataset, columnName):
    districtMapping = {
        'A1': 'Downtown',
        'A15': 'Charlestown',
        'A7': 'East Boston',
        'B2': 'Roxbury',
        'B3': 'Mattapan',
        'C6': 'South Boston',
        'C11': 'Dorchester',
        'D4': 'South End',
        'D14': 'Brighton',
        'E5': 'West Roxbury',
        'E13': 'Jamaica Plain',
        'E18': 'Hyde Park',
        'No Data': 'No Data',
        'External': 'External'
    }

    dataset[columnName].replace(districtMapping, inplace=True)



