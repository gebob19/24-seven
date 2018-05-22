from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer
from .models import User
import jwt

class UserViewSet(ModelViewSet):
    # serializer_class = UserSerializer
    # queryset = User.objects.all()

    @action(methods=['post'], detail=False)
    def all_friends(self, request):
        requestDict = request.data
        if ('token' in requestDict):
            token = requestDict['token']
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                friends = User.objects.get(id=payload['id']).friends
                queryset = User.objects(id__in=friends)
                resp = []
                for user in queryset:
                    resp.append(user.toQuickView())
            except:
                resp = {'err': 'invalid token'}
        else:
            resp = {'err': 'missing token'}
        return Response(resp)

    @action(methods=['post'], detail=False)
    def send_friend_request(self, request):
        requestDict = request.data
        if ('token' in requestDict and 'recipientUserID' in requestDict):
            token = requestDict['token']
            recipientUserID = requestDict['recipientUserID']
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user = User.objects.get(id=payload['id'])

                if (not recipientUserID in user.friends):
                    user.friends.append(recipientUserID)
                    user.save()

                resp = {'message': 'success'}
            except:
                resp = {'err': 'invalid token'}
        else:
            resp = {'err': 'missing required parameters in request'}
        return Response(resp)
