from django.shortcuts import render

# Create your views here.
posts = [
	{
		'author': 'venky',
		'title' : 'Post 1',
		'content': 'First '
	},

	{
		'author': 'venky',
		'title' : 'Post 1',
		'content': '2nd '
	}
]

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'Venky\'s Blog'})