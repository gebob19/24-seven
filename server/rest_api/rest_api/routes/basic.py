from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..user.models import User

@api_view(['POST'])
def login(request):
    requestDict = request.data
    if ('email' in requestDict and 'password' in requestDict):
        try:
            user = User.objects.get(email=requestDict['email'])
            resp = {'message': 'hello world'}
        except:
            resp = {'err': 'Invalid email/password'}
    else:
        resp = {'err': 'missing email or password'}
    return Response(resp)

@api_view(['POST'])
def register(request):
    requestDict = request.data
    if (validUserDetails(requestDict)):
        try:
            User(
                firstName=requestDict['firstName'],
                lastName=requestDict['lastName'],
                email=requestDict['email'],
                password=requestDict['password'],
            ).save()
            resp = {'message': 'success'}
        except:
            resp = {'err': 'internal error'}
    else:
        resp = {'err': 'invalid user details'}
    return Response(resp)

def validUserDetails(givenDetails):
    validDetails = ['email', 'password', 'firstName', 'lastName']
    for detail in validDetails:
        if not (detail in givenDetails):
            return False
    return True
            
