from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        return render(request, 'home.html', {"question": question})
    return render(request, 'home.html', {})
