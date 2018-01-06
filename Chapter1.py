# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 09:50:04 2018

@author: ericn
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:10:15 2018

@author: ericn
"""
from __future__ import division
import numpy as np
from matplotlib.pyplot import *



users = [ 
         {"id": 0, "name": "Hero"},
         {"id": 1, "name": "Hero"},
         {"id": 2, "name": "Hero"},
         {"id": 3, "name": "Hero"},
         {"id": 4, "name": "Hero"},
         {"id": 5, "name": "Hero"},
         {"id": 6, "name": "Hero"},
         {"id": 7, "name": "Hero"},
         {"id": 8, "name": "Hero"},
         {"id": 9, "name": "Hero"}
        ]

friendships =[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
              (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

for user in users:
    user["friends"] = []
    
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])
    
def number_of_friends(user):
    #"""How many friends does _user_ have?"""
    return len(user["friends"])

total_connections = sum(number_of_friends(user) 
    for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(users["id"], number_of_friends(user))
    for user in users]

sorted(num_friends_by_id, 
       key=lambda (user_id, num_friends): num_friends,
       reverse=True)

