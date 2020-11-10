from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import os
import lasio


def get_las(number_of_files):
    """
    Function to get well logs data as dataframes from Special Report 006 Athabasca Oil Sands Data
    McMurray/Wabiskaw Oil Sands Deposit (Alberta, Canada). By Alberta Geological Survey (AGS).

    Arguments:
        number_of_files (int): number of files to get, max. of 2173

    Returns:
        dictionary {key -> 'Unique well identifier', value -> dataframe}: data
    """

    zipfile_url = r'https://static.ags.aer.ca/files/document/SPE/SPE_006.zip'        # url to the data as a zip file

    with urlopen(zipfile_url) as resp:
        with ZipFile(BytesIO(resp.read())) as zip_file:
            zip_file.extractall('/tmp/ags_spe')         # extracting files

    datasets_dict = {}      # creating an empty dictionary to store results
    directory = r'/tmp/ags_spe/OilSandsDB/Logs/'
    files_list = os.listdir(directory)

    for filename in files_list[:number_of_files]:

        if filename.endswith(".las") or filename.endswith(".LAS"):

            path = os.path.join(directory, filename)        # get specific path as str
            df = lasio.read(path).df()                      # convert .las to dataframe using lasio

            filename = filename.replace('.LAS', '')
            filename = filename.replace('.las', '')

            # adding the dataframe to the dictionary {'Unique well identifier': dataframe}
            datasets_dict.update({filename: df})

    return datasets_dict
