from django.shortcuts import render,redirect
from.models import reg
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import EmojiModel

# Create your views here.
# def home(request):
#     mydata=reg.objects.all()
#     if(mydata!=''):
#         return render(request,'index.html',{'datas':mydata})
#     else:
#       return render(request,'index.html')
def home(request):
     return render(request,"mainpage.html")
def back(request):
     return render(request,"home.html")

def add(request):
      if request.method=='POST':
        fname=request.POST['name']
        lname=request.POST['age']
        email=request.POST['city']
        obj=reg()
        obj.Firstname=fname
        obj.Lastname=lname
        obj.Email=email
        obj.save()
        return render(request,'dash.html')
      return render(request,'index.html')
def up(request,id):
        mydata=reg.objects.get(id=id)
        if request.method=='POST':
          fname=request.POST['name']
          lname=request.POST['age']
          email=request.POST['city']
          mydata.Firstname=fname
          mydata.Lastname=lname
          mydata.Email=email
          mydata.save()
          myddata=reg.objects.all()
          return render(request,'dash.html',{'data':myddata})
        myddata=reg.objects.all()
        return render(request,'dash.html',{'datas':mydata,'data':myddata})

def de(request,id):
    mydata=reg.objects.get(id=id)
    mydata.delete()
    mydata=reg.objects.all()
    if(mydata!=''):
        return render(request,'dash.html',{'data':mydata})
    else:
      return render(request,'dash.html')


def dash(request):
       mydata=reg.objects.all()
       return render(request,'dash.html',{'datas':mydata})
def first(request):
      last_data = reg.objects.first()
      return render(request, 'dash.html', {'data': [last_data]})

def last(request):
    # Retrieve the last (most recent) record based on the 'id' field
    last_data = reg.objects.latest('id')
    
    # Return a list containing the single object
    return render(request, 'dash.html', {'data': [last_data]})

def all(request):
    if request.method=='POST':
        fname=request.POST['name']
        lname=request.POST['age']
        email=request.POST['city']
        obj=reg()
        obj.Firstname=fname
        obj.Lastname=lname
        obj.Email=email
        obj.save()
    mydata=reg.objects.all()
    if(mydata!=''):
        return render(request,'dash.html',{'data':mydata})
    else:
      return render(request,'dash.html')
def bac(request):
     return render(request,"dash.html")


def logg(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, 'dash.html')
            messages.success(request,("Check  your User name and Password"))
        else:
            return render(request, 'dash.html')
            messages.success(request,("Check  your User name and Password"))
    else:
        return render(request, 'home.html')
    



def regg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        # Create the superuser
        user = User.objects.create_superuser(username=username, email=email, password=password)
        
        # Log in the superuser
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)           
            return redirect('home')  # Redirect to the homepage after successful creation
        else:
            return render(request,'home')
    else:
        return render(request, 'home.html')

from PIL import Image, ImageDraw
from django.http import HttpResponse
from .models import EmojiModel

def emoj(request):
    return render (request,"emoji.html")



from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from .models import EmojiModel

def place_text_on_image(request):
    # Retrieve text from the Django model
    emoji_instance = EmojiModel.objects.first()  # Assuming you want the first instance
    text = emoji_instance.emoji

    # Create an image with Python Pillow
    image = Image.new("RGB", (300, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Define font and size
    font_size = 20
    font = ImageFont.load_default()  # Using default font for demonstration

    # Calculate text size
    text_width, text_height = draw.textsize(text)

    # Calculate text position
    text_x = (image.width - text_width) // 2
    text_y = (image.height - text_height) // 2

    # Draw text on the image
    draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

    # Save the image or serve it in HTTP response
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response