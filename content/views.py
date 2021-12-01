from django.shortcuts import render, redirect
from .models import BlogPost, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random

def home(request):
    blogs_search = []
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        blogs_search = BlogPost.objects.filter(blog_title__icontains = search_keyword)
    blogs = list(BlogPost.objects.all())
    blogs_main = random.sample(blogs, len(blogs))
    blogs_recent = BlogPost.objects.all().order_by('-publish_date')[:4]
    blogs_popular = random.sample(blogs_main, len(blogs_main))[:4]
    blogs_editor = random.sample(blogs_popular, len(blogs_popular))[:4]
    if blogs_search != []:
        blogs_main = blogs_search
    context = {
        "blogs": blogs_main,
        "tags": {
        'Finance': 'Finance',
        'Fashion': 'Fashion',
        'Politics' : 'Politics',
        'Sports' : 'Sports',
        'Travel' : 'Travel',
        'Lifestyle' : 'Lifestyle',
        'Science' : 'Science',
        'Environment' : 'Environment',
        'Technology' : 'Technology',
        },
        "blogs_popular": blogs_popular,
        "blogs_recent": blogs_recent,
        "blogs_editor": blogs_editor,
    }
    return render(request, "blogs/home.html", context)

@login_required(login_url='login')
def blog_upload(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            author = User.objects.get(username = request.user.username)
            blog_title = request.POST['blog_title']
            blog_content = request.POST['blog_content']
            blog_image = request.FILES['blog_image']
            category = Category.objects.get(category = request.POST['category'])
            blog = BlogPost.objects.create(author=author, blog_title=blog_title, blog_content=blog_content, blog_image=blog_image, category=category)
            blog.save()
            return render(request, 'blogs/blog_upload.html')
        else:
            return redirect('login')
    else:
        return render(request, 'blogs/blog_upload.html')

@login_required(login_url='login')
def blog_details(request, the_slug):
    blog = BlogPost.objects.filter(slug=the_slug)
    return render(request, 'blogs/blog_details.html', {'blog': blog[0]})