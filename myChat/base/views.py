from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
import json
from django.views.decorators.csrf import csrf_exempt

def getToken(request):
    appId = "2a437b8895d249889b9ba902153f6bc5"
    appCertificate = "902c1dfd353b45e7a9c8fa0414c209fa"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token': token, 'uid': uid}, safe=False)
# Create your views here.
def render_lobby(request):
    return render(request, 'base/lobby.html')


def render_room(request):
    return render(request, 'base/room.html')
