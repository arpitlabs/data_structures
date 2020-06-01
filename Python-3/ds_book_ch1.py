users_list = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#print(friendship_pairs)

friendships = {user["id"]: [] for user in users_list}

for x, y in friendship_pairs:
  friendships[x].append(y)
  friendships[y].append(x)

#print(friendships)

def get_number_of_freinds(user):
  user_id = user["id"]
  frields_ids = friendships[user_id]
  return len(frields_ids)

total_connections = sum(get_number_of_freinds(user) for user in users_list)
#print(total_connections)

number_of_friends_by_id = [(user["id"], get_number_of_freinds(user)) for user in users_list]
number_of_friends_by_id.sort(key=lambda i: i[1], reverse=True)
#print(number_of_friends_by_id)

from collections import Counter
def friends_of_friends(user):
  user_id = user["id"]
  fof = Counter(fof_id for friend_id in friendships[user_id]
  for fof_id in friendships[friend_id]
  if fof_id != user_id
  and fof_id not in friendships[user_id])
  return fof

#print(friends_of_friends(users_list[3]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
  alike = []
  for user_id, user_int in interests:
    if user_int == target_interest:
      alike.append(user_id)
  return alike

from collections import defaultdict
user_id_by_interest = defaultdict(list)
for user_id, user_int in interests:
  user_id_by_interest[user_id].append(user_int)

#print(user_id_by_interest)

interests_by_user_id = defaultdict(list)
for user_id, user_int in interests:
  interests_by_user_id[user_int].append(user_id)
print("--")
#print(interests_by_user_id)

def most_common_interests_with(user):
  user_id = user["id"]
  return Counter(interested_user_id
  for interest in user_id_by_interest[user_id]
  for interested_user_id in interests_by_user_id[interest]
  if interested_user_id != user_id)

print(most_common_interests_with(users_list[3]))