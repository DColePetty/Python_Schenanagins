 #!/bin/bash
echo "Script by Cole Petty"
echo "Ensure the current directory has distance json tests."
echo "Also please have your server running and tunnel connected."
echo "Beginning distance automated testing."
file="distance_output.txt"
if [ -f $file ] ; then
    rm "$file"
fi
python3 distance_test_automator314.py > distance_output.txt
echo "Success."
echo "Results stored in distance_output.txt"
