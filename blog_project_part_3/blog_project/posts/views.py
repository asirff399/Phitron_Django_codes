from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView ,DeleteView,DetailView
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

@method_decorator(login_required,name='dispatch')
class AddPostCreatView(CreateView):
    model = models.Post
    form_class = forms.PostFrom
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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

@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostFrom
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self,request, *args,**kwargs):
        comment_form = forms.CommentFrom(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args,**kwargs)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
    
        comment_form = forms.CommentFrom()

        contex['comments'] = comments
        contex['comment_form'] = comment_form
        return contex

        