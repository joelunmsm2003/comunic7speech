from django.shortcuts import render
from app.models import *
from colasIN.models import *
from comunica7.models import *
from django.contrib.auth.decorators import login_required


from django.views.decorators.csrf import csrf_exempt
import simplejson
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth import login

from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from app.serializers import *
from app.forms import *
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
from django.db.models.signals import pre_save
from django.dispatch import receiver



# Create your views here.
def ingresar(request):

	if request.method == 'POST':

		user = request.POST['user']
		
		psw = request.POST['password']

		user = authenticate(username=user, password=psw)
	
		if user is not None:

			if user.is_active:

				login(request, user)

				a =Agente.objects.get(user_id=request.user.id)
				a.estado_id=1
				a.save()

				return HttpResponseRedirect("/comunica7/dashboard")


		return render(request, 'ingresar.html',{'error':'Usuario no existe'})

	if request.method == 'GET':


		return render(request, 'comunica7/ingresar.html',{})


def dashboard(request):

	id_user= request.user.id

	productos=Usuarios_Productos.objects.filter(usuario__user_id=id_user)
	
	print productos

	return render(request, 'comunica7/dashboard.html',{'productos':productos})