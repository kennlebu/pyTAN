import pymongo
import random

# Variables
LOWER_LIMIT = 100000
UPPER_LIMIT = 10000000

# Connection to MongoDB
def db_connect(name):
    try:
        conn = pymongo.MongoClient()        
        # Define DB to store the results
        db = conn.tans
        posts = db.tan_transactions # collection to store the results
        print("Connected sucessfully!")

        generateTan(name, posts)

    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB:", e)

    conn


# Generating, saving and printing the TAN
def generateTan(name, p):
    tan = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    if not tanExists(tan, p):
        # Insert the TAN to the DB
        data = {"tan_no":tan, "owner_name":name}
        p.insert(data)

        # Print the TAN
        print("Your TAN is", tan)
    else:
        generateTan(name, posts)


# Checking whether the TAN already exists in the DB
def tanExists(tan, collection):
    result = {}

    search = {"tan_no":0}
    search['tan_no'] = tan

    result = collection.find_one(search)

    if result is not None:
        if len(result) >= 1:
            return True
    else: return False


# MAIN
def main():
    name = input("Hello. What is your name? ")
    db_connect(name)


if __name__ == "__main__": main()
