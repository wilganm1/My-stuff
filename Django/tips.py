Django is a python-based web frameword that makes it easy to create
websites in an easy automated fashion. It is built to be very
organized in it's' setup. 

Django works by creating a project (think website) and having
multiple apps (pages/functions) that all work together. This is 
done by creating many folders within folder.

Django works by getting requests from the user or the internet
(typing in a url into the browser) and sending that request 
through multiple files to end up at a function for a 
corresponding view. Views = web pages.

In the command line, cd into the folder you want your project
to live, then type in django-admin startproject {name of project}.
then cd into that project directory. 

To create a new app, type in python manage.py startapp {app name}

If you ever make a new app in the project you always add it to the
setting.py file in the main project folder like this:
		INSTALLED_APPS = [
			'appname.apps.AppnameConfig',
		]
   You'll' have to spcify which app it is.
	Example: a blog.
		INSTALLED_APPS = [
		'blog.apps.BlogConfig',
		]

To make a page appear you have to write a function for it in your
project's views.py'file with a request to an html file if you
made a custom web page. 

Example:
	from django.shortcuts import render

	# Create your views here.
	def about(request):
		return render(request, 'blog/about.html', {'title': 'About'})

base.html will be a template for files that will have the
same layout for certain html sections like headings or titles
or major divs.
	Use blocks to create templates to fill in information
		{% block content %}{% endblock %}    #This is where python comes into play. It will automate this type of html stuff.

	Put stuff between the blocks that you want every page/post
	to have. like <h1> or <p>.

{% extends 'blog/base.html' %}
{% block content %}
	{% for post in posts %}
	<article class="media content-section">
	  <div class="media-body">
	    <div class="article-metadata">
	      <a class="mr-2" href="#">{{ post.author }}</a>
	      <small class="text-muted">{{ post.date_posted|date:'' }}</small>
	    </div>
	    <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
	    <p class="article-content">{{ post.content }}</p>
	  </div>
	</article>
	{% endfor %}
{% endblock content %}

Go to https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#date
to find code to format dates.

Go to https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template
and copy the head portion and put that in your head portion
in base.html. Then do the same for the javascript and put that
underneath the block content. Then put the block content inside
it's own div with the class "container"'.

Within the outer app folder create a new subdirectory called static
then create another folder inside it called blog. Within that blog folder
create a file called main.css. This is where you will put the css
code you want for the blog. You reference it in base.html

To access the css in base.html, write a link to it:
  <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css'%}">

  Also put {% load static %} at the very top of the page above
  the DOCTYPE

-Creating an administrator.
   Go to your command line and type in python manage.py createsuperuser
    If you get errors just run python manage.py makemigrations
    and python manage.py migrate

   -create a user name and password 


Django has an ORM, object relational mapper. Can access our
database in an object-oriented way.



How to handle users:
 Creating a user application to keep track of users.
	 Go to the project's' command line and type in python 
	 manage.py startapp users. This will create a new folder 
	 for your users application. Add this app your the settings
	 file in the main project directory: 'users.apps.UsersConfing',
  
  In the views.py file of the users app write in 
  the following code to handle html creation.
		from django.shortcuts import render, redirect
		from django.contrib.auth.forms import UserCreationForm #creates html from form
		from django.contrib import messages

		# Create your views here.
		def register(request): #create a form that will be a template
			if request.method == 'POST':
				form = UserCreationForm(request.POST)
				if form.is_valid():
					username = form.cleaned_data.get('username')
					messages.success(request, f'Account created for {username}!')
					return redirect('blog-home')
			else:
				form = UserCreationForm()
			return render(request, 'users/register.html', {'form': form})
	Then create a new directory in users app called templates, a 
	subdirectory in that called users, and create a file called 
	register and add this in:

		{% extends 'blog/base.html' %}
		{% block content %}
			<div class ='content-section'>
				<form method="POST">
					{% csrf_token %}
					<fieldset class="form-group">
						<legend class="border-bottom mb-4">Join Today</legend>
						{{ form.as_p }}
					</fieldset>
					<div class="form-group">
						<button class = "btn btn-outline-info" type="submit">Sign Up</button>
					</div>
				</form>
				<div class="border-top pt=3">
					<small class="text-muted">
						Already Have An Account? <a class="ml-2" href="#">
						Sign In</a>
					</small>
					
				</div>
			</div>
		{% endblock content %}


Use crispy forms to style css and add in tags.
		pip install django-crispy-forms
	Now tell django that it's installed'. Go to the projects settings
	file and go to INSTALLED_APPS add in 'crispy_forms', then at
  the bottom of the file add in this:
  		CRISPY_TEMPLATE_PACK = 'bootstrap4'

Create a user authentication log in page.
	In the main project's' urls file import:
		from django.contrib.auth import views as auth_views
   Then, add this to the urlpatterns list:
   	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
  Next you have to create the templates for the page. Go to the users
  subdirectory inside the users app directory and create news file called login.html and logout.html

  	To creat the login.html file, just copy the register.html file and change the legend and <a> links
  	to say things like: <legend>Log in</legend>

  	Make sure you link to the register page if the user clicks, "Need an account?"
  	To do that use this:
  	    the href="{% url 'register' %}"
		This will link to the register.html file. Also within the register.html file
		link to the login page using {% url 'login' %}  	
		Since both pages are in the same directory it will automatically go to the correct file.

	Once that's done' go to the project settings.py file and create a new setting
		LOGIN_REDIRECT_URL = 'blog-home'
	 This will redirect the user back to the home page when they've signed in.'

