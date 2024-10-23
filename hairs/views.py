# from django.contrib.auth import login
# from django.shortcuts import render
# from posts.models import Login
# from django.http import HttpResponse
#
# def html_view(request):
#     return render(request, '../static/../templates/html/../html/hair.html')
#
# def css_view(request):
#     return render(request, '../static/css/styles.css')
#
# def login_view(request):
#     login_v = Login.objects.all()
#     return render(request, '../templates/html/login.html')



#
# class Home (TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, request):
#         ctx = {}
#         return render(request, self.template_name, ctx)
