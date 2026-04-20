"""

Name:Addison Reese
Date:10/5/25
Assignment:Module 6: Basic Document Store Creation Script, Querying Doc Store Database, and App Project
Due Date:10/5/25
About this project:This project creates, connects, and manipulates a MongoDB application
Assumptions: Created by Addison Reese under the instruction and with the help of Dr. Karen Works at FSU
"""

from pymongo import MongoClient
from datetime import datetime, timezone
print("*********************************************")
print("USING transactions.json FROM sample_analytics")
print("*********************************************\n")
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# Provide the mongodb atlas url to connect python to mongodb using pymongo
#CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase
client = MongoClient("mongodb://localhost:27017/")

## drop database
client.drop_database("sample_analytics")

mydb = client["sample_analytics"]
mycol = mydb["transactions"]

#This dictionary mirrors what is already present in the transactions database
mydict = {
"date": "20025-10-5T00:00:00.000+00:00",
"amount": "37",
"transaction_code": "nontradDBproj",
"symbol": "amg",
"price": 8.9,
"total": 10
}

#x = mycol.insert_one(mydict)
#print(client.list_database_names())


##insert many
ycol = mydb["customers"]

#ten items, unique ID, whole number, and whole and real number inside dictionary
mylist = [
    { "account_id": "191983839", "transaction_count": 652, "bucket_start_date": "2022-05-13T00:00:00.000+00:00",
    "bucket_end_date": "2023-12-27T00:00:00.000+00:00", "transactions": mydict},

    { "account_id": "204882912", "transaction_count": 418, "bucket_start_date": "2021-03-02T00:00:00.000+00:00",
      "bucket_end_date": "2023-02-11T00:00:00.000+00:00", "transactions": mydict },

    { "account_id": "177492001", "transaction_count": 973, "bucket_start_date": "2020-09-15T00:00:00.000+00:00",
      "bucket_end_date": "2024-01-03T00:00:00.000+00:00", "transactions": mydict },

    { "account_id": "199820776", "transaction_count": 211, "bucket_start_date": "2022-01-10T00:00:00.000+00:00",
      "bucket_end_date": "2023-08-14T00:00:00.000+00:00", "transactions": mydict },

    { "account_id": "185678422", "transaction_count": 540, "bucket_start_date": "2021-07-05T00:00:00.000+00:00",
      "bucket_end_date": "2024-03-21T00:00:00.000+00:00", "transactions": mydict },

    { "account_id": "200115334", "transaction_count": 864, "bucket_start_date": "2022-10-23T00:00:00.000+00:00",
      "bucket_end_date": "2024-02-18T00:00:00.000+00:00", "transactions": mydict },

    { "account_id": "178943555", "transaction_count": 327, "bucket_start_date": "2021-12-30T00:00:00.000+00:00",
      "bucket_end_date": "2023-07-11T00:00:00.000+00:00", "transactions": mydict },

    { "account_id": "196412980", "transaction_count": 745, "bucket_start_date": "2020-06-09T00:00:00.000+00:00",
      "bucket_end_date": "2023-09-19T00:00:00.000+00:00", "transactions": mydict },

    { "account_id": "209887641", "transaction_count": 589, "bucket_start_date": "2021-11-25T00:00:00.000+00:00",
      "bucket_end_date": "2023-12-01T00:00:00.000+00:00", "transactions": mydict },

    { "account_id": "175554229", "transaction_count": 680, "bucket_start_date": "2022-03-18T00:00:00.000+00:00",
      "bucket_end_date": "2024-04-07T00:00:00.000+00:00", "transactions": mydict }
]


x=mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)

#display with find
records = mycol.find()
for r in records:
    print(r)


#close connection
client.close()
