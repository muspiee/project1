from django.shortcuts import render, redirect
from .models import Human


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        image = request.FILES.get('image')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        if image:
            human = Human.objects.create(name=name, age=age,gender=gender, mobile=mobile, email=email, image=image)
            human.save()
            return redirect('home')

        else:
            human = Human.objects.create(name=name, age=age, gender=gender, mobile=mobile, email=email)
            human.save()
            return redirect('home')

    return render(request, 'index.html')


def allProfile(request):
    all_profiles = Human.objects.all()
    context = {'all_profiles': all_profiles}
    return render(request, 'all_profile.html',context)


def delete(request, id):
    human = Human.objects.get(id=id)
    human.delete()
    return redirect('allProfile')
