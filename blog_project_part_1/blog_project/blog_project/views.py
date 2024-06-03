from django.shortcuts import render
from posts.models import Post
def home(request):
    data = Post.objects.all()
    return render(request,'home.html',{'data':data})  