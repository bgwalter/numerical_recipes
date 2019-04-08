#!/bin/bash

echo
echo -e "\tBrendon Walter (s2078864)"
echo -e "\twalter@strw.leidenuniv.nl"
echo -e "\tNumerical Recipes in Astrophysics"
echo -e "\tAssignment 1"
echo 


# create output directory if it doesn't already exist
if [ ! -d "output" ]; then
  mkdir output
fi

echo "Running code..."
echo

python3 handin1.py

echo "Done!"

echo
echo "Creating pdf..."
echo

latexmk -pdf report.tex -silent
latexmk -silent -c

echo 
echo "Done! File saved to report.pdf"
echo
