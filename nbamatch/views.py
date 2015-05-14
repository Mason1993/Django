from django.shortcuts import render
from match import proj3
from .models import Center, SmallForward, PowerForward, PointGuard, ShootingGuard

# Create your views here.
def index(request):
	return render(request, 'index.html')

def input(request):
	return render(request, 'input.html')

def result(request):
	params = []
	params.append(float(request.POST['param1'])/10)
	params.append(float(request.POST['param2'])/10)
	params.append(float(request.POST['param3'])/10)
	params.append(float(request.POST['param4'])/10)
	params.append(float(request.POST['param5'])/10)
	params.append(float(request.POST['param6'])/10)

	
	import os 
	print os.getcwd() #returns current working directory of a process


	#res_index = proj3(str(request.POST['position']), params)
	#res = nbamatch_center.find_by(index: res_index).player
	pos = str(request.POST['position'])
	res_index = proj3(str(request.POST['position']), params)
	#res = Center.objects.get(index=1)
	if pos == 'C':
	      res = Center.objects.get(id=res_index).player

	elif pos == 'SF':
		  res = SmallForward.objects.get(id=res_index).player

	elif pos == 'PF':
		  res = PowerForward.objects.get(id=res_index).player

	elif pos == 'PG':
		  res = PointGuard.objects.get(id=res_index).player

	elif pos == 'SG':
		  res = ShootingGuard.objects.get(id=res_index).player

	else:
		  res = 'error'

    

	context = {'result': res,
	           'position': pos}
	# import pdb; pdb.set_trace()
	return render(request, 'result.html', context)