# Automate your server testing!
## Steps to run!
### Pre-requisites 
 * SSH with tunnels to cs314 servers on campus and database respectively
 * Run your server on localhost as per usual
 * This server uses the url localhost:8000/api/trip or localhost:8000/api/distance respectively (otherwise you may change the url variable in the code)
### Next steps
1. download the testing files from github via:
  https://github.com/csucs314f20/students via Code button and download.
2. navigate to the sprint2/sprint3 directory which holds the jsons and copy the python and sh files for trip or distance to where respective jsons are located
3. run ./run_trip.sh or ./run_distance.sh respectively. 
  >You will see some requests scroll by, do not worry unless you receive an error.
4. open trip_output.txt or distance_output.txt in your preferred text editor.

Caveats:
 * This program will only run tests that have "trip-" or "-distance" in the name.
 * Trip test cases that do not have a "distances":  parameter in the json will be run and tested for pass/fail based on
response code only. Same for "distance" parameter in the distance tests.
 * I also misspelled recieved many many times in the codebase. I am a coder not an english major. 
