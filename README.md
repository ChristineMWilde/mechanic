
# Christine Wilde's Stream Three Project

[Motorholics URL](https://motorholics-app.herokuapp.com/)

Please note the entire project is described under the "Documentation for project" folder in the word document named FinalProjectStreamThree.doc.

The goal of the stream three project is to build a Django project composed of multiple applications (apps). The Django project should include an ecommerce element to it, establish a login/logout authentication mechanism for users to the Website and connect to a database to store Website data.

Project subject:

After considering a few ideas the Motorholics Website was born, aiming to connect all users and car enthusiasts to car mechanics for advice and assistance with any car issues or subject interest.

This meant that the Website should contain a discussion feature for all users to comment on. It also allows scope for the mechanics to write any articles of interest to further educate users.  Therefore, a forum and a blog was decided on.

The Website includes the following technologies:

* Django 1.11.15 - (Framework to create Models, Views, Templates and URL links)
* SQLite database - (Open source SQL database included with Django)
* HTML5, CSS, JavaScript, Bootstrap - (Front-end technologies)
* Disqus - (Global comments/discussion platform/API)
* Stripe - (Payment processing API)
* Tinymce/Font Awesome (WYSIWYG HTML editor and Font Awesome for styling using icons)
* Car Blog - (mechanics car topics)
* Car Forum - (mechanics and users discussion forum � help site!)
* User Registration - (register to ask for advice via a small subscription)



Using the technologies above the below Website features were achieved:

1. ## Home page
This includes Bootstrap nav bar with car icon, a car cover image and an "About Us" button using Flatpages.

2. ## Motorholics Blog page
The Blog page lists various car subjects with the ability to create a �New Post�.

3. ## Motorholics Forum page
The Motorholics car forum lists all the threads to specific subjects started by the Motorholics mechanics (staff).  

4. ## Motorholics Registration page
User registration to subscribe on a monthly basis to the Website. 

5. ## Login/Logout features
For members to login and out of the Motorholics Website.

### Installation

The below table explains how to deploy the application.



```sh

1. For the live version please go to the Heroku deployed app at: https://motorholics-app.herokuapp.com/
2. To run locally download all files from: https://github.com/ChristineMWilde/mechanic.git 
3. All requirements are found in the requirements.txt file.
4. Please note that the Media/Image Upload and Disqus functionality only works for the dev environment.
4. Please go to the project root and run: python manage.py runserver.
5. Please read "FinalProjectStreamThree.doc" for detailed information on this project. This document is found under the folder "Documentation for project" folder.
```

### REUSABLE APPS are found here: 
* [accounts app](https://github.com/ChristineMWilde/reusable-accounts-app.git)

* [blog app](https://github.com/ChristineMWilde/reusable-blog-app.git)

* [forum/threads app](https://github.com/ChristineMWilde/reusable-threads-app.git)

* [polls app](https://github.com/ChristineMWilde/reusable-polls-app.git)

TESTING observations:

  * Development tool can be very useful as a 'recorder' to present the source files/code that the Website is using.
  
  * Any updates to HTML element ID's should be thoroughly investigated across all files that may have an effect on them.

  * The Django framework provided a great consolidated view of all python, static and template files working together.

  * An API will be required for Disqus and Media storing files in order to run in the staging environment.

