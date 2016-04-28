#!/usr/bin/env python2.7


import json
import os


fp = open("./nodes.json", "r")

JOURNEY = json.load(fp)
fp.close()
more = "1"
inner_dict = {}
NODES = {}
print JOURNEY.keys()
#JOURNEY = {}
while(more != "0"):
    inner_dict.clear()
    NODES.clear()
    node_name = raw_input("Please enter the name of this node:  \n")
    inner_dict_name_1 = raw_input("Please enter the name of the first room: \n")
    inner_dict_name_2 = raw_input("Please enter the name of the second room: \n")
    
    inner_dict[inner_dict_name_1] = raw_input("Please enter the text of the first room:\n")
    inner_dict[inner_dict_name_2] = raw_input("Please enter the text of the second room:\n")
    
    NODES["text"] = raw_input("Please enter the text of the main node: \n")
    NODES["branches"] = inner_dict
    JOURNEY[node_name] = NODES
    
    with open('nodes.json.new', 'w') as stream:
            json.dump(JOURNEY, stream)
            os.rename('nodes.json.new', 'nodes.json')
    more = raw_input ( "Enter 1 to enter another node, 0 to exit: ")


