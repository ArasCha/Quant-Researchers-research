from pymongo.mongo_client import MongoClient
from dotenv import dotenv_values


MONGO_URI = dotenv_values(".env")["MONGO_URI"]
client = MongoClient(MONGO_URI)


db = client.linkedin_users
profiles = db.get_collection("profiles")
index = db.get_collection("index")

local_list_of_users_id = []




def insert_profile(profile_data:dict):

	profiles.insert_one(profile_data)
	local_list_of_users_id.append(profile_data["profile_id"])


def get_list_of_users_id():

	global local_list_of_users_id
	if not local_list_of_users_id:
		cursor = profiles.find({}, {"profile_id": 1, "_id": 0})
		local_list_of_users_id = [profile["profile_id"] for profile in cursor]
	
	return local_list_of_users_id


def update_index(new_index: int):
	result = index.update_one({}, {"$set": {"value": new_index}})

def get_index() -> int:
	"""
	Function that returns the root profile index in db
	"""
	return index.find_one({})["value"]

