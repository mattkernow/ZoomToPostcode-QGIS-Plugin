"""
###################################################################
os_csv_to_pickle.py - A script to create postcode pickle files from OS
Codepoint openData.
Place script in same directory as CSV's and run. A new folder with
the pickes files will be created within the same directory.
###################################################################
"""

import csv
import pickle
import os

# List all CSV's in script directory
cur_dir = os.path.dirname(__file__)
all_csvs = [each for each in os.listdir(cur_dir) if each.endswith('.csv')]
UK_Postcodes = os.path.join(cur_dir, "UK_Postcodes")

# Create dir for new pickle files
if all_csvs and not os.path.exists(UK_Postcodes):
    os.makedirs(UK_Postcodes)

# For each csv, a pickle file is created and dict of postcodes is dumped
for each_csv in all_csvs:
    print "Pickling " + each_csv
    file_dict = {}
    with open(os.path.join(cur_dir, each_csv), 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            postcode = str(row[0]).replace(' ', '')
            eastings = row[2]
            northings = row[3]
            file_dict[postcode] = (eastings, northings)
    clean_name = str(os.path.splitext(each_csv)[0]) + ".pkl"
    pkl = open(os.path.join(UK_Postcodes, clean_name), 'wb')
    pkl_dict = pickle.dump(file_dict, pkl)
    pkl.close()
    
print "Finished!"
