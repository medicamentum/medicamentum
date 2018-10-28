#!/usr/bin/env python
import glob
import sys
import os
import io
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="drugs",
  passwd="Drug$Drug$2020",
  database="DRUGS",
  use_unicode=True
)

path = sys.argv[1] + "/*.txt"

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