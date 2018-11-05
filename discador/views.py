
from django.shortcuts import render
from discador.models import *
from django.contrib.auth.decorators import login_required


from django.views.decorators.csrf import csrf_exempt
import simplejson
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth import login

from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from discador.serializers import *

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
from django.db.models.signals import pre_save
from django.dispatch import receiver

def api_agentes(request):

	_data = Agente.objects.all()
	print 'traes la daata?', data
	serializer =  AgentesSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)
# Create your views here.
