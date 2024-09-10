from django.shortcuts import render, redirect
import requests


ESP8266_URL = 'http://10.10.202.103/'

def control(request, action):
    if action == 'on':
        requests.get(f'{ESP8266_URL}motor/on')
    elif action == 'off':
        requests.get(f'{ESP8266_URL}motor/off')
    return redirect('home')
def home(request):
    return render(request, 'Frontend/iot/home.html')
