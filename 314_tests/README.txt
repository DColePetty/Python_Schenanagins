Follow these steps to use the trip_test_automator314.py to run trip test cases against you server.

1. SSH with tunnels to cs314 servers on campus and database respectively
2. Run your server on localhost as per usual
> This server uses the url localhost:8000/api/trip, if this does not work, change the 'url' variable in the code
3. download the testing files from github via:
https://github.com/csucs314f20/students via Code button and download. 
4. navigate to the sprint3 directory which holds the trip tests and copy the trip_test_automator314.py inside that directory
5. run python3 trip_test_automator314.py > output.txt
> You will see some requests scroll by, do not worry unless you receive an error. 
6. open output.txt in your preferred text editor. 

Caveats: 
This program will only run tests that have "trip-" in the name. 
Trip test cases that do not have a "distances":  parameter in the json will be run and tested for pass/fail based on 
response code only. 
