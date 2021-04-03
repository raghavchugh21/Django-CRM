from django.shortcuts import render, reverse

def LandingPage(request):
    return render(request, 'landing_page.html')