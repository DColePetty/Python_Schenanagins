import subprocess
from subprocess import *
import requests
import json

def parse_distance(string_input):
    does_distance_exist = string_input.find("distance")
    if(does_distance_exist == -1):
        raise Exception("Test case does not have distances and cannot be automatically verified!")
    else:
        dist_json = json.loads(string_input)
        distance = str(dist_json["distance"]).strip()
    return distance

url = "localhost:8000/api/distance"
#filename = "trip_json1.json"
def run_test(file_name):
    request_file = file_name
    recieved_data_from_server = subprocess.check_output(["curl","-d", str("@" + request_file), url]).decode("utf-8")
    ''' response code handling '''
    data1 = open(request_file).read()
    response = requests.post('http://' + str(url), data=data1)
    print("Response code: " + str(response.status_code))
    if( int(response.status_code) != 200):
        raise("Invalid response code: test failed")

    test_case_data_file = open(request_file, "r")
    test_case_data = test_case_data_file.read()

    test_case_data = (parse_distance(test_case_data))
    recieved_data_from_server = (parse_distance(recieved_data_from_server))

    if(test_case_data == recieved_data_from_server):
        print("Hooray test case succeeded " + request_file)
    else:
        if(test_case_data != recieved_data_from_server):
            print("recieved_distances_from_server: \n"  + str(recieved_data_from_server))
            print("test_case_data: \n"  + str(test_case_data))

import os

# begin main
# iterate over the files
for curr_file in os.listdir():
    #print("currentfile: " + curr_file)
    if("-distance.json" in curr_file):
        print("\nRunning test case: " + curr_file)
        try:
            run_test(curr_file)
        except Exception as e:
            print("Test case failed: " + curr_file + "\n" + str(e))
