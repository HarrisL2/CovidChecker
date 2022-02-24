import tika
import csv
import os

filesToParse = []

with os.scandir('.') as it:
    for entry in it:
        if entry.name.endswith('.pdf'):
            filesToParse.append(entry.name)


tika.initVM()
from tika import parser
parsedData = []

for fileName in filesToParse:
    parsed = parser.from_file(fileName)
    parsedData.append(parsed["content"])


with open('list.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    locationList = list(reader)

found = False

for location in locationList:
    for data in parsedData:
        if data.find(location[0]) != -1:
            print(location[0].ljust(12) + " is in " + filesToParse[parsedData.index(data)])
            found = True

if (not found):
    print("No affected buildings found.")


