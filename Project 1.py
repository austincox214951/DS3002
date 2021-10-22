#Importing the csv and json libraries
import csv
import json

#defines the json array which will be used to create the eventual json dictionary
#Creates numrecords and numcol variables, which will be used to print out the total number of records in the dataset,
#as well as the number of columns in each entry
jsonArray = []
numrecords = 0
numcol = 0

#This opens the Air_Quality.csv file as a csvfile, and reads it as a dictionary using the DictReader function
#As each row gets read in, it is appended to the jsonArray previously defined and the total number of records
#increases by 1.
with open("Air_Quality.csv") as csvDataFile:
    csvReader = csv.DictReader(csvDataFile)
    for row in csvReader:
        jsonArray.append(row)
        numrecords += 1

#This creates a new json file called Air_Quality.json. The 'w' indicates that we are writing rather than reading.
#The json.dumps function converts the python object, in this case the jsonArray, into a json string that can be written
#into the Air_Quality.json file.  The indent is just for readability purposes.  Finally, we write our json string to
#the previously created jsonfile ("Air_Quality.json") which saves it to our local machine for use with SQL.

with open("Air_Quality.json", 'w') as jsonfile:
    jsonstr = json.dumps(jsonArray, indent=5)
    jsonfile.write(jsonstr)

#This portion of the program contains a nested for function.  First, the each entry in "jsonArray" is input as "record".
#Then, the number of columns is set to 0.  This is so when we output the total number of columns of data, we get a number
#per record, rather than the number of columns times the number of records.  Finally, each column of the record is loaded
#in and upon doing so, the numcol variable increases by 1 until the end of the "record" is reached
for record in jsonArray:
    numcol = 0
    for column in record:
        numcol += 1

#Finally, these statement just let the user know how many records were in the file, as well as how many columns of data
#are in each record
print("There are", str(numrecords), "records in Air_Quality.csv")
print("Each record contains", numcol, "different columns of data")










