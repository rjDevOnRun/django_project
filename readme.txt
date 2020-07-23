	create project/website
- django-admin startproject "project-name"

	run server
- python manage.py runserver


	create a webapp inside website
- python manage.py startapp blog

- Add ActionMethods to views.py
- Add new file (urls.py) to blog app
	- add url routing for blog methods
	  eg: 	# format: name, view.method name, name
    		path('', views.home, name='blog-home'),

- Add blog urls-patterns to be included in the main application
  by adding/including to the main-application: urls.py file
	
	path('blog/', include('blog.urls')),  # << point to the app 'blog's urls

- Create 'templates/blog' directory in blog app. it should be "templates/app-name"
- Add html templates to this folder.
- Add the AppConfig to main application. open "apps.py" from 'blog'.. copy class-name
  ... open 'settings.py" from website-app and add the name under "INSTALLED_APPS"..
	'blog.apps.BlogConfig' [format:  app-name.app.app-Config-name]

- to load a template to views... use "render(request, 'blog/home.html')"
		