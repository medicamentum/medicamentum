#!/bin/sh


echo "Converting PDF files in TXT ...""

for filename in $(ls $1/*.pdf); do pdftotext $filename $filename".txt"; done;

echo "Done!"



