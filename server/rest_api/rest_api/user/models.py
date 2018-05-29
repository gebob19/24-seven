from mongoengine import Document, fields
from passlib.hash import pbkdf2_sha256
#from ..controllers.friendController import FriendController

class User(Document):
    firstName = fields.StringField(required=True)
    lastName = fields.StringField(required=True)

    email = fields.StringField(required=True, unique=True)
    password = fields.StringField(required=True)

    # ENUM("AVAILABLE", "BUSY")
    status = fields.StringField(required=True, default="BUSY") 

    # list of document IDs
    friends = fields.ListField(fields.StringField(), default=[])
    myFriendRequests = fields.ListField(fields.StringField(), default=[])
    sentFriendRequests = fields.ListField(fields.StringField(), default=[])

    def clean(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def toPayload(self):
        return {
            'id': str(self.id),
        }
    
    def toQuickView(self):
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'status': self.status,
            'id': str(self.id)
        }
    
    def canSendFriendRequest(self, recipient):
        alreadyFriends = str(self.id) in recipient.friends
        requestAlreadySent = str(self.id) in recipient.myFriendRequests

        return not alreadyFriends and not requestAlreadySent
    
    def canAcceptFriendRequest(self, recipient):
        return str(self.id) in recipient.sentFriendRequests

    def getFriendController(self):
        return FriendController(self)


        
