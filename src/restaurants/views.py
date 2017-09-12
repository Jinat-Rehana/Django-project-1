import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# function based view

# def home(request):

	# html_=""" <!DOCTYPE html>

	# <html lang=eng>
	# <head>
	# </head>
	# <body>

	# <h1>Hellow</h1>

	# <p>This is html coming through</p>	

	# </body>
	# </html>

    


	#  """

	# return HttpResponse(html_)

	#return render(request, "home.html", {})         #response

def home(request):

	num= random.randint(0, 100000)
	some_list= [num, random.randint(0, 100000), random.randint(0, 100000)]

	context= {
	"bool_item":True, 
	"num":num,
	"some_list":some_list
	}

	return render(request, "base.html", context)         #response