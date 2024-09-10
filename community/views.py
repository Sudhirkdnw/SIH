from django.shortcuts import render, redirect
import requests

def community(request):
    return render(request, 'community/community.html')