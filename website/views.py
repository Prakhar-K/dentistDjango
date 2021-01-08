from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request, 'home.html',{})

def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		messages = request.POST['message']

		#Send an email
		send_mail(
			message_name,#subject
			messages,#message
			message_email,# from email
			['something@someone.com'],#to email
			)
		return render(request, 'contact.html',{"message_name":message_name})


	else:
		return render(request, 'contact.html',{})

def about(request):
	return render(request, 'about.html',{})

def pricing(request):
	return render(request, 'pricing.html',{})

def services(request):
	return render(request, 'services.html',{})

def portfolio(request):
	return render(request, 'portfolio.html',{})

