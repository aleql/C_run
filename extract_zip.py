# Decompress zip file in same folder
import zipfile

import os

import sys

"""
Extract zip receives a directory where a zip recides and a zip name
It extracts the zip in a folder with the same name as the zip
"""
def extract_zip(hwdirectory, zip_name):

    # Create dir to extract zip
    dir_name = zip_name.split('.')[0]
    extract_folder = hwdirectory + '/' + dir_name
    os.mkdir(extract_folder)

    # Extract zip
    zip_directory = hwdirectory + '/' + zip_name
    zip_ref = zipfile.ZipFile(zip_directory, 'r')
    zip_ref.extractall(extract_folder)
    zip_ref.close()

    return hwdirectory + '/' + dir_name


# extract_zip(sys.argv[1], sys.argv[2])