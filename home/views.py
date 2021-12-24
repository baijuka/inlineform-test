from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm


def getName(request):
    if request.method =='POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    
    return render(request, 'name.html', {'form': form})


def thanks(request):
    
    return render(request, 'thanks.html')
