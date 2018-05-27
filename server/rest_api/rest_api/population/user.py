import sys

sys.path.append('../user')
import models
User = models.User

# mongodb name
dbName = '24-seven-test'

# MongoDB connection
from mongoengine import connect
db = connect(dbName)

def populate_users():
    try:
        billy = User(
            firstName='billy',
            lastName='bob',
            email="billybob@gmail.com",
            password='password123',
        ).save()

        fred = User(
            firstName='freddy',
            lastName='kennedy',
            email='fredmyster@gmail.com',
            password='password123'
        ).save()


        kennny = User(
            firstName='kenny',
            lastName='louis',
            email='kenny123@gmail.com',
            password='password123'
        ).save()
    except:
        return False
    return True    

if __name__ == "__main__":
    print("Populating Users...")
    print("Success.") if populate_users() else print("Fail.")

    # print('dropping database...')
    # db.drop_database(dbName)
