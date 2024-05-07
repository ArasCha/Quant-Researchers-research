from pymongo import MongoClient
import json

client = MongoClient("127.0.0.1", 27017)

db = client.qr2


def insert_data(data:dict):

	file_path = 'data.json'

	with open(file_path, 'r+', encoding="utf-8") as file:
		try:
			existing_data = json.load(file)
		except json.JSONDecodeError:
			existing_data = []

		existing_data.append(data)
		file.seek(0)
		json.dump(existing_data, file, indent=4, ensure_ascii=False)
		file.truncate()
