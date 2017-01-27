from django.shortcuts import render
from django.http import HttpResponse

from models import MyData
import copy

# Create your views here.

def hello(request):

	all_data = MyData.objects.filter(name="Name 01")[:n]
	data = []

	for dt in all_data:
		information = {}
		information['name'] = dt.name
		information['inst'] = dt.institution
		data.append(copy.deepcopy(information))

	ctx = {'data': data}
	print ctx

	return render(request, 'main.html', ctx)
	# return HttpResponse("Hello")


def showData(request):

	name = request.GET.get("name", "No Name")
	inst = request.GET.get("inst", "Empty")

	data = {
		'name': name,
		'institute': inst
	}

	new_data_element = MyData(name=name, institution=inst)
	new_data_element.save()

	ctx = {'data': data}

	return render(request, 'index.html', ctx)
	# return HttpResponse("data")