#!/usr/bin/env python2.7


import json
import os


#/fp = open("./nodes.json", "wr")

#NODES = json.load(fp)
more = True
inner_dict = {}
NODES = {}
while(more):
    inner_dict.clear()
    node_name = raw_input("Please enter the name of this node:  \n")
    inner_dict_name_1 = raw_input("Please enter the name of the first room: \n")
    inner_dict_name_2 = raw_input("Please enter the name of the second room: \n")
    
    inner_dict[inner_dict_name_1] = raw_input("Please enter the text of the first room:\n")
    inner_dict[inner_dict_name_2] = raw_input("Please enter the text of the second room:\n")
    
    NODES["name"] = raw_input("Please enter the text of the main node: \n")
    NODES["branches"] = inner_dict
    
    with open('nodes.json.new', 'w') as stream:
            json.dump(NODES, stream)
            os.rename('nodes.json.new', 'nodes.json')
    more = raw_input ( "Enter 1 to enter another node, 0 to exit")


