from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Alson',
        'title': 'Blog Post 1',
        'content': "What is reality? Is it what we perceive with our eyes? "
                   "If so, then wouldn't a dog's reality be different then ours? "
                   "Then which reality would be real?",
        'date_posted': 'February 28th, 2020'
    },
    {
        'author': 'John Smith',
        'title': 'Blog Post 2',
        'content': 'How do you parallel park?',
        'date_posted': 'February 29th, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




