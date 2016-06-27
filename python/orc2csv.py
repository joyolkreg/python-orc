# -*- coding: utf-8 -*-
import os.path as path
import sys
from orcreader.reader import OrcReader

if len(sys.argv) <= 1:
    print "Usage: python orc2csv.py ORC_FILE"
    exit()

orc_file = path.realpath(sys.argv[1])
reader = OrcReader(orc_file)
reader.open()

max = reader.num_rows
for row in reader:
   print u",".join([unicode(field) for field in row]).encode("utf-8")

reader.close()
