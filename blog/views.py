from django.shortcuts import render
from django.views.generic import View

class BlogView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, "blog.html", context)


# Create your views here.
