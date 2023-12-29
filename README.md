# KidLit Swap

![Home Page](documentation/home-page.png)

KidLit Swap, derived from Kids' Literature Swap, is a vibrant online community where parents unite to share and exchange children's books. Originating from conversations among parents at my kids' school, it serves as a virtual clubhouse celebrating the enchantment of storytelling in the digital era.

KidLit Swap's purpose is clear – to encourage the sharing and borrowing of kids' literature, fostering a love for reading in young minds. You can share your favorite stories, borrow books from others, and be part of our growing library. It's a fun way to help your kids become great readers.

Join KidLit Swap and let's make reading magical for our little ones!

[KidLit Swap Live Page](https://kidlit-swap-96ca222a1195.herokuapp.com/)


## CONTENTS

- [KidLit Swap](#kidlit-swap)
  - [CONTENTS](#contents)
  - [Project Goals](#project-goals)
  - [User Experience (UX)](#user-experience-ux)
    - [Target Audience](#target-audience)
    - [User Requeriments and Expectations](#user-requeriments-and-expectations)
    - [User Stories](#user-stories)
      - [First Time Visitor Goals](#first-time-visitor-goals)
      - [Returning Visitor Goals](#returning-visitor-goals)
      - [Frequent Visitor Goals](#frequent-visitor-goals)
  - [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Imagery](#imagery)
    - [Fonts](#fonts)
    - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
  - [Data Model](#data-model)
  - [Security Features and Defensive Design](#security-features-and-defensive-design)
    - [User Authentication](#user-authentication)
    - [Form Validation](#form-validation)
    - [Database Security](#database-security)
    - [Custom error pages:](#custom-error-pages)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Favicon](#favicon)
      - [Header](#header)
      - [Footer](#footer)
    - [Home Page](#home-page)
    - [User Account Pages](#user-account-pages)
    - [Error Pages](#error-pages)
    - [Future Implementations](#future-implementations)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Testing](#testing)
    - [Bugs](#bugs)
  - [Deployment](#deployment)
    - [Code Institute Python Essentials Template](#code-institute-python-essentials-template)
    - [Deployment process](#deployment-process)
    - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
  - [Acknowledgments](#acknowledgments)

---

## Project Goals

The KidLit Swap project was developed with the following goals in mind:



[Back to Contents](#contents)

## User Experience (UX)

### Target Audience

KidLit Swap is designed to cater to the following target audience:


### User Requeriments and Expectations

- User Requirements: 

- User Expectations: 

### User Stories

#### First Time Visitor Goals

-

#### Returning Visitor Goals



#### Frequent Visitor Goals


Include EPIC and user stories
Include User stories not yet implemented
Include Benefits of key features and the EPIC Milestone Approach

---

## Design

Intro

### Color Scheme

Include Color palette from Coolors

### Imagery

### Fonts

### Wireframes

<details>

 <summary>Home Page</summary>

![Home Page]()
</details>

[Back to Contents](#contents)

---

## Agile Methodology

Github projects was used to manage the development process using an agile approach. Please see link to project board [here]()

The  Epics listed above were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone(Epic). Each User Story has defined acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks to facilitate the User Story's execution.

[Back to Contents](#contents)

---

## Data Model

I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.  

Django AllAuth was used for the user authentication system.




The diagram below details the database schema.

![Database Schema]()


[Back to Contents](#contents)

---

## Security Features and Defensive Design

### User Authentication



### Form Validation

### Database Security


### Custom error pages:

Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

- 400 Bad Request - The KidLit Swap is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - The KidLit Swap is currently unable to handle this request

[Back to Contents](#contents)

---

## Features

### Existing Features

#### Favicon

The website features a favicon that is visible in the browser tab.

![favicon](documentation/favicon-image.png)

#### Header

**Logo**

**Navigation Bar**

#### Footer

### Home Page

### User Account Pages

**Sign Up**

**Log In**

**Log Out**

### Error Pages

Custom Error Pages were created to give the user more information on the error and to guide them back to the site.

![header]()

- 400 Bad Request - The Easy Eater is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - The Easy Eater is currently unable to handle this request

### Future Implementations

The following user stories were scoped out of the project due to time constraints and labelled as "Could Have" on the project board in Github. It is intended that these user stories will be implemented at a later date. 


[Back to Contents](#contents)

---

## Technologies Used

### Languages Used

- Python
- HTML
- CSS
- Javascript

### Frameworks, Libraries & Programs Used

- [VS Code](https://code.visualstudio.com/) - IDE used to create the KidLit Swap.

- [Github](https://github.com/) - Used for file storage, version control, and hosting page assets.

- [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) - Served as the foundational structure for this project.

- [Code Institute Python Linter](https://pep8ci.herokuapp.com/) - Verify code conformity with PEP8.

- [Pylance Validator](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
  
- [Heroku](https://www.heroku.com/) - Used to deploy the project.

- [TinyPNG](https://tinypng.com/) - To compress images

- [CloudConvert](https://cloudconvert.com/) - To transform a video into a GIF for inclusion in the Readme.md file.

- [Favicon.io](https://favicon.io/) - To create favicon.

- [Chat-GPT](https://chat.openai.com/) - Enhance Readme.md readability; streamline content for effective communication.


- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud based platform to deploy the site on.
- [Responsinator](http://www.responsinator.com/) - Used to verify responsiveness of website on different devices.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - Used for icons in information bar.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [PEP8 Online](http://pep8online.com/) - used to validate all the Python code
- [Jshint](https://jshint.com/) - used to validate javascript
- [Coolors](https://coolors.co/) - Used to create colour palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Grammerly](https://app.grammarly.com/) - used to proof read the README.md
- [Summernote](https://summernote.org/): A WYSIWYG editor to allow users to edit their posts
- [Techsini](https://techsini.com/multi-mockup/index.php) - Site mockup generator
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling
- [Hatchful](https://hatchful.shopify.com/): Used to generate custom logo
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert excel testing tables to markdown


[Back to Contents](#contents)

---

## Testing

Please refer to [TESTING.md](TESTING.md) file for a comprehensive overview of all conducted testing procedures.

### Bugs

| **BUG** | **DESCRIBE THE BUG**  | **HOW I SOLVED**|
| ------- | ------- | ------- |


[Back to Contents](#contents)

---

## Deployment 

The website has been successfully deployed on Heroku. You can access the live site [here](https://kidlit-swap-96ca222a1195.herokuapp.com/).

### Code Institute Python Essentials Template 

To create a terminal-based user interface using the Code Institute Python Essentials Template and display Python code output:

1. Go to the [Code Institute Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) and click on "Use this template."
2. Choose "Create a new repository."

### Deployment process

Vide Txt


### Local Development

#### How to Fork

To fork the repository:

1. Login (or signup) to GitHub account.
2. Go to the repository for this project, [IzabellaLopes/kidlit-swap](https://github.com/IzabellaLopes/kidlit-swap).
3. Click the Fork button in the top right corner.
4. Edit the repository name and description if desired
4. Click the green create fork button

#### How to Clone

To clone the repository:

1. Login (or signup) to GitHub account.
2. Go to the repository for this project, [IzabellaLopes/kidlit-swap](https://github.com/IzabellaLopes/kidlit-swap).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.


[Back to Contents](#contents)

---

## Credits

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Update View](https://pytutorial.com/django-updateview-example)
- [Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/#using-paginator-in-a-view)
- [AutoSlugField](https://django-extensions.readthedocs.io/en/latest/field_extensions.html)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog)

### Code


### Content

- Content for the website was written by Izabella Lopes.


## Acknowledgments

I would like to express my gratitude to the following individuals who played significant roles in the successful completion of my fourth project:

- I am grateful to my family for their consistent support and understanding throughout this period of intense studying.
- I want to express my sincere thanks to my fellow peers from the April 2023 cohort at Code Institute. Their invaluable contributions in bug testing are deeply appreciated.
- Jubril Akolade, my mentor from the Code Institute.