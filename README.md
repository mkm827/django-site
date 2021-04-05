#Programmershub-Django App

You can view a working version of this app here at -----  http://myprogrammershub.com

PyShop1 == django-site     #dummy name for the main project file which contains the url.py, settings.py ,wsgi.py which are responsible for binding the project together.
products == blog-app       #blog directory that manages different functionalities such as updating ,adding, deleting etc for the posts and organising them on the home page.

The complete app was deployed using Apache2 on Ubuntu server but you can deploy it on Heroku to play it.


It is best to use the python virtualenv tool to build locally
Then visit http://localhost:8000 to view the app.

![Untitled](https://user-images.githubusercontent.com/79550971/113526146-12431d80-9576-11eb-9308-8a3ec2526663.png)

The EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in the above image are personal email id and password used to send email for password reset functionality from admins personal GMAIL. So you can change it to your email and password while running the app for yourself, the proper place to find the global varibles is   PyShop1 >> settings.py >> bottom_of_the_page.

HTML FILES: 1. Base.html in the templates folder.
            2. Specific htmls files in  different template app folders.
            
CSS FILE: products >> static >> products >> main.css
