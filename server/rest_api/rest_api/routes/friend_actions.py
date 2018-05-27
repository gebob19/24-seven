from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..user.models import User

import jwt

@api_view(['POST'])
def send_friend_request(request):
    requestDict = request.data
    if ('token' in requestDict and 'recipientUserID' in requestDict):
        token = requestDict['token']
        recipientUserID = requestDict['recipientUserID']
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = User.objects.get(id=payload['id'])
            recipient = User.objects.get(id=recipientUserID)
        except:
            return Response({'err': 'invalid token'})


        if (not recipientUserID in user.friends and 
            not recipientUserID in user.friendRequests):
            recipient.friendRequests.append(recipientUserID)
            user.save()

        resp = {'message': 'success'}
    else:
        resp = {'err': 'missing required parameters in request'}
    return Response(resp)

@api_view(['POST'])
def accept_friend_request(request):
    requestDict = request.data
    if ('token' in requestDict and 'recipientUserID' in requestDict):
        token = requestDict['token']
        recipientUserID = requestDict['recipientUserID']
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = User.objects.get(id=payload['id'])
            recipient = User.objects.get(id=recipientUserID)
        except:
            return Response({'err': 'invalid token'})
        
        if (recipientUserID in user.friendRequests):
            user.friendRequests.remove(recipientUserID)
            user.friends.append(recipientUserID)
            recipient.friends.append(payload['id'])
            user.save()

        resp = {'message': 'success'}
    else:
        resp = {'err': 'missing required parameters in request'}
    return Response(resp)