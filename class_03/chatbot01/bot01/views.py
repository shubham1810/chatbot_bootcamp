from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
	return render(request, 'main.html')
	# return HttpResponse("Hello")


def showData(request):

	name = request.GET.get("name", "No Name")
	inst = request.GET.get("inst", "Empty")

	data = {
		'name': name,
		'institute': inst
	}

	ctx = {'data': data}

	return render(request, 'index.html', ctx)
	# return HttpResponse("data")