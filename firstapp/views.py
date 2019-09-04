# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from firstapp.model.dream_real import Dreamreal,Online
from django.core.mail import send_mail
from django.shortcuts import render
from firstapp.forms import  LoginForm

import sys
# Create your vyus here.
def hi(request,number):
   text = "<h1>welcome to my app number %s!</h1>"%number
   return HttpResponse(text)

def create_site(request, name, phno):
   "this is a sample post request"
   print(request.method, request.COOKIES)
   ol=Online.objects.get(id=1);
   dream_real_entity =  Dreamreal(website = "www.polo.com", mail = "sorex@polo.com",
      name = name, phonenumber = phno, online=ol)
   dream_real_entity.save();
   all_objects = Dreamreal.objects.all()
   print(all_objects)
   for obj in all_objects:
      print(obj.website, obj.name, obj.mail, obj.phonenumber)

   #ob=Dreamreal.objects.get(name="1");
  # print(ob.mail)

   text = "<h1>Successfully created app with name {} and phoneno  {} !</h1>".format(name ,phno)
   return HttpResponse(text)

def get_sites(request):
   "get all sites"
   all_objects=Dreamreal.objects.all()
   print(all_objects)


def send_email(request,emailto):
   print("sending email to {} ".format(emailto))
   res = send_mail("hello rokes", "message?", "rrakesh100@gmail.com", ["rrakesh100@gmail.com"])
   return HttpResponse('%s'%res)


def static_file(request):
   return render(request, 'static.html', {})

def login(request):

   user_name='dummy'
   print(request)
   if(request.method=="POST"):
      print("request method is post")
      print("request. post = {}".format(request.POST));
      print("request.body = {}".format(request.body))
      MyLoginForm=LoginForm(request.POST);
      print(MyLoginForm)
      if MyLoginForm.is_valid:
         print('reached inside valid')
         print(MyLoginForm.cleaned_data)
         user_name=MyLoginForm.cleaned_data['password']
      else:
         print("is valid failed")
   else:
      MyLoginForm=LoginForm();

   return render(request, 'loggedin.html', {"username" : user_name})


