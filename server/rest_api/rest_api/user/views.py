from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer
from .models import User
import jwt

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = None

    @action(methods=['post'], detail=False)
    def friends(self, request):
        validation = isValidRequest(request)
        if (validation[0]):
            payload = validation[1]
            friends = User.objects.get(id=payload['id']).friends

            queryset = User.objects(id__in=friends)
            resp = []
            for user in queryset:
                resp.append(user.toQuickView())
        else:
            resp = {'err': validation[1]}
        
        return Response(resp)

    @action(methods=['post'], detail=False)
    def my_friend_requests(self, request):
        validation = isValidRequest(request)
        if (validation[0]):
            payload = validation[1]
            myFriendRequests = User.objects.get(id=payload['id']).myFriendRequests

            queryset = User.objects(id__in=myFriendRequests)
            resp = []
            for user in queryset:
                resp.append(user.toQuickView())
        else:
            resp = {'err': validation[1]}
        
        return Response(resp)

    
    @action(methods=['post'], detail=False)
    def sent_friend_requests(self, request):
        validation = isValidRequest(request)
        if (validation[0]):
            payload = validation[1]
            sentFriendRequests = User.objects.get(id=payload['id']).sentFriendRequests

            queryset = User.objects(id__in=sentFriendRequests)
            resp = []
            for user in queryset:
                resp.append(user.toQuickView())
        else:
            resp = {'err': validation[1]}
        
        return Response(resp)


def isValidRequest(request):
    requestDict = request.data
    if ('token' in requestDict):
        token = requestDict['token']
        try: 
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
            return [False, 'unable to decode token']

        resp = [True, payload] if payload['id'] else [False, 'invalid token']
    else:
        resp = [False, 'missing parameters']
    
    return resp