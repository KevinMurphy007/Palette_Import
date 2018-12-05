"""
functions to read the a CSV file
and put it into a dictionary
"""
import csv
mydict = dict()
def read_palette_from_file(palette_filename):
    """
    read the palette from the csv file.
    Each row is a key and an RGB triple.  Make that RGB triple
    into a TUPLE and then put into a dictionary with the key.
    """

    with open(palette_filename) as csvfile:
        read= csv.reader(csvfile)
        for row in read:
            key = row[0]
            key = int(key)
            value = [row[1], row[2], row[3]]
            mydict[key]= value
    return mydict
