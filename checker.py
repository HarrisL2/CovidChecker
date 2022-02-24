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


with open('list.csv', newline='', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    locationList = list(reader)

found = False
with open('results.txt', 'w', encoding='utf-8-sig') as file:
    for location in locationList:
        for data in parsedData:
            if data.find(location[0]) != -1:
                file.write(location[0].ljust(12) + " is in " + filesToParse[parsedData.index(data)]+"\n")
                found = True
    if (not found):
        file.write("No affected buildings found.")


