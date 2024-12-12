from django.shortcuts import render
from django.contrib import messages

def crob_home_view(request):
	return render(request, 'crob/index.html')

def event_page_view(request):
	return render(request, 'crob/apply.html')
