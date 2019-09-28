#!/usr/bin/env python
import glob
import sys
import os
import io
import mysql.connector

mydb = mysql.connector.connect(
  host=sys.argv[1],
  user=sys.argv[2],
  passwd=sys.argv[3],
  database="DRUGS",
  use_unicode=True
)

path = sys.argv[4] + "/*.txt"

mycursor = mydb.cursor()

for file in glob.glob(path):
    content = io.open(file, mode="r", encoding="utf-8").read()
    directory, filename = os.path.split(file)
    filename = filename.replace(".txt", "")
    sql = "INSERT INTO DRUG_LEAFTLET (leaflet, content) VALUES (%s, %s)"
    val = (filename, content)
    print(filename, " processing ...")
    mycursor.execute(sql, val)
    mydb.commit()

print("Done")