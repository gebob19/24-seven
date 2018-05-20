from mongoengine import Document, fields


class User(Document):
    firstName = fields.StringField(required=True)
    lastName = fields.StringField(required=True)

    email = fields.StringField(required=True, unique=True)
    password = fields.StringField(required=True)

    # ENUM("AVAILABLE", "BUSY")
    status = fields.StringField(required=True, default="BUSY") 

    # list of document IDs
    friends = fields.ListField(fields.StringField(), default=[])

    # def clean(self):
        # self.password = pbkdf2_sha256.hash(self.password)
