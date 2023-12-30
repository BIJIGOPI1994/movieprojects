
from django.shortcuts import render
from review.models import Review
app_name="review"


def addmovie(request):
    if(request.method=="POST"):
        image = request.FILES["i"]
        name = request.POST["m"]
        year = request.POST["y"]
        b=Review.objects.create(image=image,name=name,year=year)
        b.save()
        return viewmovie(request)
    return render(request,"addmovie.html")

def viewmovie(request):
    b = Review.objects.all()
    return render(request,"viewmovie.html",{"review":b})

def update_delete(request,p):
    b = Review.objects.get(id=p)
    return render(request,"update.html",{"review":b})

def delete(request,p):
    b = Review.objects.get(id=p)
    b.delete()
    return viewmovie(request)
def update(request,p):
    if(request.method=="POST"):
       b = Review.objects.get(id=p)
       b.image =  request.FILES["i"]
       b.name = request.POST["m"]
       b.year = request.POST["y"]
       b.save()
       return viewmovie(request)
    return render(request,"addmovie.html")