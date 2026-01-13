from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Login,Post
from .forms import customerform

def create_post(request):
    Post.objects.create(
        title='My hobby ',
        content='The most activity that I love is play socceer because it made me feel relax .',

    )
    return HttpResponse('Post created  ')

def show_post(request):
    posts=Post.objects.all()
    return render(request,'myapp/post.html',{"posts":posts})

def update_post(request,id):
    post=get_object_or_404(Post,id=id )
    post.title="The django "
    post.content="Django is a frameword of python that using for backend website ."
    post.save()
    return HttpResponse('Post update success !')

def delete_post(request,id):
    post=get_object_or_404(Post,id=id )
    post.delete()
    return HttpResponse('Post Delete  success !')

def create_byformmodels(request):
    if request.method=='POST':
        form=customerform(request.post)
        if form.is_valid():
            form.save()
    else: 
        form=customerform()
    return render (request,'myapp/formcutomer.html',{'form':form})


def product(request):
    product={
            "store":{
                "electronics":[
                    {"name" :"laptop","price":1200},
                    {"name" :"headphones","price":1200},
                ],
                "clothing":[
                    {"name" :"t-shirt","price":1200},
                    {"name" :"jacket","price":1200},
                ]
            }
        }
        
    return render(request,'myapp/index.html',{"store":product['store']})

def student(request):
    
        student=[
            {"name ":"dara","score":97},
            {"name ":"min","score":97},
            {"name ":"bobo","score":97}
        ]
        return  render(request, "myapp/students.html", {"students": student})


def login_form(request):
    login=Login.objects.all()
    if request.method == "POST":
        action = request.POST.get("action")
        
        if action == "add":
            name = request.POST.get("name",'')
            age = request.POST.get("age",'')
            gender = request.POST.get("gender",'')

            Login.objects.create(name=name, age=age, gender=gender)

        elif action == "delete":
            name = request.POST.get("name")
            Login.objects.filter(name=name).delete()

        elif action == "search":
            name = request.POST.get("name")
            login = Login.objects.filter(name__icontains=name)

        elif action == "update":
            name = request.POST.get("name")
            age = request.POST.get("age")
            gender = request.POST.get("gender")

            Login.objects.filter(name=name).update(age=age, gender=gender)

        login = Login.objects.all()  # refresh table after action

    return render(request, "myapp/login.html",{"login": login})
def login_database(request):
    if request.method =="POST":
          user=authenticate(request,
                            username=request.POST.get("username","") ,
                            password=request.POST.get("password","") 
                            )
          if user is not None :
               login(request, user)
               return redirect("login/")
          else:
            return render(request, "", {"error": "Invalid credentials"})
          
    return render(request, "myapp/authentication.html")
          
          




def show(request):
     login=Login.objects.all()
     return render(request, "myapp/table.html", {"login": login})

def base(request):
    return render(request,'myapp/base.html')

def home(request):
    return render(request,'myapp/home.html')

def admin(request):
    return render(request,'myapp/admin.html')

def admin1(request):
    return render(request,'myapp/admin1.html')

