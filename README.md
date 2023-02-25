# Developer Board Review

A Code Institute course project requirement. You can see the deployed site [here] https://dooco-pp4.herokuapp.com/

[Gitpod] https://github.com/dooco/pp4

User: Dan
password: 


## Project Overview
The aim of this project is to demonstrate skills in developing a Full Stack Application using the Django framework accomplished through a blog syle application where a community of electronic hobbiests post their projects and comment on others.
## Introduction
A hobby electronic and microprocessor development site where users can post articles and can add comments in order to build a community of developers sharing their creations. This blog style website can provide a platform for hobbyists to showcase their electronic and microprocessor projects and connect with other like-minded individuals. Users can post their projects along with detailed descriptions and images allowing other users to learn from and appreciate their work. Additionally, comments and likes can provide a means for users to share feedback, offer advice, and show their support for fellow hobbyists. This can lead to a vibrant community of makers, where users can learn from each other, collaborate on projects, and push the boundaries of hobby electronics and microprocessor development.
## User Experience
### Visitor
1. As a visitor I can view a list of articles on home page so that I can pick out articles I am interested in to read.
2. As a visitor I can click on an article so that I can read its full content.
3. As a visitor I can view articles by category so that I can focus on articles I am interested in.
4. As a visitor I can create an account so that I can post articles or comment on other articles.
17. As a visitor I can load a page of articles and have the option to continue onto next page so that I can view articles and not load too much content in browser.
19. As a visitor I can search posts so that I can narrow my search with keywords used in my search selection.
20. As a visitor I can view about page so that I can find out information on website.
### Registered User

5. As a user I can log into account so that I can add, edit, view or delete my articles and view and comment on other articles.
6. As a user I can use my social account credentials to log in so that I can easily log in
7. As a logged-in user I can create my new article so that I can share information on the platform
8. As a logged-in user I can edit my articles so that I can keep my articles up to date.
9. As a logged-in user I can delete articles I have posted so that I can keep my posts relevant.
10. As a logged-in user I can comment on other user's articles so that I can give my opinion on that article.
11. As a logged-in user I can click a like button below an other user's article so that I can show that I liked their article.
18. As a logged in user I can log out so that other users can log in from my computer.
### Admin
12. As an admin I can view, add, edit, delete posts on platform so that I can act as administrator of the platform.
13. As an admin I can moderate articles and comments on the platform so that I can regulate content on site.
14. As an admin I can edit, add or delete categories available on site so that I can keep site up to date.
15. As an admin I can organise user's articles under different headings so that I can easily see articles and comments.
16. As an admin I can search user's posts and comments so that I can easily access information.
21. As an admin I can add and delete users so that I can have control over users on site.
22. As an admin I can add social account credentials so that users can log in with ease using different social account methods.



# Surface Plane
## Website Design

### Colours used
Colours used include
### Fonts
Fonts used are google Roboto font and 
### Imagery
Hero image on index page is an image from

### The strategy plane
Minimum requirements:

Visitor doesn't need to login to view content but is restricted on adding comments and posting.
The user must be able to sign in and sign out of the site allowing extra functionality.
Admin should see be able to access the admin panel with admin username and password.
There must be a way to manage user posts with full Create / Read / Update / Delete functionality.


### Data Relationship
Only four models are used in this project:
 
 BoardFeature is a class based model which captures most of the date needed for the project. It consiste of a number of charField fields which holds the name, excerpt and maufacturer details. Two of the fields are ForeignKey, author and category which are linked with User auth model and Category model. Two fields, update_on and creatrd_on use DateTimeField models. The slug field contains the slugified versiom of board_name. Special_feature field is a text field which contains a longer text based field that holds the features and description of the article. The like field is a many to many field and holds the relationship between user and BoardFeature.

 Category is a class based model with only five fields. Foreign field 'name' is connected to the category field in BoardFeature. This field hold's a list of categories, which can be added to by admin, to group user posts into common popular categories helping to narrow searching by user to thir most interested category. The slug field is a slugified version of the name field. Body is 

 Reviews

 User Auth

[Database Relationship Table](/static/images/readme/pp4-database-relationship-table.png )







## Scope plane


## Technologies

### Languages used:

- HTML 5
- CSS3
- Python
- Javascript

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
    