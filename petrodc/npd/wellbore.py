import requests
import pandas as pd
import numpy as np


def wellbore(dataset_number):
    """
    Function to request wellbore data from NPD Database.

    Arguments:
        dataset_number (int): to select the dataset
            (1: oil samples,
            2: NPD ID,
            3: lithostratigraphy,
            4: history,
            5: drilling mud,
            6: drill stem tests,
            7: documents,
            8: cores,
            9: core photos,
            10: coordinates,
            11: casing and leak off,
            12: exploration,
            13: development,
            14: shallow)

    Returns:
        dataframe: requested data
    """

    data_list = ['with-oil-samples', 'with-npdid', 'with-lithostratigraphy', 'with-history', 'with-drilling-mud',
                 'with-drill-stem-tests', 'with-documents', 'with-cores', 'with-core-photos', 'with-coordinates',
                 'with-casing-and-leak-off', 'exploration', 'development', 'shallow']

    data = data_list[dataset_number - 1]

    return get_dataset(data)


def get_dataset(data):
    """
    looping through all pages, append in JSON dictionary, create dataframe
    This function is based on the Anne Estoppey's code https://github.com/AnneEstoppey/EasyDataTools
    """
    dataset = requests.get('https://hotell.difi.no/api/json/npd/wellbore/' + data + '?page=1').json()

    url_dataset = 'http://hotell.difi.no/api/json/npd/wellbore/' + data

    pages = dataset['pages']
    data_list = []
    for i in range(pages):
        url = url_dataset + f'?page={i + 1}'
        dataset_final = requests.get(url).json()
        entries = len(dataset_final['entries'])

        for entry in range(entries):
            data_list.append(dataset_final['entries'][entry])

    df = pd.DataFrame(data_list)
    df.replace('', np.nan, inplace=True)
    return df
