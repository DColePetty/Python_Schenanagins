# start class to hold service objects
class Service:
    # variables - do not declare here will be class variables
    # type = ""; # tcp/udp/other
    # port = 0 # 1-65553 ?
    # count = 0 # number of occurences

    def __init__(self, itype, iport, icount):
        self.type = itype
        self.port = iport
        self.count = icount
    def byPort(self, otherService):
        returnint( otherService.port) <= int(self.port) # 0 or 1 not great sorting but ok
    def byCount(self, otherService):
        return int(otherService.count) <= int(self.count) # 0 or 1 not great sorting but ok
    def toString(self):
        return str(self.type) + str(self.port) + " with " + str(self.count) + " connections\n"
    def toCSV(self):
        return str(self.type) + "," +  str(self.port) + "," + str(self.count) + "\n"

# meant to take HTML inner object from firemon's serives portion of the html reports
def populate(filename, sort_count_or_port, output_file_name, head_value = 5):
    my_file = open(filename).readlines()
    items_list = []
    curr_string = ""
    for line in my_file:
        line = line.strip(" ")
        if "</li>" in line:
            curr_string = curr_string.replace("<li>", "")
            curr_string = curr_string.replace("<span>", "")
            curr_string = curr_string.replace("</span>", "")
            curr_string = curr_string.replace("</small>", "")
            curr_string = curr_string.replace("<small>", "")
            items_list.append(curr_string)
            curr_string = ""
        else:
            curr_string += str(line.strip(" ").strip(",").strip("\n"))
    print("Read document into memory: " + str(filename) + " \n")
    services_list = []
    for entry in items_list:
        if "udp" in entry or "tcp" in entry or "other" in entry:
            #new_line = entry.strip("</span>").strip("<span>").strip("<\/span>").strip("<small>").strip("<\/small>").strip("\n").strip("i><span>").strip("<\/span><small>").strip("<\/span><small>")
            new_line = entry.strip("span").strip("small").strip("<").strip("li>").strip("\\").strip("\/")
            services_list.append(new_line)
    print("Stripping unncessary data. \n")
    #objectize
    services_objects = []
    for i in range(0, len(services_list)):
            current_object_string = services_list[i].replace("(", "_").replace(")", "").replace(",", "").replace("/", "_").split("_")
            new_services_object = Service(current_object_string[0], current_object_string[1], current_object_string[2])
            if isinstance(new_services_object, Service):
                services_objects.append(new_services_object)
    print("Created respective service objects. \n")
    print("Begun sorting based on __ " + str(sort_count_or_port) + "__ of service objects. \n")
    # sort list on service count
    for i in range(0, len(services_objects)):
        for j in range(0, len(services_objects)):
            if(services_objects[i] == services_objects[j] or i == j):
                continue
            else:
                if not isinstance(services_objects[i], Service):
                    print("NOT: " + str(current))
                if isinstance(services_objects[i], Service)  and isinstance(services_objects[j], Service):
                    if(sort_count_or_port.lower() == "count"):
                        if( services_objects[i].byCount(services_objects[j]) ):
                            temp = services_objects[i]
                            services_objects[i] = services_objects[j]
                            services_objects[j] = temp
                    if(sort_count_or_port.lower() == "port"):
                        if( services_objects[i].byPort(services_objects[j]) ):
                            temp = services_objects[i]
                            services_objects[i] = services_objects[j]
                            services_objects[j] = temp
    print("Completed sorting based on __ " + str(sort_count_or_port) + "__ of service objects. \n")
    # write to file
    print("Writing to file: "   + output_file_name + "\n")
    newfile = open("sorted_services.csv", "w+")
    for i in services_objects:
        newfile.write(i.toCSV())
    newfile.close()
    print("Done. \n")
    #
    for i in range(0, head_value):
        if( i < len(services_objects)):
            print(services_objects[i].toCSV().replace("\n", ""))
    print("\n")

# ____ begin main
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("services_raw_inner_html_file", help="<inspect element for firemon services html report and right click copy inner html>")
parser.add_argument("head_value", help="<output for number of values to be read from top of sort. Default 5>")
args = parser.parse_args()
#Get data
filename = args.services_raw_inner_html_file
head_value = int(args.head_value)
#filename = "all_services.txt" # manual override
populate(filename, "count", "sorted_services_" + filename+ ".csv", head_value)
