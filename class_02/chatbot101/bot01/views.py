from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def mainBot(request):

	name = str(request.GET.get('name', 'abc'))

	html = """
	<html>
	<head>
	<title>MyPage</title>
	<style>
		body {
			background-color: yellow;
		}
	</style>
	</head>

	<body>
	My Name is """ + name + """.
	This is my test page
	</body>

	</html>
	"""
	return HttpResponse(html)

def convertTemp(request):
	temp = float(request.GET.get('temp', 0.0))

	faren = (9.0 * temp/5) + 32.0

	data = {
		'celsius': temp,
		'converted': faren,
		'status': 'OK'
	}

	final = json.dumps({'data': data})

	return HttpResponse(final)