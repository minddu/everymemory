from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def memory1(request):
    return render(request, 'memory1.html')

def study(request):
    return render(request, 'study.html')

def testsheet(request):
    return render(request, 'testsheet.html')

