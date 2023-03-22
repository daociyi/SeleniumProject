import csv
import json
from contextlib import ExitStack

import yaml

csvlist = []

with open("csvdata.csv","r",encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        csvlist.append(dict(row))
print(csvlist)

# def newyaml(oldyamlfile,newyamlfile):
def newfile(oldyamlfile,newyamlfile):
    with ExitStack() as stack:
        old = stack.enter_context(open(oldyamlfile,"r"))
        newoutput = stack.enter_context(open(newyamlfile,"w"))
        old_line = old.readlines()
        for i in range(0,len(csvlist)):
            for line in old_line:
                print(line)
                newoutput.write(line)
            newoutput.write("\n")
newfile("csvyaml","csvtrans_yaml")