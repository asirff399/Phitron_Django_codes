from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(request): 
    if request.method == 'POST':
        post_froms = forms.PostFrom(request.POST)
        if post_froms.is_valid():
            # post_froms.cleaned_data['author'] = request.user
            post_froms.instance.author = request.user
            post_froms.save()
            return redirect('add_post')
    else:
        post_froms = forms.PostFrom()
    return render(request,'add_post.html',{'form':post_froms}) 

@login_required
def edit_post(request,id): 
    post = models.Post.objects.get(pk=id)
    post_froms = forms.PostFrom(instance=post)
    if request.method == 'POST':
        post_froms = forms.PostFrom(request.POST,instance=post)
        if post_froms.is_valid():
            post_froms.instance.author = request.user
            post_froms.save()
            return redirect('homepage')
    return render(request,'add_post.html',{'form':post_froms})

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')