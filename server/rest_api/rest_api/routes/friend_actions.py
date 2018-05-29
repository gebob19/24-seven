from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..user.models import User

import jwt

@api_view(['POST'])
def send_friend_request(request):
    validation = validRequest(request)
    if (validation[0]):
        user = validation[1]
        recipient = validation[2]

        if (user.canSendFriendRequest(recipient)):
            user.getFriendController().sendFriendRequest(recipient)
            resp = {'message': 'success'}
        else:
            resp = {'message': 'unable to send friend request'}
    else:
        resp = {'err': validation[1]}
    return Response(resp)

@api_view(['POST'])
def accept_friend_request(request):
    validation = validRequest(request)
    if (validation[0]):
        user = validation[1]
        requester = validation[2]

        if (user.canAcceptFriendRequest(requester)):
            user.getFriendController().acceptFriendRequest(requester)
            resp = {'message': 'success'}
        else:
            resp = {'err': 'unable to accept friend request'}
    else:
        resp = {'err': validation[1]}

    return Response(resp)

def validRequest(request):
    requestDict = request.data
    if ('token' in requestDict and 'recipientID' in requestDict):
        token = requestDict['token']
        recipientID = requestDict['recipientID']
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
            return [False, 'unable to decode token']
        try:
            print(payload['id'], recipientID)
            user = User.objects.get(id=payload['id'])
            recipient = User.objects.get(id=recipientID)
        except:
            return [False, 'invalid parameters']
        
        resp = [True, user, recipient]
    else:
        resp = [False, 'missing parameters']
    return resp
        
