from __future__ import division

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:10:15 2018
@author: ericn
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter, defaultdict # not loaded by default
from Chapter1Functions import getNumFriends, number_of_friends, \
 friends_of_friend_ids_bad, friends_of_friend_ids, \
 most_common_interests_with, \
 data_scientists_who_like

users = [ 
         {"id": 0, "name": "Hero"},
         {"id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"},
         {"id": 4, "name": "Thor"},
         {"id": 5, "name": "Clive"},
         {"id": 6, "name": "Hicks"},
         {"id": 7, "name": "Devin"},
         {"id": 8, "name": "Kate"},
         {"id": 9, "name": "Klein"}
        ]

friendships =[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
              (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

def tenure_bucket(tenure):
    if tenure < 2: return "less than two"
    elif tenure < 5: return "between two and five"
    else: return "more than five"
    
def make_chart_salaries_by_tenure():
    tenures = [tenure for salary, tenure in salaries_and_tenures]
    salaries = [salary for salary, tenure in salaries_and_tenures]
    plt.scatter(tenures, salaries)
    plt.xlabel("Years Experience")
    plt.ylabel("Salary")
    plt.show()
    
for user in users:
    user["friends"] = []
    
for i, ji in friendships:
    users[i]["friends"].append(users[ji])
    users[ji]["friends"].append(users[i])
    

total_connections = sum(number_of_friends(user) 
    for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], number_of_friends(user))
    for user in users]


for person in num_friends_by_id:
    print(getNumFriends(person))
    

num_friends_by_id1 = sorted(num_friends_by_id,
             key= getNumFriends, # by number of friends
             reverse=True) 

print()

for person in num_friends_by_id1:
    print(getNumFriends(person))
    
print()
    
[print(friends_of_friend_ids_bad(user))
    for user in users]

print() 
#print("enter the number of user you want to see the efriend tree:")
#f = int(input())

#print (users[f])   

print( friends_of_friend_ids(users[3])) # Counter({0: 2, 5: 1})
   
print()       
print(data_scientists_who_like("regression"))

print()
print(most_common_interests_with(users[4]))

print()
###########################
#                         #
# SALARIES AND EXPERIENCE #
#                         #
###########################
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
    }

print()
print(average_salary_by_tenure)

tenure_bucket_dict  = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    tenure_bucket_dict[tenure_bucket(tenure)].append(salary)

average_salary_by_bucket = {
        bucket : sum(salaries) / len(salaries)
        for bucket, salaries in tenure_bucket_dict.items()
        }

print()
print(average_salary_by_bucket)

bucket_list = list(average_salary_by_bucket.items())

bucket_list.sort(key=lambda x : x[1], reverse=True)
    
print()
print(bucket_list)

bucket_max = 0
bucket_min = 10000000

for i in range(len(bucket_list)-1):
    
    if bucket_max < bucket_list[i][1]:
        bucket_max = bucket_list[i][1]
        bucket_max_index = i
        
    if bucket_min > bucket_list[i][1]:
        bucket_min = bucket_list[i][1]
        bucket_min_index = i
        
    if bucket_max < bucket_list[i+1][1]:
        bucket_max = bucket_list[i+1][1]
        bucket_max_index = i+1
        
    if bucket_min > bucket_list[i+1][1]:
        bucket_min = bucket_list[i+1][1]
        bucket_min_index = i+1
        
        
    val = (bucket_list[i][1] - bucket_list[i+1][1])/bucket_list[i+1][1]
    print(r"group ", bucket_list[i][0], " has a ", val*100, r"% differnce from ", \
          bucket_list[i+1][0])

print(bucket_list[bucket_max_index][0], r"group has:", bucket_list[bucket_max_index][1])
print(bucket_list[bucket_min_index][0], r"group has:", bucket_list[bucket_min_index][1])
print(r"Max group is: ", (bucket_list[bucket_max_index][1] - bucket_list[bucket_min_index][1])/bucket_list[bucket_min_index][1], " percent greater")




print()