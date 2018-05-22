from mongoengine import Document, fields
from passlib.hash import pbkdf2_sha256

class User(Document):
    firstName = fields.StringField(required=True)
    lastName = fields.StringField(required=True)

    email = fields.StringField(required=True, unique=True)
    password = fields.StringField(required=True)

    # ENUM("AVAILABLE", "BUSY")
    status = fields.StringField(required=True, default="BUSY") 

    # list of document IDs
    friends = fields.ListField(fields.StringField(), default=[])

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
