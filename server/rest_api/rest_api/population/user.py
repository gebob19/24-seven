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

        harold = User(
            firstName='harold',
            lastName='yutago',
            email='haroldinho@hotmail.com',
            password='password123'
        ).save()

    except:
        return False
    return True    

def populate_friends():
    try:
        users = User.objects
        for i in range(0, len(users) - 1):
            currentUser = users[i]
            if i == len(users) - 1:
                sendRequestTo = users[0]
            else:
                sendRequestTo = users[i+1]
            print(currentUser.firstName + ' -> ' + sendRequestTo.firstName)
            # friend request sent
            currentUser.sentFriendRequests.append(str(sendRequestTo.id))
            sendRequestTo.myFriendRequests.append(str(currentUser.id))
            currentUser.save(clean=False)
            sendRequestTo.save(clean=False)
    except:
        return False
    return True

def accept_requests():
    users = User.objects
    for i in range(0, len(users) - 1):
        currentUser = users[i]
        requestCount = 0
        print(currentUser.myFriendRequests)
        for request in currentUser.myFriendRequests:
            if requestCount % 2 == 0:
                friendRequester = User.objects.get(id=request)

                friendRequester.sentFriendRequests.remove(str(currentUser.id))
                currentUser.myFriendRequests.remove(str(friendRequester.id))

                friendRequester.friends.append(str(currentUser.id))
                currentUser.friends.append(str(friendRequester.id))

                currentUser.save(clean=False)
                friendRequester.save(clean=False)
            requestCount += 1
    return True

def drop():
    print('dropping database...')
    try:
        db.drop_database(dbName)
        print("Success.")
    except:
        print("Fail.")
        
def attempt(title, function):
    print(title)
    print("Success.") if function() else print("Fail.")

if __name__ == "__main__":
    if (len(sys.argv) > 1 and sys.argv[1] == 'drop'):
        drop()
    else:
        attempt("Populating Users...", populate_users)
        attempt("Populating Friends...", populate_friends)
        attempt("Accepting Friend Requests...", accept_requests)
