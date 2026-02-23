from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
import requests
import threading
import json
FIREBASE_URL = "https://mayaedu-accounts-default-rtdb.firebaseio.com/"
# Create your views here.
def loading(request):
  return render(request, "loading.html")
def index(request):
  return render(request, "index.html")
def course(request):
  return render(request, "course.html") 
def about(request):
  return render(request, "about.html") 
def contact(request):
  return render(request, "contact.html")
def send_to_firebase(url, data):
    try:
        requests.patch(url, json=data)
    except:
        pass  # ignore errors

"""def signup(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname").replace(" ", "_")
        class_name = request.POST.get("class_name").lower()
        sex = request.POST.get("sex")
        user_data = None
        url = None
        if class_name == "student":
          user_data = {
              fullname: {
                  "fullname": fullname,
                  "sex": sex,
                  "classcaptain": "none"
              }
          }
          url = f"{FIREBASE_URL}/students/{class_name}.json"  
        elif class_name == "none":
          user_data = {
              fullname: {
                  "fullname": fullname,
                  "sex": sex,
              }
          }
          url = f"{FIREBASE_URL}/teachers/.json"  
        
        threading.Thread(target=send_to_firebase, args=(url, user_data)).start()
        response = redirect("/index/")
        response.set_cookie("user_info",json.dumps(user_data),max_age=314496000)
        return response
        
    return render(request, "signup.html")"""
def signup(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname").replace(" ", "_")
        class_name = request.POST.get("class_name").lower()
        sex = request.POST.get("sex")

        if class_name == "student":
            user_data = {
                fullname: {"fullname": fullname, "sex": sex, "classcaptain": "none"}
            }
            url = f"{FIREBASE_URL}/students/{class_name}.json"
        else:
            user_data = {fullname: {"fullname": fullname, "sex": sex}}
            url = f"{FIREBASE_URL}/teachers/.json"

        # Directly send without threading
        try:
            requests.patch(url, json=user_data, timeout=5)
        except requests.RequestException:
            pass

        response = redirect("/index/")
        response.set_cookie("user_info", json.dumps(user_data), max_age=314496000)
        return response

    return render(request, "signup.html")    