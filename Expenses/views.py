from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Expenses/index.html')

def add_expenses(request):
    return render(request,'Expenses/add_expenses.html')