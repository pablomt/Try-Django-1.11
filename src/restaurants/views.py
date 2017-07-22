from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
def home(request):
	html_var = "f strings"
	html_ = f"""<!DOCTYPE html> 
	<html lang=es>
	<head>
	<body>
	<h1> Hello World!! </h1>
	<p> This is {html_var} coming through</p>
	</body>
	</head>
	</html>
	""" 

	# f strings es nuevo en python 3.6. Es una buena manera de hacer sustitucion de strings
	# Se necesita poner la f antes de empezar el string con """ para poder realizar la sistitucion
	return HttpResponse(html_)
	#return render(request, "template", {})

