"""

Name:Addison Reese
Date:10/5/25
Assignment:Module 6: Basic Document Store Creation Script, Querying Doc Store Database, and App Project
Due Date:10/5/25
About this project:This project creates, connects, and manipulates a MongoDB application
Assumptions: Created by Addison Reese under the instruction and with the help of Dr. Karen Works at FSU
"""
print("*********************************************")
print("USING transactions.json FROM sample_analytics")
print("*********************************************\n")
from pymongo import MongoClient
from datetime import datetime, timezone

def DisplaySpecificTransaction(client):
    userinput = input("Enter transaction ID: ")
    mydb = client["sample_analytics"]
    mycol = mydb["transactions"]
    print("limit rows")
    all_items = mycol.find({"transaction_count": userinput}, {"account_id": True, "transaction_count": True,
                                                        "bucket_start_date": True, "bucket_end_date": True})
    print("account_id")
    for a in all_items:
        print(str(a["account_id"]).ljust(30, ' ')[0:30], "\t\t", a["transaction_count"],
              "\t\t", a["bucket_start_date"], "\t\t", a["bucket_start_date"])



#validates and formats date for string
def GetValidDate(user_in):
    while True:
        user_input = input(user_in).strip()
        try:
            #format the data into standard date
            dt = datetime.strptime(user_input, "%Y-%m-%d")

            #convert to ISO 8601
            iso_date = dt.replace(tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+00:00"
            return iso_date
        except ValueError:
            print("Invalid date format.")

#validates transaction count for float
def GetValidCount():
    #prompt and read in transaction count as a float
    val = float(input("Enter in a transaction count "))
    while ((val<=0) or (val >120000)):
        #while val is invalid count

        # prompt and read in count
        val = float(input("Enter in a transaction count "))
    #return valid count
    return val

#validates unique transaction ID
def GetValidID(mycol):
    while True:
        account_id = input("Enter account ID: ").strip()

        #check if taken
        taken = mycol.find_one({"account_id": account_id})

        if taken:
            print(f"Invalid ID")
        elif account_id == "":
            print("Invalid ID")
        else:
            return account_id

def AddATransaction(client):
    #get id
    user = GetValidString()

    #get count
    post = GetValidCount()

    #get bucket start date
    start = GetValidDate("Enter in the start date")

    #get bucket end date
    end = GetValidDate("Enter in the end date")

    mydict = {
        "account_id": user,
        "transaction_count": post,
        "bucket_start_date": start,
        "bucket_end_date": end,
    }
    mydb = client["sample_analytics"]
    mycol = mydb["transactions"]
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


def print_Menu():
    #print menu
    print("A) Add a Transaction ")
    print("B) Display All Transactions ")
    print("C) Display a Specific Transaction ")

    # Quit
    print("Q) Quit")

def getMenuOption():
    #get menu option
    option = str(input("Please enter in your option..."))
    #convert to upper case
    option = option.upper()
    #while menu option not valid choice
    while ((option < "A") and (option > "C") and (option != "Q") ):
        #display menu
        print_Menu()
        # get menu option
        option = str(input("Please enter in your option..."))
        # convert to upper case
        option = option.upper()
    return option


def GetValidString():
    #prompt and read in string
    val = input("Enter in a value")
    #strip string of spaces
    val = val.strip()
    while (len(val)<=0):
        #while string empty

        # prompt and read in string
        val = input("Enter in a value")
        # strip string of spaces
        val = val.strip()
    #return valid string
    return val

def DisplayAllTransactions(client):
    ## sample_analytics database
    ## Does sample_analytics database exist

    mydb = client["sample_analytics"]
    mycol = mydb["transactions"]
    records = mycol.find()
    for r in records:
        print(r)

def mainApp(client):
    option =""

    #while user decides not to quit
    while (option != "Q"):
        #show menu
        print_Menu()
        #get option from user
        option = getMenuOption()

        if (option =="A"):
            #If option A chosen, add a transaction item
            AddATransaction(client)
        elif (option =="C"):
            #If option C chosen, display a specific transaction
            DisplaySpecificTransaction(client)
        elif (option =="B"):
            #If option B chosen, display all
            DisplayAllTransactions(client)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017/")
    mainApp(client)
    #close connection
    client.close()
