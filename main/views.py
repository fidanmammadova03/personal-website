from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    return render(request, "contact.html")

def tryanyway(request):
    return render(request, "blogs/tryanyway.html")

def cutsugar(request):
    return render(request, "blogs/cutsugar.html")

def remsleep(request):
    return render(request, "blogs/remsleep.html")

def beingok(request):
    return render(request, "blogs/beingok.html")

def idea(request):
    return render(request, "blogs/idea.html")

def books(request):
    return render(request, "blogs/books.html")

def sales_dashboard(request):
    return render(request, 'projects/sales_dashboard.html')
