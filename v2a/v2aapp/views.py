from django.shortcuts import render
from .models import feedbackdata
from django.contrib import messages
# Create your views here.
def feedback(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        msg=request.POST["feedback"]
        obj=feedbackdata(name=name,email=email,msg=msg)
        obj.save()
        messages.success(request,"your feedback saved successfully, Thanks for giving feedback")
        
    return render(request,"feedback.html")