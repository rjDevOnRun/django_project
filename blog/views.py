from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'RobyJ',
        'title': 'Blog post 1',
        'content': 'First post contents. This is the contents section',
        'date_posted': 'July 15, 2020'
    },

    {
        'author': 'NeilDeGrass',
        'title': 'Blog post 2',
        'content': 'Second post contents. This is the contents section',
        'date_posted': 'July 18, 2020'
    },

    {
        'author': 'StephenHwakins',
        'title': 'Blog post 3',
        'content': 'Third post contents. This is the contents section',
        'date_posted': 'July 20, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    # render(request, template_path, data-context)
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    # return HttpResponse('<h1>About Page</h1>')