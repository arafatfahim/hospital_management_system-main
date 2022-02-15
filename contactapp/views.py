from django.shortcuts import render
from contactapp.models import Contact
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            meassage  = request.POST.get("message")
            phone = request.POST.get("phonenumber") 
            Contact.objects.create(name=name,meassage=meassage,phone=phone)
            return render(request,'homeapp/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form field currectly!')
    return render(request,'contactapp/contact.html')


