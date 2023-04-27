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
    with open(newyamlfile) as f:
        f.close()
    with ExitStack() as stack:
        old = stack.enter_context(open(oldyamlfile,"r"))
        newoutput = stack.enter_context(open(newyamlfile,"w"))
        old_line = old.readlines()
        for i in range(0,len(csvlist)):
            for line in old_line:
                new_line = str(line)
                if new_line.find('$csv{')>0:
                    value = new_line.split(':')
                    key = value[1].strip().split('{', 1)[1].split('}')[0]
                    replacement = ""
                    if key in csvlist[i].keys():
                        replacement = csvlist[i][key]
                        # for j in range(0,len(csvlist[i])):
                        new_line = new_line.replace(value[1].strip(), replacement)
                newoutput.write(new_line)
            newoutput.write("\n")

newfile("csvyaml","csvtrans_yaml.yaml")