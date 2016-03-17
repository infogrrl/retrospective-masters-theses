#*********************************************************************************************
#
# This module is designed to pull "Number of Pages" from a folder of pdfs and generate a CSV file
#       of them for use in thesis metadata for the ETD project.
#
# The outputs are:
#       * a CSV file of the file names and number of pages for each file anaylyzed
#
# Created by Kelly Thompson, June 2014, based on the pycdm module built by Shawn Averkamp.
#
#*********************************************************************************************

#**************************************************************
# import all the necessary libraries
#**************************************************************

import pyPdf

# use to create directories
import os

# regular expressions
import re

# opening files w/ certain encodings
# import codecs

# import cStringIO

import string

# library for creating/workingwith/writing to/parsing CSV files.  We're outputting to CSV
import csv

# library for working w/ file-like objects
import io

# get the date for the filename
import datetime
today = datetime.date.today().strftime('%Y-%m-%d')


#**************************************************************
# Create the directory folder where you will put everything you're collecting
#**************************************************************

# create variable for name of directory
datadir = 'pages'

# path is collection of fx w/in OS.
# could say from OS import PATH to save memory
# returns true/false
# if it doesn't exist, make a directory called 'cookbooks'
# keeps all files in same place
if not os.path.isdir(datadir):
    os.mkdir(datadir)

#**************************************************************
# Create the CSV file for the metadata for all the cookbooks you are exporting.
# Create the writer which will record data to this file.
#**************************************************************

# create metadata file
# should get current date instead of being hard coded
# get date and save as variable, put variable in...
# mode w=write + read/write??
metadata = open(datadir + '/pages_' + today + '.csv', mode='w+')

# UnicodeWriter for writing Unicode values to CSV [From Shawn's audioVideoHarvest.py script]

#class UnicodeWriter:
 #   """
  #  A CSV writer which will write rows to CSV file "f",
   # which is encoded in the given encoding.
    #"""

    #def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
     #   self.queue = cStringIO.StringIO()
      #  self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
       # self.stream = f
        #self.encoder = codecs.getincrementalencoder(encoding)()

    #def writerow(self, row):
     #   self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
      #  data = self.queue.getvalue()
       # data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        #data = self.encoder.encode(data)
        # write to the target stream
        #self.stream.write(data)
        # empty queue
        #self.queue.truncate(0)

#    def writerows(self, rows):
 #       for row in rows:
  #          self.writerow(row)

##########################################
#OLD CSV WRITER -- THROWS ASCII ERRORS
# create writer for writing to CSV file
wtr = csv.writer(metadata, delimiter=',')
##########################################

# create array for header row
headerrow = ['Filename', 'Number_of_Pages']
# write the list to the CSV file
#OLD writer obj fx writerow (coming from CSV library)
#wtr = csv.writer(metadata, delimiter=',')
wtr.writerow(headerrow)

#**************************************************************
# Ask the user which pdfs they want to open
#**************************************************************

# getting folder info
folderpath = raw_input('Enter the filepath of the folder containing your PDFs with no quotation marks and ensuring that each backslash is changed to a forward slash:')

def to_unicode_or_bust(
        obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj

                      
#**************************************************************
# Begin the process 
# For each:
#**************************************************************

from pyPdf import PdfFileReader

folderlist = os.listdir(folderpath)

for d in folderlist:
    d = d.strip(' ')
    pdfopen = PdfFileReader(open(folderpath + '/' + d, 'rb'))
    pdfpages = pdfopen.getNumPages()       
    row = [d, pdfpages]
    wtr.writerow(row)

    #****************************************************************
    # keep cycling...
    #****************************************************************
        
#****************************************************************
# close the CSV file
#****************************************************************
metadata.close()

print "Done."

