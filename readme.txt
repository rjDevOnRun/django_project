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


-- ADMIN ------------------------------------------------

-- prepare database (collect TODOs for database actions)
    python manage.py makemigrations

-- make changes to database
    python manage.py migrate

* NOTE: makemigrations/migrate every time
        you change/modify models or db

        in migrations folder we can view the
        impacted changes/actions of migrate

        checkout, 'app-name'.'migration_num'.py file
        check sql execute to db:
            python manage.py sqlmigrate blog 001
                                     (app-name) [number]

- to create Admin user:
    python manage.py createsuperuser
        SuperAdmin: Test@123.
        TestUser: Testing321
-- ------------------------------------------------------

-- SHELL
    we can create classes, posts, or any objects using
    the Shell environment

    python manage.py shell
    exit() <<-- to exit

        app.models          model-name
    from blog.models import Post
    from django.contrib.auth.models import User

    Get all models:
    User.objects.all()
    Post.objects.all()


        filters:
        User.objects.first()
        User.objects.filter(username='TestUser')

    Capture in a variable:
    user = User.objects.filter(username='TestUser').first()

    Add a Post:
    post_1 = Post(title='Blog 1', content='First post from Shell', author = user)
    post_1.save()  <<-- saves post to Db







		