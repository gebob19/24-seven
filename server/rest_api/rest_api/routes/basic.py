from rest_framework.decorators import api_view
from rest_framework.response import Response
from passlib.hash import pbkdf2_sha256
from ..user.models import User
import jwt

@api_view(['POST'])
def login(request):
    validation = validLoginRequest(request)
    if (validation[0]):
        user = validation[1]
        token = getToken(user)
        resp = {'token': token}
    else:
        resp = {'err': validation[1]}

    return Response(resp)

@api_view(['POST'])
def register(request):
    validation = validRegisterRequest(request)
    if (validation[0]):
        parameters = request.data
        user = User(
            firstName=parameters['firstName'],
            lastName=parameters['lastName'],
            email=parameters['email'],
            password=parameters['password'],
        ).save()

        token = getToken(user)
        resp = {'token': token}
    else:
        resp = {'err': validation[1]}
    return Response(resp)    

def validRegisterRequest(request):
    requestDict = request.data

    # validate parameters
    validDetails = ['email', 'password', 'firstName', 'lastName']
    for detail in validDetails:
        if not (detail in requestDict):
            return [False, "missing parameters"]

    # validate unique email
    if (User.objects(email=requestDict['email']).count() == 0):
        return [True, ""]
    else:
        return [False, "email already registered"]

def validLoginRequest(request):
    requestDict = request.data
    if ('email' in requestDict and 'password' in requestDict):
        email = requestDict['email']
        password = requestDict['password']
        try:
            user = User.objects.get(email=email)
        except:
            return [False, 'unable to find user']

        if (pbkdf2_sha256.verify(password, user.password)):
            return [True, user]
        else:
            return [False, 'invalid password']
    else:
        return [False, 'missing parameters']

def getToken(user):
    payload = user.toPayload()
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token
            
