# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
    {"id": 9, "name": "Klein"},
    ]

print(users)


friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

print(friendship_pairs)

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}


# ANd loop over the friendship pairs to poplulate it:
for i, j in friendship_pairs:
    friendships[i].append(j) # Add j as a friend of user i
    friendships[j].append(i) # Add i as a friend of user j
    
    
def number_of_friends(user):
    """How many freinds does_user_have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

# Create a list (user_id, number_of_friends)
num_of_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_of_friends_by_id.sort(                                      # Sort the list
    key=lambda id_and_friends: id_and_friends[1],               # by num_friends
    reverse=True)                                               # largest to smallest


def foaf_ids(user):
    """foaf is short for "friend of friend """
    foaf_id = [foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]]
    return foaf_id

print(users[0])

print(friendships[0])


            