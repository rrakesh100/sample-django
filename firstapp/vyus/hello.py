from django.http import HttpResponse
from django.shortcuts import render

def hi(request, num):
   text = "<h1>welcome to vyu number %s!</h1>"%num
   return HttpResponse(text)


def hi_with_template(request, num):
   return render(request, "hello.html", {"number": num})