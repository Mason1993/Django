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
	      query_para1 = Center.objects.get(id=res_index).twopercent
	      query_para2 = Center.objects.get(id=res_index).freethrows
	      query_para3 = Center.objects.get(id=res_index).trbs
	      query_para4 = Center.objects.get(id=res_index).assists
	      query_para5 = Center.objects.get(id=res_index).steals
	      query_para6 = Center.objects.get(id=res_index).blocks
	      

	elif pos == 'SF':
		  res = SmallForward.objects.get(id=res_index).player
		  query_results = SmallForward.objects.get(id=res_index)

	elif pos == 'PF':
		  res = PowerForward.objects.get(id=res_index).player
		  query_results = PowerForward.objects.get(id=res_index)


	elif pos == 'PG':
		  res = PointGuard.objects.get(id=res_index).player
		  query_results = PointGuard.objects.get(id=res_index)

	elif pos == 'SG':
		  res = ShootingGuard.objects.get(id=res_index).player
		  query_results = ShootingGuard.objects.get(id=res_index)

	else:
		  res = 'error'

    

	context = {'result': res,
	           'position': pos,
	           'para1': query_para1,
	           'para2': query_para2,
	           'para3': query_para3,
	           'para4': query_para4,
	           'para5': query_para5,
	           'para6': query_para6}
	# import pdb; pdb.set_trace()
	return render(request, 'result.html', context)


