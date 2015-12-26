from os import path, listdir
from geojson import crs, Point, FeatureCollection, Feature, dump, is_valid
import csv

__author__ = 'Matt'


class CsvToJson(object):
    """
    Parse OS Code Point Open CSV files to create GeoJson files.
    """
    def __init__(self):
        """
        Set paths
        """
        self.cur_dir = path.dirname(__file__)
        self.uk_postcodes = path.join(self.cur_dir, "uk_postcodes")

    def csv_to_json(self):
        """
        Main run method
        """
        csv_list = self.get_csv()
        if csv_list:
            for csv_f in csv_list:
                print csv_f
                fc = self.create_feature_collection(csv_f)
                validation = is_valid(fc)
                if validation['valid'] == 'yes':
                    self.encode_to_raw_json(fc, csv_f)
                else:
                    print "Failed to create GeoJson for file: " + csv_f + " - Error: " + str(validation['message'])
            print "Finished!"
        else:
            print "No CSV's to process"

    def get_csv(self):
        """
        Gets a list of all the CSV's in the scripts directory
        :return: List of CSV file names
        """
        all_csvs = [each for each in listdir(self.cur_dir) if each.endswith('.csv')]
        return all_csvs

    def create_feature_collection(self, csv_file):
        """
        Parse a CSV to create a FeatureCollection object for all postcodes.
        :param csv_file: csv file name
        :return: FeatureCollection of all postcodes in file
        """
        all_features = list()
        with open(path.join(self.cur_dir, csv_file), 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                postcode = str(row[0]).replace(' ', '')
                easting = float(row[2])
                northing = float(row[3])
                point = Point(coordinates=(easting, northing))
                feature = Feature(geometry=point, properties={'postcode': postcode})
                all_features.append(feature)
        # Set CRS to BNG
        coord_ref = crs.Named(properties={'name': 'EPSG:27700'})
        feature_collection = FeatureCollection(all_features, crs=coord_ref)
        return feature_collection

    def encode_to_raw_json(self, feature_collection, csv_f):
        """
        Encode a feature collection and dump into JSON file.
        :param feature_collection: FeatureCollection object
        :param csv_f: csv file name
        """
        clean_name = str(path.splitext(csv_f)[0]) + ".json"
        with open(path.join(self.uk_postcodes, clean_name), "wb") as json_outfile:
            dump([feature_collection], json_outfile)

run = CsvToJson()
run.csv_to_json()
