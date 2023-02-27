# Developer Board Review

A Code Institute course project requirement. You can see the deployed site [here] https://dooco-pp4.herokuapp.com/

[Gitpod] https://github.com/dooco/pp4

User: Dan
password: 


## Project Overview
The aim of this project is to demonstrate skills in developing a Full Stack Application using the Django framework accomplished through a blog syle application where a community of electronic hobbiests post their projects and comment on others.
## Introduction
A hobby electronic and microprocessor development site where users can post articles and can add comments in order to build a community of developers sharing their creations. This blog style website can provide a platform for hobbyists to showcase their electronic and microprocessor projects and connect with other like-minded individuals. Users can post their projects along with detailed descriptions and images allowing other users to learn from and appreciate their work. Additionally, comments and likes can provide a means for users to share feedback, offer advice, and show their support for fellow hobbyists. This can lead to a vibrant community of makers, where users can learn from each other, collaborate on projects, and push the boundaries of hobby electronics and microprocessor development.
## User Stories
[Project ]
### Visitor
1. As a visitor I can view a list of articles on home page so that I can pick out articles I am interested in to read.
2. As a visitor I can click on an article so that I can read its full content.
3. As a visitor I can view articles by category so that I can focus on articles I am interested in.
4. As a visitor I can create an account so that I can post articles or comment on other articles.
17. As a visitor I can load a page of articles and have the option to continue onto next page so that I can view articles and not load too much content in browser.
19. As a visitor I can search posts so that I can narrow my search with keywords used in my search selection.
20. As a visitor I can view about page so that I can find out information on website.
23. As a visitor I can visit website so that I can use features with ease and without needing knowledge on how to run in development mode.
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
Colours used include:
Main background colour: #F9FAFC
light background background colour: #445261
masthear text colour: #445261
card image flash colour: #23BBBB


### Fonts
Fonts used are google Roboto font and 
### Imagery
Hero image on index page is an image from

### The strategy plane
Minimum requirements:

Visitor doesn't need to login to view content but is restricted on adding comments, likes and posting.
The user must be able to sign in and sign out of the site allowing extra functionality.
Admin should see be able to access the admin panel with admin username and password.
There must be a way to manage user posts with full Create / Read / Update / Delete functionality.


### Data Relationship
Only four models are used in this project:
 
 BoardFeature is a class based model which captures most of the date needed for the project. It consists of a number of CharField fields which holds the name, excerpt and maufacturer details. Two of the fields are ForeignKey, author and category which are linked with User auth model and Category model. Two fields, update_on and created_on use DateTimeField models. The slug field contains the slugified versiom of board_name. The special_feature field is a text field which contains a longer text based field that holds the description of the article. The status field is an Integer field that holds the status, draft or published, controled by admin and determines if post can be seen on home page. The like field is a many to many field and holds the relationship between user and BoardFeature.

 Category is a class based model with only two fields. The field 'title' is a CharField and holds the name of the category. This field hold's a list of categories, which can be added to by admin, to group user posts into common popular categories helping to narrow searching by user to thir most interested category. The slug field is a slugified version of the name field.

 Review is a class based model with only five fields. Foreign field 'board' is connected to the BoardFeature model. This field hold's a list of reviews, which are displayed under the posts description on detail page. The name field contains the name of the user that posted the comment. The slug field is a slugified version of the name field. The body field is a TextField that holds the content of the review from user. The created_on field is a DateTimeField holding the date that the comment was created. The approved field is a BooleanField which, controled by admin, determines whether review is displayed.

 User Auth is a system model referenced in the applications models that holds essential information on user name, email, password, permissions, group status etc. which makes it possible to interact with users with ease.

[Database Relationship Table](/static/images/readme/pp4-database-relationship-table.png )





## Scope plane
### Minimum requirements:
- Design a Front-End for a data-driven web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of user interactions.
- Implement custom HTML and CSS code to create a responsive Full-Stack application consisting of one or more HTML pages with relevant responses to user actions and a set of data manipulation functions.
- Build a database-backed MVC web application that allows users to store and manipulate data records about a particular domain.
- Design a database structure relevant for your domain, consisting of a minimum of one custom model.
- Use an Agile tool to manage the planning and implementation of all significant functionality.
- Document and implement all User Stories and map them to the project within an Agile tool.
- Write Python code that is consistent in style and conforms to the PEP8 style guide and validated HTML and CSS code.
- Include sufficient custom Python logic to demonstrate your proficiency in the language.
- Include functions with compound statements such as if conditions and/or loops in your Python code.
- Write code that meets minimum standards for readability (comments, indentation, consistent and meaningful naming conventions).
- Name files consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatibility.
- Document and implement all User Stories within the Agile tool and map them to the project goals.
- Document the UX design work undertaken for this project, including any wireframes, mockups, diagrams, etc.,created as part of the design process and its reasoning. Include diagrams created as part of the design process and demonstrate that these have been followed through to implementation.

### Agile Planning
Agile practice is an iterative approach to project management that encourages collaboration within the development team and with client. In this way, software development is achieved in small, incremental steps, with each step delivering a working piece of software that can be tested and appraised by client. Several stages, including planning, design, development, testing, and deployment are incorporated into the agile approach. At each stage, the team works closely with the client to ensure that the output meets their requirements.

The project had 8 milestones. Milsestones were set up as headings to group user stories into and loosly have achievemnet goals that could be reached.
#### Project initialisation
- Install django, gunicorn, heroku, psycopg2, dj3-cloudinary-storage, summernote, dj-database-url, django-allauth, django-crispy-forms
- Create env.py file to hold private information not to be pushed to github.
- Create cloudinary account and bring over credentials to settings and env.py
- Create account in elephantsql and use 'tiny turtle' plan and bring over credentials to heroku
- Log into Heroku and create bew project, applying set-up variables and credentials from elephantsql.
- Create Procfile file and apply gunicorn details. 
- Setting up the database structure in settings.


#### User accounts setup
- Set up AllAuth
- Set up social accounts google, facebook and github
- Get credentials from applications API
- Make use of Raymond Penners github user [login templates]https://github.com/pennersr/django-allauth
- Style login, logout and signup templates.
- Creating the superuser login.

#### Model Design and Creation
- Plan out models and fields required.
- Map out relationships between models
- Ceate models in models.py and add required definitions.
- Plan logic to be applied in class and definitions in views.py
- Create views.py classes and functions.
- Connect urls.py paths to views and templates.
- Create forms for posts and comments.


#### Home Page
- Create base.html
- Create header with links to bootstrap, css stylesheet, fonts, fontawsome. 
- Create navbar and include logic to display user and logout option or where no user is loge in an option to log in.
- Create footer, add javascript code to deal with messages.
- Create home (index.html)
- manual test output along with coding.

#### Detail Page
- Create detail page (board_detail.html).
- Link page with add, edit and delete functions.
- Insert logic to ensure only users that own posts hav permission to edit and delete posts.
- Insert logic to ensure only loged in users can create posts and comment on other posts.
- manual test output along with coding.

#### Admin
- Set up admin pannel to be able to moderate posts and comments.
- Add social allauth accounts to admin area.
- Add credentials from social account providers.

#### Test
There are many ways of testing code, the most common are manual testing and automated testing. In order to complete manual testing, a list of all the features site has, the different types of input it can accept, and what are the expected outcomes. Each time there's a change to code, the test method needs to go through every item on that list and test it. Automated testing can be achieved by a script and  instead of manually going through each test a built in python test function itterates through the pre-programmed tests.


[Manual User Experience Tests](https://res.cloudinary.com/dklz0mnqm/raw/upload/v1677482969/pp4-validation-excel_lxyanr.xlsx)
#### Deploy to Heroku

 


## Technologies

### Languages used:

- HTML 5
- CSS3
- Python
- Javascript
### Frameworks and Libraries used:
- [Django](https://djangoproject.com) : framework used to connect backend with frontend of project.
- [django-allauth](https://django-allauth.readthedocs.io/) :  Supports user authentication, loging in and out and registration. 
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io) :  Renders behavior of your Django forms in a very elegant and DRY way.
- [summernote](https://summernote.org/) : WYSIWYG Editor on Bootstrap Summernote is a JavaScript library that helps you create WYSIWYG editors online.
- [dj-database-url](https://pypi.org/project/dj-database-url/) : Django utility allowing utilisation of the 12factor inspired DATABASE_URL environment variable to configure Django application.
- [psycopg2](https://www.psycopg.org/docs/) : A database adapter for the Python programming language.
- [Google Fonts](https://fonts.google.com/) : Library of fonts.


### Databases used:
- [PostgreSQL](https://postgresql.org) Used on deployed site for storing all the data.
- [SQLite](https://swlite.org) Used during development and testing.




### Programs used: 

- [Git](https://git-scm.com/) : Git is a free and open source distributed version control system.
- [GitHub](https://github.com/) : A code hosting platform for version control and collaboration.
- [Gitpod](https://www.gitpod.io/): A cloud development environment for teams to efficiently and securely develop software.
- [Bootstrap](https://getbootstrap.com/) : Development framework for the creation of websites to enable responsive development of mobile-first websites.
- [Cloudinary](https://cloudinary.com/) :  Image and video storage and management solution for websites . 
- [ElephantSQL](https://customer.elephantsql.com/) : Installs and manages PostgreSQL databases.
- [W3C](https://validator.w3.org/) : Develop protocols and guidelines that ensure long-term growth for the Web.
- [Pep8CI](https://peps.python.org/pep-0008/) : Validation of Python.
- [Heroku]() : A platform enabling developers to build, run, and operate applications entirely in the cloud. 
- [Balsamiq Wireframes](https://balsamiq.com/) : A user interface design tool for creating wireframes.
- [Favicon.io](https://favicon.io/) : Favicon generator 
- [Font Awesome](https://fontawesome.com/) :  Icon library and toolkit.
- [Lucidchart](https://www.lucidchart.com/) : To create flowcharts & diagrams online.


--------

## Testing





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
    