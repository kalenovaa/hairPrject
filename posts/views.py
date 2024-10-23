from django.contrib.auth import login
from django.shortcuts import render
from posts.models import Login

def html_view(request):
    main_page_data = Login.objects.order_by('position')
    template = '../templates/html/hair.html'
    return render(request, template, {'logins': main_page_data})

def login_view(request):
    login_v = Login.objects.all()
    return render(request, '../templates/html/login.html', context={"login": login_v})

def sign_in(request):
    return render(request, '../templates/html/sign_in.html')
