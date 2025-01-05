from pymongo import MongoClient
import json

client = MongoClient("127.0.0.1", 27017)

db = client.qr2

file_path ='data.json'


def insert_data(data:dict):

	with open(file_path, 'r+', encoding="utf-8") as file:
		try:
			existing_data = json.load(file)
		except json.JSONDecodeError:
			existing_data = []

		existing_data.append(data)
		file.seek(0)
		json.dump(existing_data, file, indent=4, ensure_ascii=False)
		file.truncate()


def get_total_data():

	existing_data = {}
	with open(file_path, 'r', encoding="utf-8") as file:
		existing_data = json.load(file)

	return existing_data


def profile_not_in_db(profile: dict) -> bool:

	data = get_total_data()
	for profile_db in data:
		if profile_db["profile_url"] == profile["url"]:
			return False
	
	return True

