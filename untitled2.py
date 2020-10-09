# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:26:25 2020

@author: Mateusz
"""


import json

x='{"name":"John", "age":30, "city":"New York"}'

y=json.loads(x)

print(y["age"])