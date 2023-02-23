# Developer Board Review

A Code Institute course project requirement. You can see the deployed site [here] https://dooco-pp4.herokuapp.com/
## Project Overview
The aim of this project is to demonstrate skills in developing a Full Stack Application using the Django framework accomplished through a blog syle application where a community of electronic hobbiests post their projects and comment on others.
## Introduction
A hobby electronic and microprocessor development site where users can post articles and can add comments in order to build a community of developers sharing their creations. This blog style website can provide a platform for hobbyists to showcase their electronic and microprocessor projects and connect with other like-minded individuals. Users can post their projects along with detailed descriptions and images allowing other users to learn from and appreciate their work. Additionally, comments and likes can provide a means for users to share feedback, offer advice, and show their support for fellow hobbyists. This can lead to a vibrant community of makers, where users can learn from each other, collaborate on projects, and push the boundaries of hobby electronics and microprocessor development.
## User Experience
### Visitor
* As a visitor I want to be able to view articles on electronic projects.
* As a visitor I want to be able to select an article I am interested in and view its full content.
* As a visitor I want to be able to select a category of priject I am interested in and view projecte in that category.
### Registered User
* As a visitor I want to be able to register for an account so that I can post articles.
* As a registered user I want to be able to post articles on projects I am working on or post articles on electronic kits I am interested in.
* As a registered user I want to able to easily log in and out of my account so that I can access my posts.
* As a registered user I want to be able to comment and like other user's articles, to provide feedback on their posts.
* As a registered user I want to be able to add an image to my post.
* As a registered user I want to be able edit and delets my posts.
### Admin
* As an admin I want to be able to log in and view uses, groups, social accounts and models.
* As an admin I want to be able to add and delete users and social accounts.
* As an admin I want to be able to search for posts.
* As an admin I want to be able to view posts under different headings.
* As an admin I want to moderate posts and comments.
* As an admin I want to be able to add, edit, delete posts.
* As an admin I want to be able to add and delete categories for users to assign their projects to.

## WEBSITE DESIGN
### The strategy plane
Minimum requirements:

Visitor doesn't need to login to view content but is restricted on adding comments and posting.
The user must be able to sign in and sign out of the site allowing extra functionality.
Admin should see be able to access the admin panel with admin username and password.
There must be a way to manage user posts with full Create / Read / Update / Delete functionality.
The customer must have information about the location of the restaurant.
The customer must have links to the address (map location), telephone number, email and social media links should be in the footer
If time permits, or for future development

A separate contact page.
Automation to delete bookings when there are no-shows, or the reservation date is in the past.
Ability to edit menu items using a styled form.

#### 






## Scope plane


## Technologies

### Languages used:

- HTML 5
- CSS3
- Python
- 

### Libraries and Programs used: 

- Git, for version control.
- GitHub, for storing code and deploying site.
- Gitpod, Used to build project and editing the code.
- Django, a python based framework to develop this project
- Bootstrap, for HTML design templates.
- Cloudinary, to store images. 
- Figma, to mockup the design.
- ElephantSQL, database through Heroku.
- W3C for validation of HTML and CSS.
- Pep8CI for validation of Python.
- Summernote, for usage in the admin panel.
- Heroku, for deploying the project. 
- Convertion, for converting JPG to AVIF. 


--------

## Testing


### Project set-up and deployment steps
### Create Repository



#### To create a new repository:

-  Log in to GitHub.
-  Click on 'repositories'.
-  Click on 'new' button, which create a new repository.
-  Select CodeInstitute template from the dropdown menu. 
-  Name project by adding title, 'PP4'.
-  Select 'Add Read.Me'.
-  Click 'create repository'.
-  Open repository and click green 'GitPod' button to create workspace.

#### Install Django 

- Install Django: pip3 install 'django' 
- Create project: django-admin startproject PP4 .
- Create app: python3 manage.py startapp joinus
- Add app to installed settings: INSTALLED_APPS = [ ... 'django.contrib.staticfiles', 'joinus',]
- Migrate: python3 manage.py migrate
- Run http server to confirm installation was successful: python3 mange.py runserver
#### Install libraries
- Install Cloudinary: pip3 install cloudinary

- Create requirements

Connect to Heroku and ElephantSQL
- Create Heroku App
- Create new instance on Elephant SQL and copy DB url
- Create env.py, adding the secret key. Ensure env.py is in gitignore
- Import env.py into Settings, and edit secret key accordingly
- Comment out original databases in Settings
- Connect to ElephantSQL
- Make migrations
- Test connect to ElephantSQL was successful
- Add config vars to Heroku

Connect to Cloudinary
- Add Cloudinary API environment variable to env.py
- Add Cloudinary API environment variable to Heroku Config Vars
- Add DISABLE_COLLECTSTATIC to Heroku config vars
- In Settings,  "Installed Apps", add cloudinary_storage and cloudinary

Set up Directories and deploy
- In Settings, under STATIC_URL add STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage', and add STATICFILES_DIRS, STATIC_ROOT, MEDIA_URL, DEFAULT_FILE_STORAGE
- Add Templates Directory under BASE_DIR in settings, and fill in brackets for "DIR": []
- Add Heroku host name to ALLOWED_HOSTS
- Add top level directories
- Add a procfile
- In Heroku, link to GitHub as the deployment method

#### Final deployment

- In settings, 
    - Set DEBUG to False. If this is not done, cloudinary images won't be served and traceback error messages will be shown to the user (which can also reveal credentials that can benefit hackers).
- Update Heroku configuration settings. Remove CollectStatic.
    