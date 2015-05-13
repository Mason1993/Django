from django.shortcuts import render
from match import proj3
from .models import Center

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
	res = proj3(str(request.POST['position']), params)
	#res = Center.objects.get(index=1)


	context = {'result': res}
	# import pdb; pdb.set_trace()
	return render(request, 'result.html', context)