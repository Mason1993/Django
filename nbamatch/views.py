from django.shortcuts import render
from match import proj3
from .models import Center, SmallForward, PowerForward, PointGuard, ShootingGuard

# Create your views here.
def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def input(request):
	return render(request, 'input.html')

def inputc(request):
	return render(request, 'inputc.html')

def inputpg(request):
	return render(request, 'inputpg.html')

def inputpf(request):
	return render(request, 'inputpf.html')

def inputsg(request):
	return render(request, 'inputsg.html')

def inputsf(request):
	return render(request, 'inputsf.html')

'''
def inputpf(request):
	return render(request, 'inputpf.html')

def inputpg(request):
	return render(request, 'inputpg.html')

def inputsf(request):
	return render(request, 'inputsf.html')

def inputsg(request):
	return render(request, 'inputsg.html')
'''

def resultc(request):
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
	'''
	pos = str(request.POST['position'])
	res_index = proj3(str(request.POST['position']), params)
	'''
	res_index = proj3('C', params)
	user_para1 = 10 * params[0]
	user_para2 = 10 * params[1]
	user_para3 = 10 * params[2]
	user_para4 = 10 * params[3]
	user_para5 = 10 * params[4]
	user_para6 = 10 * params[5]
	#res = Center.objects.get(index=1)
	
	res = Center.objects.get(id=res_index).player
	query_para1 = 100 * round(Center.objects.get(id=res_index).twopercent,2)
	query_para2 = 100 * round(Center.objects.get(id=res_index).freethrows,2)
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
	context = {'user_para1': user_para1,
	           'user_para2': user_para2,
	           'user_para3': user_para3,
	           'user_para4': user_para4,
	           'user_para5': user_para5,
	           'user_para6': user_para6,
	           'result': res,
	           #'position': pos,
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
	return render(request, 'resultc.html', context)

def resultpf(request):
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
	'''
	pos = str(request.POST['position'])
	res_index = proj3(str(request.POST['position']), params)
	'''
	res_index = proj3('PF', params)
	user_para1 = 10 * params[0]
	user_para2 = 10 * params[1]
	user_para3 = 10 * params[2]
	user_para4 = 10 * params[3]
	user_para5 = 10 * params[4]
	user_para6 = 10 * params[5]
	#res = PowerForward.objects.get(index=1)
	
	res = PowerForward.objects.get(id=res_index).player
	query_para1 = round(100 * PowerForward.objects.get(id=res_index).twopercent,2)
	query_para2 = round(100 * PowerForward.objects.get(id=res_index).freethrows,2)
	query_para3 = round(PowerForward.objects.get(id=res_index).trbs,2)
	query_para4 = round(PowerForward.objects.get(id=res_index).assists,2)
	query_para5 = round(PowerForward.objects.get(id=res_index).steals,2)
	query_para6 = round(PowerForward.objects.get(id=res_index).blocks,2)
	query_para1_n = round(10 * PowerForward.objects.get(id=res_index).twopercentn,0)
	query_para2_n = round(10 * PowerForward.objects.get(id=res_index).freethrowsn,0)
	query_para3_n = round(10 * PowerForward.objects.get(id=res_index).trbsn,0)
	query_para4_n = round(10 * PowerForward.objects.get(id=res_index).assistsn,0)
	query_para5_n = round(10 * PowerForward.objects.get(id=res_index).stealsn,0)
	query_para6_n = round(10 * PowerForward.objects.get(id=res_index).blocksn,0)
	context = {'user_para1': user_para1,
	           'user_para2': user_para2,
	           'user_para3': user_para3,
	           'user_para4': user_para4,
	           'user_para5': user_para5,
	           'user_para6': user_para6,
	           'result': res,
	           #'position': pos,
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
	return render(request, 'resultc.html', context)


def resultpg(request):
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
	'''
	pos = str(request.POST['position'])
	res_index = proj3(str(request.POST['position']), params)
	'''
	res_index = proj3('PG', params)
	user_para1 = 10 * params[0]
	user_para2 = 10 * params[1]
	user_para3 = 10 * params[2]
	user_para4 = 10 * params[3]
	user_para5 = 10 * params[4]
	user_para6 = 10 * params[5]
	#res = PointGuard.objects.get(index=1)
	
	res = PointGuard.objects.get(id=res_index).player
	query_para1 = round(100 * PointGuard.objects.get(id=res_index).threepercent,2)
	query_para2 = round(100 * PointGuard.objects.get(id=res_index).twopercent,2)
	query_para3 = round(100 * PointGuard.objects.get(id=res_index).freethrows,2)
	query_para4 = round(PointGuard.objects.get(id=res_index).assists,2)
	query_para5 = round(PointGuard.objects.get(id=res_index).steals,2)
	query_para6 = round(PointGuard.objects.get(id=res_index).trbs,2)
	
	query_para1_n = round(10 * PointGuard.objects.get(id=res_index).threepercentn,0)
	query_para2_n = round(10 * PointGuard.objects.get(id=res_index).twopercentn,0)
	query_para3_n = round(10 * PointGuard.objects.get(id=res_index).freethrowsn,0)
	query_para4_n = round(10 * PointGuard.objects.get(id=res_index).assistsn,0)
	query_para5_n = round(10 * PointGuard.objects.get(id=res_index).stealsn,0)
	query_para6_n = round(10 * PointGuard.objects.get(id=res_index).trbsn,0)

	context = {'user_para1': user_para1,
	           'user_para2': user_para2,
	           'user_para3': user_para3,
	           'user_para4': user_para4,
	           'user_para5': user_para5,
	           'user_para6': user_para6,
	           'result': res,
	           #'position': pos,
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
	return render(request, 'resultc.html', context)



def resultsf(request):
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
	'''
	pos = str(request.POST['position'])
	res_index = proj3(str(request.POST['position']), params)
	'''
	res_index = proj3('SF', params)
	user_para1 = 10 * params[0]
	user_para2 = 10 * params[1]
	user_para3 = 10 * params[2]
	user_para4 = 10 * params[3]
	user_para5 = 10 * params[4]
	user_para6 = 10 * params[5]
	#res = SmallForward.objects.get(index=1)
	
	res = SmallForward.objects.get(id=res_index).player
	query_para1 = round(100 * SmallForward.objects.get(id=res_index).threepercent,2)
	query_para2 = round(100 * SmallForward.objects.get(id=res_index).twopercent,2)
	query_para3 = round(100 * SmallForward.objects.get(id=res_index).freethrows,2)
	query_para4 = round(SmallForward.objects.get(id=res_index).assists,2)
	query_para5 = round(SmallForward.objects.get(id=res_index).trbs,2)
	query_para6 = round(SmallForward.objects.get(id=res_index).steals,2)
	query_para1_n = round(10 * SmallForward.objects.get(id=res_index).threepercentn,2)
	query_para2_n = round(10 * SmallForward.objects.get(id=res_index).twopercentn,2)
	query_para3_n = round(10 * SmallForward.objects.get(id=res_index).freethrowsn,2)
	query_para4_n = round(10 * SmallForward.objects.get(id=res_index).assistsn,2)
	query_para5_n = round(10 * SmallForward.objects.get(id=res_index).trbsn,2)
	query_para6_n = round(10 * SmallForward.objects.get(id=res_index).stealsn,2)
	context = {'user_para1': user_para1,
	           'user_para2': user_para2,
	           'user_para3': user_para3,
	           'user_para4': user_para4,
	           'user_para5': user_para5,
	           'user_para6': user_para6,
	           'result': res,
	           #'position': pos,
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
	return render(request, 'resultc.html', context)


def resultsg(request):
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
	'''
	pos = str(request.POST['position'])
	res_index = proj3(str(request.POST['position']), params)
	'''
	res_index = proj3('SG', params)
	user_para1 = 10 * params[0]
	user_para2 = 10 * params[1]
	user_para3 = 10 * params[2]
	user_para4 = 10 * params[3]
	user_para5 = 10 * params[4]
	user_para6 = 10 * params[5]
	#res = ShootingGuard.objects.get(index=1)
	
	res = ShootingGuard.objects.get(id=res_index).player
	query_para1 = round(100 * ShootingGuard.objects.get(id=res_index).threepercent,2)
	query_para2 = round(100 * ShootingGuard.objects.get(id=res_index).twopercent,2)
	query_para3 = round(100 * ShootingGuard.objects.get(id=res_index).freethrows,2)
	query_para4 = round(ShootingGuard.objects.get(id=res_index).trbs,2)
	query_para5 = round(ShootingGuard.objects.get(id=res_index).assists,2)
	query_para6 = round(ShootingGuard.objects.get(id=res_index).steals,2)
	query_para1_n = round(10 * ShootingGuard.objects.get(id=res_index).threepercent,0)
	query_para2_n = round(10 * ShootingGuard.objects.get(id=res_index).twopercentn,0)
	query_para3_n = round(10 * ShootingGuard.objects.get(id=res_index).freethrowsn,0)
	query_para4_n = round(10 * ShootingGuard.objects.get(id=res_index).trbsn,0)
	query_para5_n = round(10 * ShootingGuard.objects.get(id=res_index).assistsn,0)
	query_para6_n = round(10 * ShootingGuard.objects.get(id=res_index).stealsn,0)
	context = {'user_para1': user_para1,
	           'user_para2': user_para2,
	           'user_para3': user_para3,
	           'user_para4': user_para4,
	           'user_para5': user_para5,
	           'user_para6': user_para6,
	           'result': res,
	           #'position': pos,
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
	return render(request, 'resultc.html', context)



	      
	      
'''
	elif pos == 'SF':
		  res = SmallForward.objects.get(id=res_index).player
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

	elif pos == 'PF':
		  res = PowerForward.objects.get(id=res_index).player
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


	elif pos == 'PG':
		  res = PointGuard.objects.get(id=res_index).player
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

	elif pos == 'SG':
		  res = ShootingGuard.objects.get(id=res_index).player
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

	else:
		  res = 'error'

'''    

	


