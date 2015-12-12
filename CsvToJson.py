from os import path, listdir

__author__ = 'Matt'


class CsvToJson(object):

    def __init__(self):
        pass

    def read_csv(self):
        # List all CSV's in script directory
        print("hello world")
        cur_dir = path.dirname(__file__)
        all_csvs = [each for each in listdir(cur_dir) if each.endswith('.csv')]

        print all_csvs


run = CsvToJson()

run.read_csv()
