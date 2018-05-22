from rest_framework.decorators import api_view
from rest_framework.response import Response
from passlib.hash import pbkdf2_sha256
from ..user.models import User
import jwt

@api_view(['POST'])
def login(request):
    requestDict = request.data
    if ('email' in requestDict and 'password' in requestDict):
        email = requestDict['email']
        password = requestDict['password']
        try:
            user = User.objects.get(email=email)
            if (pbkdf2_sha256.verify(password, user.password)):
                # create and give token
                payload = user.toPayload()
                token = jwt.encode(payload, 'secret', algorithm='HS256')
                resp = {'token': token}
            else:
                 resp = {'err': 'Invalid email/password'}
        except:
            resp = {'err': 'Invalid email/password'}
    else:
        resp = {'err': 'Missing email or password'}
    return Response(resp)

@api_view(['POST'])
def register(request):
    requestDict = request.data
    if (validUserDetails(requestDict)):
        try:
            # save user
            user = User(
                firstName=requestDict['firstName'],
                lastName=requestDict['lastName'],
                email=requestDict['email'],
                password=requestDict['password'],
            ).save()
            
            # create and give token
            payload = user.toPayload()
            token = jwt.encode(payload, 'secret', algorithm='HS256')
            resp = {'token': token}
        except:
            resp = {'err': 'email is already registered'}
    else:
        resp = {'err': 'invalid user details'}
    return Response(resp)

def validUserDetails(givenDetails):
    validDetails = ['email', 'password', 'firstName', 'lastName']
    for detail in validDetails:
        if not (detail in givenDetails):
            return False
    return True
            
