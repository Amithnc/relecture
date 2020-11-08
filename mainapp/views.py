from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib import auth
from .models import post

def homepage(request):
    return render (request,'home.html')

def register(request):
    if request.method == "POST":
        Type=request.POST.get('type',None)
        User = get_user_model()
        if Type=="Organization":
            org_name = request.POST['org_name']
            password = request.POST['password']
            if User.objects.filter(username=org_name).exists():
                messages.error(request, 'Organization Name is already present ')
                return redirect("/register")
            else:
                User.objects.get_or_create(username=org_name, is_staff=True)   
                u = User.objects.get(username=org_name)   
                u.set_password(password)    
                group = Group.objects.get(name='organization')
                u.groups.add(group)
                u.save()
                messages.success(request, 'Created successfully please login with your username')
                return redirect("/")
        elif Type=="experts":
            expert_name =request.POST.get('expert_name',None)
            password = request.POST.get('password',None)
            if User.objects.filter(username=expert_name).exists():
                messages.error(request, 'Name is already present ')
                return redirect("/register")
            else:
                User.objects.get_or_create(username=expert_name, is_staff=False)   
                u = User.objects.get(username=expert_name)   
                u.set_password(password)    
                group = Group.objects.get(name='experts')
                u.groups.add(group)
                u.save()
                messages.success(request, 'Created successfully please login with your username')
                return redirect("/")
    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'logged-out successfully')
    return redirect("/")


@login_required(login_url='/login')
def dashboard(request):
    context={}
    user=request.user
    if user.groups.filter(name='organization').exists():
        User = get_user_model()
        all_experts=User.objects.filter(groups__name="experts")
        context['experts']=all_experts
    elif user.groups.filter(name='experts').exists():
        posts=post.objects.all()
        context['posts']=posts
    return render(request,'dashboard.html',context)

