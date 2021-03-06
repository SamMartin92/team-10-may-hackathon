# Connectify

Here is a link to the live project. (https://connectify-nka.herokuapp.com)

This website was created for Soda social and Code institutes Getting connected Hackathon.
Coders were Nat, Rian, David, Debbie and Sam.

![Image showing the website displayed on different screen sizes](static/images/responsive.png)

## Contents 

- [Aim](#aim)
    * [Cause](#reason)
- [User Experience (UX)](#user-experience-ux)
   * [Strategy](#strategy)
   * [User Stories](#user-stories) 
   * [Scope](#scope)
      + [Current Features](#current-features)
      + [Features to implement in the future](#features-to-implement-in-the-future)
   * [Structure](#structure)
   * [Skeleton](#skeleton)
   * [Surface](#surface)
     + [Colour Scheme](#colour-scheme)
     + [Imagery](#imagery)
- [Technologies](#technologies)
   * [Languages used](#languages-used)
   * [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

- [Challenges](#challenges)

- [Testing](#testing)
   
- [Deployment](#deployment)
   * [Creation](#creation)
   * [Forking](#forking)
   * [Clone](#clone)
   * [Setting Up Project](#setting-up-project)
   * [Heroku Deployment](#heroku-deployment)

- [Credits](#credits)
   * [Code](#code)
   * [Content](#content)
   * [Media](#media)
   * [Acknowledgements](#acknowledgements)


## Aim

### Reason
Loneliness is not treated, or viewed as a mental health issue but is known as a large contributor towards further mental health issues. <br>
Whilst lonliness affects people in different ways, this can influence depression, anxiety, low self-esteem, sleep problems and increased levels of stress.<br><br>
30.9% of adults (survey of 7.4 million adults) reported their well-being has been effected by the feeling of being lonely over the past 7 years.
[stats taken from https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/bulletins/coronavirusandlonelinessgreatbritain/3aprilto3may2020]

### Target
To support connectivity between people identifying as lonely, we aimed to expand the options of contacts within a virtual network fo people.

Ensuring a positive conversation, we decided the platform is to be made for small groups determined by their mental health strengths. The group will consist of 1 person from each category, opening the conversations/post to different perspectives.

### Research
Our methodology was inpsired by myers-briggs questionnaire(https://eu.themyersbriggs.com/, using ratings of feelings towards a set topic.

Categorizing for stages of mental health expanded our selection to a broad area too wide for creating small groups/pods of users. Refining our categories, we swapped the focus from after-effects of mental health, to the beaviours of a positive mental health. This is broken down to 5 factors;
1. Positive Self-esteem
2. Sense of Belonging
3. Sense of Purpose
4. Positive Outlook
5. Autonomy

### Purpose

The application is designed to present the user with a questionnaire after creation of an account.

Post-results, our application will display the mental strengths to the user and allocate to a group of people from different categories. 
Questionnaire is only applicable once to the user, this will not be required on each login.

This unlocks the apps feature to the user, allowing them to blog a post within their selected group.
Each group will consist of at least one other person from each category. This method has been prefered to encourage different perpectives of a conversation, keeping a positive flow on the selected topic.

As a norm, people are reserved with making conversations with new people, even moreso since the pandemic of COVID-19 rushed across the globe causing a world-wide shutdown of any social life. To break the chain of interacting with people you know, this application is designed to introduce you to a new host of people you are likely to collaborate and support with.


## User Experience (UX)

   ### Strategy 
   - User goals 
       * As a user I want to be able to connect with people.
       * As a user I want an attractive easy to use site.

   - Site owner/ business goals
       * As the site owner I want my site to be responsive to different screen sizes.
       * As the site owner I want my site to be accessible to my visitors.

   ### User Stories

   - #### Unregistered Visitor
      * As an unregistered user I want to be able to find information about the purpose of the site.
      * As an unregistered user I want to be able to find helpful resources.
    
   - #### Registered First Time User (in addition to above)
      * As a registered first time user I want to take a personality test so I can get recommendations on how to improve different traits.

   - #### Registered Returning User Goals
      * As a returning visitor, I want to share my feelings on the blog.
      * As a returning visitor, I want to be able to edit my blog post.
      * As a returning visitor, I want to be able to delete my blog post.
      
   - #### Registered Frequent User Goals
      * As a frequent user, I want to be able to comment on other peoples blogs.

   - #### Admin/Superuser goals
      * As admin, I want to be able to inactivate a user if they have been abusive or inapropriate.
      * As admin, I want to be able to remove a blog post
 

   ### Scope

   Within project conception, a list of features were compiled, these were the scored 
   between 1 & 5 for importance and feasibility/ viability which then decided which features 
   could be included for initial launch.    

   #### Current features 

-   Responsive on all device sizes

-   Accessible 

-   Easy to navigate (Single use learning)

-   Interactive elements

-   Social Links 

-   Logged in users can take a quiz and get suggestions based on the result.

-   Users can access helpful resources.

-   Logged in users can contribute to a community blog, editing and deleting their own posts and commenting on other posts.

-   Admin can delete posts and comments and inactivate users if required via the admin portal.


   #### Features to implement in the future

- Ability to contact owner via contact page.

- Profile pages

- Users to be able to contact other users via users preferred social media.

- Users to get recommended connections based on their quiz result. 

- Add delete and edit functionality to comments.

### Structure

-   Created a database schema using [GraphizOnline](https://dreampuf.github.io/GraphvizOnline/), as per Emmets instructions on [slack](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1642276160282900) 

     ![image showing database schema](static/images/database.png)

### Skeleton 

Wireframes were created on Balsamiq (see links below)

* [Mobile](DT-WIREFRAMES.md)


### Surface

 -  #### Colour Scheme

    ![image showing database schema](static/images/color-palette.png)
          
-   #### Imagery

    The images seen on the site were chosen as they show people positively connecting via their devices.
    
## Technologies 

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

1. [Bootstrap v5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/) - Bootstrap was used for the initial layout and styling before customising it.
2. [Google Fonts](https://fonts.google.com/)
    - Google fonts were used to import the font used.
3. [Font Awesome](https://fontawesome.com/)
    - The icons used throughout.
4. [Git](https://git-scm.com/)
    - Version control.
5. [GitHub](https://github.com/)
    - For storing project.
6. [Gitpod](https://www.gitpod.io/)
    - Used for editing my code.
7. [Diagrams.net](https://www.diagrams.net/)
    - Wireframe creation
8. [GraphizOnline](https://dreampuf.github.io/GraphvizOnline/)
9. [Am I responsive](http://ami.responsivedesign.is/)
    - This was used to generate the image at the top of this README.
10. [Chrome devtools](https://developer.chrome.com/docs/devtools/)
    - This was used massively throughout development to troubleshoot, try out changes before 
   changing code, to test responsiveness and for testing performance of the final site with lighthouse. 
11. [jQuery](https://jquery.com/)
    - Required for some of the bootstrap elements such as collapsibles, modal and tooltips.
12. [Heroku](https://dashboard.heroku.com/apps)
    - For deploying the application
13. [Postgres](https://www.postgresql.org/)
    - Database used for our data
14. [Django](https://www.djangoproject.com/)
    - Framework for building applications.
15. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    - Used to generate secret key

## Challenges 
 - Deploying to heroku took longer than expected. Installed whitenoise and added STATIC_ROOT which I seemed to have missed. In addition the python version was causing an issue, so created a runtime.txt which was recommended on slack overflow.
 - Ensuring all links to different parts of site were correct. At one point we had duplicate nav links, think this was due a merge conflict.
 - Slug wasn't being filled in when I created a blog post and so I imported slugify and used that to assign the slug field.


## Testing

Tested as we developed and everything seemed to be working upon deployment. Ran out of time to a do a proper thorough testing event prior to submission.

## Deployment

 - ### Creation 

    I created this repository by:<br>
    (a) Logging into Github and clicked the green new button.<br>
    (b) I selected the code institute template, input a repository name and clicked the green create repository button.<br>
    (c) Opened new repository and clicked green Gitpod button to create a workspace in Gitpod for editing.

  - ### Forking
    (a) To fork my project sign in to Github and go to [repository]()<br>
    (b) Above and to the right of the settings there are three options and the far right one says Fork, select this.<br>
    (c) The fork is now in your repositories.

  - ### Clone
    To clone my project sign in to Github and go to [repository]()<br>
   [Setting Up Project](#setting-up-app) and [Heroku Deployment](#heroku-deploment) for more information about what will be required to run project.

    *  Clone using command line 
        +  Next to the green Gitpod button is a button that says code, select this. There is a few options as to how you 
        would like to clone, if you choose https, SSH or Github CLI, select the clipboard icon to copy the URL.
        +  In your workspace that you've created, in the terminal , type git clone, paste the URL and enter.

    *  Desktop Github
        + If you choose to clone by selecting open with desktop Github, it will guide you through the clone with prompts.<br>

    For more information or troubleshooting see the Github documentation 
    [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository)

- ### Setting Up Project
   
    - Install requirements in terminal using pip3 install, see requirements below. If you have cloned my project you can use pip3 install -r requirements.txt which will install everything for you.
    - Create a SECRET_KEY for django to use. I used [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) for this. My settings.py file is set up to collect keys from the environment so name your variables accordingly. In github you go into settings from your dashboard and then variables. And add the following. You can complete the rest when you go through these sections. DEVELOPMENT value is set to True. Scope you can set to your repository name meaning its only accessible by that project or you can set it to */* meaning all your repositories can access them. 
    - Ensure you have requirements.txt file and Procfile. These are required by Heroku so ensure these are pushed to github prior to deployment. Ensure all requirements are saved by using pip3 freeze > requirements.txt
    - If using in development you will need to Run migrations usimg command python3 manage.py makemigrations and then python3 manage.py migrate. To create a superuser in the terminal to get access to admin panel, use command python3 manage.py createsuperuser and fill in details required.

- ### Heroku deployment
    - Log in to Heroku, click 'New' and select 'Create New App'. In window give the app a name and choose region closest to you and then click 'Create App'. Then in Resources under Add-ons, select Heroku Postgresql
    - In new app page select settings from menu, click reveal config vars. DATABASE_URL will have been pre-filled when you selected Postgres. SECRET_KEY was generated as before with Django Secret Key generator.
    - Next select 'Deploy' from menu, three options of deployment are available. If you select Heroku CLI, it gives you step by step of what you need to do.
    - You will now need to migrate and create superuser as above in Setting Up Project section.

## Credits

Advice summaries
- Improving self esteem: (https://www.positivityblog.com/)
- Sense of belonging: (https://www.psychologytoday.com/
- Improving sense of purpose: (https://www.improveon.co.uk/www/5-steps-to-a-renewed-sense-of-purpose/)
- Improving your outlook on life: (https://youcanpym.com/blogs/learn/how-to-have-a-positive-outlook-on-life
- Improving your sense of autonomy: (https://www.kellylynnssweetsandtreats.com/how-to-improve-your-sense-of-autonomy/)  

### Code
-   Natalie used her MS4 as a guide throughout Blog app development as a starting point for each file and README template.
-   Django documents
-   Boostrap documents

### Content

-   Content was created by all team members working together, sharing tasks on the github project board.

### Media
-   Photo by MART PRODUCTION: (https://www.pexels.com/photo/a-young-woman-video-calling-with-a-laptop-on-a-couch-7606078/) 
-   Photo by William Fortunato: (https://www.pexels.com/photo/smiling-young-ethnic-woman-working-distantly-on-laptop-and-talking-on-smartphone-6393342/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)
-   Photo by Andrea Piacquadioa: https://www.pexels.com/photo/cheerful-senior-mother-and-adult-daughter-using-smartphone-together-3791664/

### Acknowledgements
Thanks to CI and Trust in Soda for organising the hackathon.
Thanks to all team members for their valued contributions and hard work coding!

-   
