class FriendController:
    def __init__(self, user):
        self.user = user
        self.userID = str(user.id)

    def sendFriendRequest(self, friend):
        friendID = str(friend.id)

        self.user.sentFriendRequests.append(friendID)
        friend.myFriendRequests.append(self.userID)

        friend.save()
        self.user.save()
    
    def acceptFriendRequest(self, friend):
        friendID = str(friend.id)

        self.user.friends.append(friendID)
        friend.friends.append(self.userID)

        self.user.myFriendRequests.remove(friendID)
        friend.sentFriendRequests.remove(self.userID)

        friend.save()
        self.user.save()