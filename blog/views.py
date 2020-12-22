from django.shortcuts import render
#from django.http  import HttpResponse
# Create your views here.
posts = [
		
		{
		'author' :'Masud',
		'title' :'Blog Post-1',
		'content' :'Are you running yet?',
		'date_posted' :'Dec 23,2020'
		},

		{
		'author' :'John',
		'title' :'Blog Post-2',
		'content' :'Are you doing yet?',
		'date_posted' :'Dec 23,2020'
		}
]

def home(request):
	#return HttpResponse('<h1>Blog Home </h1>')
	context = {
		'posts' : posts #posts is a key here,it will be now accessible from template-> home.html
	}
	return render(request, 'blog/home.html', context) #goes to blog->templates->blog->home.html
def about(request):
	#return HttpResponse('<h1>About </h1>')
	return render(request, 'blog/about.html',{'title' : 'About'})