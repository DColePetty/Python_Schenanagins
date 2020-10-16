import subprocess
from subprocess import *
import requests

def parse_distance(string_input):
    test_case_data = string_input
    # now compare the distances arrays
    does_distance_exist = test_case_data.find("distances")
    if(does_distance_exist == -1):
        raise Exception("Test case does not have distances and cannot be automatically verified!")
    # otherwise it will just keep running
    #print("Distances exists in sent_data\n")
    distance_string = test_case_data[does_distance_exist::].strip()
    distance_string = distance_string[11:distance_string.find("]"):] + "]"
    distance_string = distance_string.strip()
    distances_list = distance_string.split(",")
    distances_ints = []
    #print(type(distances_list))
    for i in range(0, len(distances_list)):
        curr_str = str(distances_list[i].strip().strip("\n").strip().strip(" ").strip().strip("[").strip().strip("]").strip().strip(":").strip("[").strip(" ").strip())
        if( len(curr_str) == 0):
            #distances_ints.append(int(0)) # placeholder zero if someone put an extra comma as the schema is broken
            #raise Exception("Sorry, invalid scheme as empty object in distances. Extra ',' ?\n")
            pass
        else:
            try:
                distances_ints.append(int(curr_str.strip("[")))
            except Exception as e:
                raise Exception("Sorry, invalid scheme for int '" + curr_str + "' distance request\n " + str(e))
    #print("send_list: " + str(distances_list))
    return distances_ints

url = "localhost:8000/api/trip"
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
    recieved_data_from_server = parse_distance(recieved_data_from_server)

    if(test_case_data == recieved_data_from_server):
        print("Hooray test case succeeded " + request_file)
    else:
        if(len(test_case_data) != len(recieved_data_from_server)):
            print("nonequal lengths")
            print("request_distances_array: \n"  + str(test_case_data))
        print("recieved_distances_from_server: \n"  + str(recieved_data_from_server))
        print("test_case_data: \n"  + str(test_case_data))

'''
Process:
use curl to send the request_file data to the server
the curl will return into the recieved_data_from_server string the response from the server.
This response includes the new correctly calculated distances data.
Get the reponse code and check that to make sure it is 200
iterate through the current directory looking for trip-requests

'''

import os

# iterate over the files
for curr_file in os.listdir():
    #print("currentfile: " + curr_file)
    if("-trip.json" in curr_file):
        print("\nRunning test case: " + curr_file)
        try:
            run_test(curr_file)
        except Exception as e:
            print("Test case failed: " + curr_file + "\n" + str(e))
