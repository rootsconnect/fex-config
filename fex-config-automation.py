# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:20:07 2016

@author: netwhitebread
"""
#opening input file
file = open('fex.txt', 'r')

#iterating through input file line by line and split/save details into variables
for line in (x.rstrip ('\n') for x in file):
    current_line = line.split(",")
    
    fex_number = current_line[0]
    fex_port1 = current_line[1]
    fex_port2 = current_line[2]
    """
    print(fex_number)
    print(fex_port1)
    print(fex_port2)
    """
    #generating & printing config for each line with above generated variables of input file
    print("fex {}".format(str(fex_number)))
    print("  pinning max-links 1")
    print("  description FEX{}".format(str(fex_number)), "\n")

    print("interface port-channel{}".format(str(fex_number)))
    print("  description FEX{}".format(str(fex_number)))
    print("  switchport mode fex-fabric")  
    print("  fex associate {}".format(str(fex_number)))
    print("  vpc {}".format(str(fex_number)), "\n")
  
    print("interface Ethernet{}".format(fex_port1))
    print("  description FEX{}".format(str(fex_number)))
    print("  switchport mode fex-fabric") 
    print("  fex associate {}".format(str(fex_number)))
    print("  channel-group {}".format(str(fex_number)), "\n")

    print("interface Ethernet{}".format(fex_port2))
    print("  description FEX{}".format(str(fex_number)))
    print("  switchport mode fex-fabric") 
    print("  fex associate {}".format(str(fex_number)))
    print("  channel-group {}".format(str(fex_number)), "\n\n")

#closing input file
file.close()