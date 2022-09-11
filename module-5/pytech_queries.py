from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.14fftaj.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

Bill = students.find_one({"student_id": "1008"})

print("  Student ID: " + Bill["student_id"] + "\n  First Name: " + Bill["first_name"] + "\n  Last Name: " + Bill["last_name"] + "\n")
