"""
functions to read the a CSV file
and put it into a dictionary
"""
import os
import csv

def read_palette_from_file(palette_filename):
    """
    read the palette from the csv file.
    Each row is a key and an RGB triple.  Make that RGB triple
    into a TUPLE and then put into a dictionary with the key.
    """
    dictionary = {}
    with open(palette_filename, 'r') as f:
        csv_reader = csv.reader(f)

        for row in csv_reader:
            key = int(row[0])

            R_value = int(row[1])
            G_value = int(row[2])
            B_value = int(row[3])

            RGB_tuple = (R_value, G_value, B_value)


            dictionary[key] = RGB_tuple


    return(dictionary)
