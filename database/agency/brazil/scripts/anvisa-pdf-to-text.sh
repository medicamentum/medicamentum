#!/bin/sh


echo "Converting PDF files in TXT ..."

for filename in $(ls $1/*.pdf); do pdftotext -enc UTF-8 $filename $filename".txt"; done;

echo "Done!"