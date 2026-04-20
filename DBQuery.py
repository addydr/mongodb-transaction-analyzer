"""

Name:Addison Reese
Date:10/5/25
Assignment:Module 6: Basic Document Store Creation Script, Querying Doc Store Database, and App Project
Due Date:10/5/25
About this project:This project creates, connects, and manipulates a MongoDB application
Assumptions: Created by Addison Reese under the instruction and with the help of Dr. Karen Works at FSU
"""

from pymongo import MongoClient
print("*********************************************")
print("USING transactions.json FROM sample_analytics")
print("*********************************************\n")
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# Provide the mongodb atlas url to connect python to mongodb using pymongo
#CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase
client = MongoClient("mongodb://localhost:27017/")

## drop database
#client.drop_database("sample_analytics")

mydb = client["sample_analytics"]
mycol = mydb["transactions"]

#this function came from FindShowSubItems.py by Dr. Works, explained in Find examples.
def DescribeKeyValues(X,Level):
    for key_k in X.keys():
        for i in range(Level):
            print("\t\t\t",end="")
        print(key_k, "\t\t\t", type(X[key_k]), "\t\t\t", X[key_k])
        if (isinstance(X[key_k],dict) or (isinstance(X[key_k],list) and isinstance(X[key_k][0],dict))):
            for i in range(Level):
                print("\t\t\t", end="")
            print("Sub Object:")
            if (isinstance(X[key_k], dict)):
                DescribeKeyValues(X[key_k], Level+1)
            else:
                DescribeKeyValues(X[key_k][0], Level+1)

one_item = mycol.find_one()

### call function to display key info
DescribeKeyValues(one_item,0)



### Limit attributes returned
print("***************")
print("limit attributes")
all_items = mycol.find({},{"account_id":True,"transaction_count":True,"bucket_start_date":True,
                           "bucket_end_date":True})
print("account_id")
for a in all_items:
    print(str(a["account_id"]).ljust(30,' ')[0:30],"\t\t",a["transaction_count"],
          "\t\t",a["bucket_start_date"], "\t\t",a["bucket_start_date"])



### sort ascending and descending
print("***************")
print("sort ascending and descending")
all_items = mycol.find({},{"account_id":True,"transaction_count":True}).sort((("account_id",-1),
                                                                             ("transaction_count",1)))
print("account_id")
for a in all_items:
    print(str(a["account_id"]).ljust(30,' ')[0:30],"\t\t",a["transaction_count"])



### limit return values/rows
print("***************")
print("limit rows")
all_items = mycol.find({"transaction_count": 652},{"account_id":True,"transaction_count":True,
                                                   "bucket_start_date":True, "bucket_end_date":True})
print("account_id")
for a in all_items:
    print(str(a["account_id"]).ljust(30,' ')[0:30],"\t\t",a["transaction_count"],
          "\t\t",a["bucket_start_date"], "\t\t",a["bucket_start_date"])



### limit rows and columns
print("***************")
print("limit rows and columns")
all_items = mycol.find({"transaction_count": 652},{"account_id":True,"transaction_count":True,
                                                   "bucket_start_date":True})
print("account_id")
for a in all_items:
    print(str(a["account_id"]).ljust(30,' ')[0:30],"\t\t",a["transaction_count"],
          "\t\t",a["bucket_start_date"])



### sort by one
print("***************")
print("sort by one")
all_items = (mycol.find({"transaction_count": {"$lt" :700}},{"account_id":True,"transaction_count":True})
             .sort("transaction_count",-1))
print("account_id")
for a in all_items:
    print(str(a["account_id"]).ljust(30,' ')[0:30],"\t\t",a["transaction_count"])

client.close()
print("Disconnected from MongoDB")