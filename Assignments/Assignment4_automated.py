
#  Click the link below and download the SQLite database named "chinook.db".
# Link: https://sites.google.com/site/yasinunlu/home/research/new1/chinook.db
#  You can browse the given database file using an online database browser. Here is an example link: https://sqliteonline.com/. How many tables are there in the database?

import pandas as pd
import sqlite3
import json as JSON
import os

def file_write(table, db_loc, save_loc):
	"""This is a function for automated creation of CSV, TSV, and JSON files from a dataframe imported from a database."""
	# Establish a connection using Python code below.
	conn = sqlite3.connect(db_loc)

	# Read tables in the database as Pandas dataframe.
	query = "SELECT * FROM " + table + ";"
	df = pd.read_sql_query(query, conn)

	conn.close()

	# Store each dataframe as a CSV file (in .csv and .txt extensions) and a TSV file in .txt extension.
	ext_CSV_csv = table +"_CSV.csv"
	ext_CSV_txt = table +"_CSV.txt"
	ext_TSV_txt = table +"_TSV.txt"

	df.to_csv(os.path.join(directory, ext_CSV_csv), index = False)
	df.to_csv(os.path.join(directory, ext_CSV_txt), index = False)
	df.to_csv(os.path.join(directory, ext_TSV_txt), sep = "\t", index = False)

	# Store each dataframe file as a .json file by using to_json() in Pandas.
	ext_json = table + ".json"
	df.to_json(os.path.join(directory, ext_json))

	# Read each .json file as a single string by using read() function in Python.
	with open(os.path.join(directory, ext_json), "r") as json_file:
	    json_data = json_file.read()

	# Create a JSON object by using json.loads().
	json_object = JSON.loads(json_data)

	# Convert the JSON object into an indented format by using json.dumps() function.
	json_formatted = JSON.dumps(json_object, indent = 2)

	# Write the formatted data into a file with .json extension. Use write() function.
	ext_json_formatted = table + "_formatted.json"
	with open(os.path.join(directory, ext_json_formatted),"w") as file:
	    file.write(json_formatted)


chinook = "..\\data\\chinook.db"
directory = "Assignment4_files_auto\\"

# query the database for the names of all the tables
conn = sqlite3.connect("..\\data\\chinook.db")
cur = conn.cursor()
cur.execute('SELECT name from sqlite_master WHERE type= "table"')
db_tables = cur.fetchall()
conn.close()

# create a list of the table names in the database
table_names = [table[0] for table in db_tables]

table = "employees"

file_write(table, db_loc=chinook, save_loc=directory)
file_write(, db_loc=chinook, save_loc=directory)