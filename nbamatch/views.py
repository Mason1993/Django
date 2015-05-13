from django.shortcuts import render
from match import proj3

# Create your views here.
def index(request):
	return render(request, 'nbamatch/index.html')

def result(request):
	params = []
	params.append(float(request.POST['param1'])/10)
	params.append(float(request.POST['param2'])/10)
	params.append(float(request.POST['param3'])/10)
	params.append(float(request.POST['param4'])/10)
	params.append(float(request.POST['param5'])/10)
	params.append(float(request.POST['param6'])/10)

	
	import os 
	print os.getcwd() 

	res = proj3(str(request.POST['position']), params)


	context = {'result': res}
	# import pdb; pdb.set_trace()
	return render(request, 'nbamatch/result.html', context)