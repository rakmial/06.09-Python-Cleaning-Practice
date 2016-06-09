"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def year_clean(dict_entry):
    for year in range(1886,2014):
        if str(year) + '-01-01T00:00:00+02:00' in dict_entry:
            return year
    return False

def check_URI(dict_entry):
    if 'dbpedia.org' not in dict_entry:
        return False
    else:
        return dict_entry

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        car_list = []
        good_year = []
        bad_year = []
        for row in reader:
            car_list.append(row)
        for entry in car_list:
            entry['URI'] = check_URI(entry['URI'])
            entry['productionStartYear'] = year_clean(entry['productionStartYear'])
            if entry['URI'] == False:
                continue
            elif entry['productionStartYear'] == False:
                bad_year.append(entry)
            else:
                good_year.append(entry)


    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in good_year:
            writer.writerow(row)

    with open(output_bad, "w") as h:
        writer = csv.DictWriter(h, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in bad_year:
            writer.writerow(row)

process_file(r'C:\Users\Bash\Desktop\Udacity\2_Data Analysis\P3\0609\autos.csv', OUTPUT_GOOD, OUTPUT_BAD)

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


#if __name__ == "__main__":
#    test()
