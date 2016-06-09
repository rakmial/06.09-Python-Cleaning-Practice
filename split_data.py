# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
import re
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def split_save(filename,n,splinter):
    with open("{}-{}".format(filename,n), "w+") as file:
        sculpt = splinter + r'</us-patent-grant>'
        final = sculpt.strip()
        file.write(final)


def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.

    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """
    with open(filename, 'r') as f:
        rough = f.read()
        hewn = rough.split('</us-patent-grant>')
        for n in range(0,4):
            split_save(filename, n, hewn[n])

split_file(r'C:\Users\Bash\Desktop\Udacity\2_Data Analysis\P3\0609\patent.data')

def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


#test()
