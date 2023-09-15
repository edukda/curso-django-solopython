from django.shortcuts import render, redirect, get_list_or_404  
from django.views.generic import View
from .form import CreateForm
from .models import Post

class BlogView(View):
    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(request, "blog.html", context)
    
class BlogViewList(View):
    def get(self, request, *args, **kwargs):

        posts = Post.objects.all()
        context = {
            'posts': posts
        }

        return render(request, 'blog_list.html', context)
    
class BlogViewCreate(View):
    def get(self, request, *args, **kwargs):
        form = CreateForm()
        context = {
            'form': form
        }
        return render(request, "form.html", context)
    
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = CreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                comment = form .cleaned_data.get('comment')

                p, created = Post.objects.get_or_create(title=title, comment=comment)
                p.save()
                return redirect('primary')
            
        context={

        }
        return render(request, "form.html", context)     

# Create your views here.
