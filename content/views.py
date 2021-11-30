from django.shortcuts import render, redirect
from .models import BlogPost, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    blogs = BlogPost.objects.all()
    context = {
        "blogs": blogs,
        "tags": {
        'Finance': 'Finance',
        'Fashion': 'Fashion',
        'Politics' : 'Politics',
        'Sports' : 'Sports',
        'Travel' : 'Travel',
        'Lifestyle' : 'Lifestyle',
        'Inspiration' : 'Inspiration',
        'Environment' : 'Environment',
        },
        "blogs_recent": blogs,
        "blogs_highlight": blogs[0],
        "blogs_main": blogs[0],
        "blogs_editor": blogs,
        "blogs_trending": blogs[0:2],
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
