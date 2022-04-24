from django.shortcuts import redirect, render
from .models import Complaint
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm, ContactUs
from django.contrib import messages
# Create your views here.

@login_required
def complaint_add(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST ,request.FILES)
        if form.is_valid():
            item = form.save()
            request.session['complaintnumber']=str(item.complaintnumber)
            messages.success(request,'Complaint Added Successfully')
            return redirect('success')
        else:
            messages.error(request,'Something is not correct')
    else:
        form = ComplaintForm()
    ctx = {
        "form":form,
        "title": "Add a complaint"
    }
    return render(request, "complaint_add.html",ctx)

def complaintstatus(request):
    q = request.GET.get('query')
    if q:
        results = Complaint.objects.filter(complaintnumber__contains=q)
        ctx = {
                'title':'search results',
                'results':results,
                'query':q,
            }
        return render(request, "searchresult.html",ctx)
        
    return redirect('status')

def contactme(request):
    form = ContactUs()
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"We will reply back soon")
            return redirect('contactme')
        else:
            messages.error(request,'Something is not correct')
    else:
        form = ContactUs()
    ctx = {
        "form":form,
        "title": "Contact Us"
    }
    return render(request, "contact.html",ctx)


@login_required
def dashboard(request):
    ctx = {'title':'Dashboard'}
    return render(request, 'complaint_add.html',ctx)