# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 19:32:53 2020

@author: Mateusz
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:57:33 2020

@author: Mateusz
"""


import socket
import sys
import json





# a Python object (dict):
x = '{"user":"Johpn","admin":"2ppp3","age":"234","name":"2.34"}'


# convert into JSON:
message = json.dumps(x)

    

    
y=json.loads(x)
y["user"]="mark"
print(y["user"])
   

