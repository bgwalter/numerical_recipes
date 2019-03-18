#!/bin/bash

START=`date +%s`

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

echo "Running files..."
echo

echo "1. a) Poisson distribution"
python3 poisson.py > output/poisson.txt

echo "1. b) Randon number generator"
python3 RNG.py > output/RNG.txt



echo

END=`date +%s`
RUNTIME=$((END-START))

echo "Done! Runtime: $RUNTIME s"

echo
echo "Creating pdf..."

latexmk -pdf report.tex -silent
latexmk -silent -c

echo "Done! File saved to report.pdf"