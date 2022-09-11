from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.14fftaj.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

Will = {
    "student_id": "1007",
    "first_name": "Will",
    "last_name": "Ferrell",
    "enrollments": {
        "radiology": {
            "term": "Spring",
            "gpa": "3.56",
            "start_date": "02/31/24",
            "end_date": "05/31/24",
            "courses": {
                "balistics": {
                    "id": "234635654",
                    "description": "a fun time for all",
                    "instructor": "Mr. Stoke",
                    "grade": "A"
                },
                "microwaves": {
                    "id": "97468456765473",
                    "description": "cooking and physics",
                    "instructor": "Mrs. Phylmanine",
                    "grade": "A+"
                }
            }
        },
        "magnetism": {
            "term": "Fall",
            "gpa": "3.96",
            "start_date": "11/14/24",
            "end_date": "01/03/25",
            "courses": {
                "compasses": {
                    "id": "8478465325",
                    "description": "learn to direct",
                    "instructor": "Prof. Lestory",
                    "grade": "A-"
                },
                "electromagnets": {
                    "id": "3276757",
                    "description": "magnets that turn off",
                    "instructor": "Ms. Stephanie",
                    "grade": "B"
                }
            }
        }
    }
}
Bill = {
    "student_id": "1008",
    "first_name": "Bill",
    "last_name": "Ferrell",
    "enrollments": {
        "Exotic": {
            "term": "Spring",
            "gpa": "3.75",
            "start_date": "02/31/24",
            "end_date": "05/31/24",
            "courses": {
                "Marmalade": {
                    "id": "73257625",
                    "description": "Elementary",
                    "instructor": "Ms. Bartlow",
                    "grade": "A+"
                },
                "Nanowaves": {
                    "id": "268475241",
                    "description": "These are even smaller",
                    "instructor": "Mrs. Phylmandy",
                    "grade": "C-"
                }
            }
        },
        "Impressions": {
            "term": "Fall",
            "gpa": "3.43",
            "start_date": "11/14/24",
            "end_date": "01/03/25",
            "courses": {
                "Meow": {
                    "id": "2457345654868",
                    "description": "How to viciously meow",
                    "instructor": "Mr. Grenny",
                    "grade": "A"
                },
                "Barking": {
                    "id": "376846797564",
                    "description": "Make those same sounds",
                    "instructor": "Miss Barbahbo",
                    "grade": "B-"
                }
            }
        }
    }
}
Phil = {
    "student_id": "1009",
    "first_name": "Phil",
    "last_name": "Ferrell",
    "enrollments": {
        "Moodiness": {
            "term": "Spring",
            "gpa": "3.74",
            "start_date": "02/31/24",
            "end_date": "05/31/24",
            "courses": {
                "Brooding": {
                    "id": "435967352454351",
                    "description": "Who should do it, and who shouldn't?",
                    "instructor": "Miss Melds",
                    "grade": "A+"
                },
                "Wallowing": {
                    "id": "5908986364652",
                    "description": "The Art of Wallowing",
                    "instructor": "Ms. Tarm",
                    "grade": "C+"
                }
            }
        },
        "Misc": {
            "term": "Fall",
            "gpa": "3.85",
            "start_date": "11/14/24",
            "end_date": "01/03/25",
            "courses": {
                "Willows": {
                    "id": "4457365",
                    "description": "Dripping trees",
                    "instructor": "Mrs. Mella",
                    "grade": "B-"
                },
                "Exotic faiths": {
                    "id": "376354634",
                    "description": "Marshalism",
                    "instructor": "Mr. Brock",
                    "grade": "B+"
                }
            }
        }
    }
}
 
students = db.students

Will_student_id = students.insert_one(Will).inserted_id

Bill_student_id = students.insert_one(Bill).inserted_id

Phil_student_id = students.insert_one(Phil).inserted_id
