#!/bin/bash
echo "Script by Cole Petty"
echo "Ensure the current directory has trip json tests."
echo "Also please have your server running and tunnel connected."
echo "Beginning trip automated testing."
file="trip_output.txt"
if [ -f $file ] ; then
   rm "$file"
fi
python3 trip_test_automator314.py > trip_output.txt
echo "Success."
echo "Results stored in $file"
