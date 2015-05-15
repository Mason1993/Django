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
	user_para1 = 10 * params[0]
	user_para2 = 10 * params[1]
	user_para3 = 10 * params[2]
	user_para4 = 10 * params[3]
	user_para5 = 10 * params[4]
	user_para6 = 10 * params[5]
	#res = Center.objects.get(index=1)
	if pos == 'C':
	      res = Center.objects.get(id=res_index).player
	      query_para1 = round(Center.objects.get(id=res_index).twopercent,2)
	      query_para2 = round(Center.objects.get(id=res_index).freethrows,2)
	      query_para3 = round(Center.objects.get(id=res_index).trbs,2)
	      query_para4 = round(Center.objects.get(id=res_index).assists,2)
	      query_para5 = round(Center.objects.get(id=res_index).steals,2)
	      query_para6 = round(Center.objects.get(id=res_index).blocks,2)
	      query_para1_n = round(10 * Center.objects.get(id=res_index).twopercentn,0)
	      query_para2_n = round(10 * Center.objects.get(id=res_index).freethrowsn,0)
	      query_para3_n = round(10 * Center.objects.get(id=res_index).trbsn,0)
	      query_para4_n = round(10 * Center.objects.get(id=res_index).assistsn,0)
	      query_para5_n = round(10 * Center.objects.get(id=res_index).stealsn,0)
	      query_para6_n = round(10 * Center.objects.get(id=res_index).blocksn,0)
	      

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

    

	context = {'user_para1': user_para1,
	           'user_para2': user_para2,
	           'user_para3': user_para3,
	           'user_para4': user_para4,
	           'user_para5': user_para5,
	           'user_para6': user_para6,
	           'result': res,
	           'position': pos,
	           'para1': query_para1,
	           'para2': query_para2,
	           'para3': query_para3,
	           'para4': query_para4,
	           'para5': query_para5,
	           'para6': query_para6,
	           'para1n': query_para1_n,
	           'para2n': query_para2_n,
	           'para3n': query_para3_n,
	           'para4n': query_para4_n,
	           'para5n': query_para5_n,
	           'para6n': query_para6_n}
	# import pdb; pdb.set_trace()
	return render(request, 'result.html', context)


