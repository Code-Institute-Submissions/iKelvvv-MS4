# Restaurant Booking System

## Introduction
Welcome to my fourth project. This project is a simple restaurant booking system, allow users to book a table for this restaurant. This will use languages such as Django, Python, HTML, CSS and JavaScript.

A live website can be found [here]().

![website preview](documentation_assets/images/website_preview.png)

# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User Expectations:](#user-expectations)
            -   [Trends of Modern Websites](#trends-of-modern-websites)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Structure](#structure)
    -   [1.3. Skeleton](#skeleton)
    -   [1.4. Surface](#surface)
-   [2. Features](#features)
-   [3. Technologies Used](#technologies-used)
-   [4. Testing](#testing)
-   [5. Development Cycle](#development-cycle)
-   [6. Deployment](#deployment)
-   [7. End Product](#end-product)
-   [8. Known Bugs](#known-bugs)
-   [9. Credits](#credits)

<a name="ux"></a>

# 1. UX

[Go to the top](#table-of-contents)

As a big foodie, I have always enjoyed going out to different restaurants to try new cuisines. The simplest way is to book a table at a restaurant. The booking system is best when it's simple to use and asks for the necessary information.

This project will showcase simplicity and ease to booking a table, update a booking, cancel a booking, create a personal profile and update a profile.

<a name="strategy"></a>

## 1.1. Strategy

[Go to the top](#table-of-contents)

### Project Goals
The main goal of this project is to allow the user to sign up, sign in/out, create/update a user profile and create/update/delete a table booking in a simple and effective process.

### User Goals:
First Time Visitor Goals
-   As a first-time visitor, I want to book a table at my chosen date and time.
-   As a first-time visitor, I want to view the menu for the restaurant, so that I can decide to book a table or not.
-   As a first-time visitor, I want to be able to get the contact details of the restaurant with ease.

Returning Visitor Goals
-   As a Returning Visitor, I want to update my booking details.
-   As a Returning Visitor, I want to cancel a booking I have already made.
-   As a Returning Visitor, I want to edit my profile for any future bookings.

Frequent User Goals
-   As a Frequent User, I want to check to see if there are any new food items on the menu.

### User Expectations:
The system should have a simple user interface, with the navigation to each section clear and concise.

-   The menu is clear to read.
-   The user interface is easy to navigate.
-   The website is responsive on all devices.
-   To have the ability to contact the restaurant for any enquiries.

### Strategy Table
Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Display a food Menu | 5 | 5
Account signup | 5 | 5
User profile | 5 | 5
Responsive design | 5 | 5
Contact form | 4 | 5
Ability to create a booking | 5 | 4
Ability to update a booking | 5 | 4
Ability to cancel a booking | 3 | 4
Multiple table occupancies | 4 | 1
Avoid double bookings | 4 | 1

Total | 45 | 39

## Scope
As I am unable to include all of the features from the strategy table. I will phase this project in multiple phases. Phase 1 will be what I have identified as a minimum viable product. Please find below the plans I have for each phase.

### Phase 1
- Display a food menu
- Allow users to register for an account
- Allow users to create and edit a personal profile
- Responsive design
- Contact form
- Ability to create a booking
- Ability to update a booking
- Ability to cancel a booking

### Phase 2
- Multiple table occupancies
- Avoid double bookings

<a name="structure"></a>

## 1.2. Structure

[Go to the top](#table-of-contents)

It is really important to include responsive design in this project as many users are using different devices (mobile, tablet, laptop/PC). This gives the user the best experience on their device.

- Responsive on all device sizes
- Easy navigation through labelled buttons
- Footer at the bottom of the index page that links to the social media website.
- All elements will be consistent including font size, font family, colour scheme.

### Database Model
![database_model](documentation_assets/images/database_model.png)

<a name="skeleton"></a>

## 1.3. Skeleton

[Go to the top](#table-of-contents)

### Wire-frames
Home/Landing Page Desktop:
![home_page_desktop](documentation_assets/wireframes/home_desktop.png)

Home/Landing Page Mobile:
![home_page_mobile](documentation_assets/wireframes/home_mobile.png)

Navigation Bar Mobile:
![navigation_bar_mobile](documentation_assets/wireframes/navbar_mobile.png)

Menu Page Desktop:
![menu_page_desktop](documentation_assets/wireframes/menu_desktop.png)

Menu Page Mobile:
![menu_page_mobile](documentation_assets/wireframes/menu_mobile.png)

Register Page Desktop:
![register_page_desktop](documentation_assets/wireframes/register_desktop.png)

Register Page Mobile:
![register_page_mobile](documentation_assets/wireframes/register_mobile.png)

Login Page Desktop:
![login_page_desktop](documentation_assets/wireframes/login_desktop.png)

Login Page Mobile:
![login_page_mobile](documentation_assets/wireframes/login_mobile.png)

User Logged In Desktop:
![user_logged_in_desktop](documentation_assets/wireframes/user_logged_in_desktop.png)

User Logged In Mobile:
![user_logged_in_mobile](documentation_assets/wireframes/user_logged_in_mobile.png)

Online Booking Page Desktop:
![online_booking_page_desktop](documentation_assets/wireframes/online_booking_desktop.png)

Online Booking Page Mobile:
![online_booking_page_mobile](documentation_assets/wireframes/online_booking_mobile.png)

Contact Page Desktop:
![contact_page_desktop](documentation_assets/wireframes/contact_desktop.png)

Contact Page Mobile 1:
![contact_page_mobile](documentation_assets/wireframes/contact_mobile_1.png)

Contact Page Mobile 2:
![contact_page_mobile](documentation_assets/wireframes/contact_mobile_2.png)

Edit Profile Page Desktop:
![edit_profile_page_desktop](documentation_assets/wireframes/edit_profile_desktop.png)

Edit Profile Page Mobile:
![edit_profile_page_mobile](documentation_assets/wireframes/edit_profile_mobile.png)

Manage Booking Page Desktop:
![manage_booking_page_desktop](documentation_assets/wireframes/manage_booking_desktop.png)

Manage Booking Page Mobile:
![manage_booking_page_mobile](documentation_assets/wireframes/manage_booking_mobile.png)

<a name="surface"></a>

## 1.4. Surface

[Go to the top](#table-of-contents)

### Colours

Please find the colours schemes that I used [here](https://coolors.co/bd3c31-000000-ffffff-212529).

### Typography

I decided to use Be Vietnam Pro as my font of choice with sans serif as my backup font for browsers that might not support Be Vietnam Pro.

The link to the font can be found [here](https://fonts.google.com/share?selection.family=Be%20Vietnam%20Pro).

<a name="features"></a>

# 2. Features

[Go to the top](#table-of-contents)

### All Pages
- The navigation bar is placed at the top of all pages. The navigation bar is dynamic in that meaning depending on if the user is logged in or not the options will change.
- If the user is not logged in the navigation bar will look like this:
![user_not_logged_in](documentation_assets/images/navbar_not_logged_in.png)
- If the user is logged in the navigation bar will look like this:
![user_logged_in](documentation_assets/images/navbar_logged_in.png)
- The footer is placed at the bottom of each page with social media icons. When hovering over them it creates a zoom effect giving the user more of an experience. These icons will open the links in a new tab.

- The restaurant logo is also placed at the top of all pages. Clicking on it will also direct the user to the home page.
- Animated background, to give more of a user experience instead of a plain static background.

### Register Page
- A simple signup form that requires the user to enter a unique email address and a password. The password must be entered again for confirmation, this must match the already entered password above.
- A message to prompt the user that if an account is already been created they can click the sign-in hyperlink to be redirected to the sign-in page.
- If the user enters an email address that has already been registered, the user is prompted by an error message.
![email_validation_error](documentation_assets/images/signup_email_validation.png)
- If the user enters a password that is not secure, the user will be prompted by a message.
![password_too_common](documentation_assets/images/password_too_common.png)
- If the user enters both passwords that do not match, the user is prompted by a message.
![signup_email_validation](documentation_assets/images/signup_email_validation.png)
- Once the user has successfully signed up, this will automatically log in and direct the user to the create profile page.

### Login Page
- A login form that requires the user to enter their email address and password that they used when signing up to the site.
- A message to prompt the user that if an account has not been created they can click the signup hyperlink to be redirected to the signup page.
- If the user enters in the wrong credentials, a message is displayed to the user.
![signup_email_validation](documentation_assets/images/login_validation.png)

### Logout Page
- When clicking logout from the navigation bar, the user is redirected to a sign-out page to confirm their action.

### Landing Page
- A simple but elegant banner to give the user a sense of the restaurant.
- A book now button that directs the user to create a booking page. If the user has not logged in it will prompt the user to register or log in first.
- A short introduction to describe the restaurant.

### Create Profile Page
- Once the user has registered they will be redirected to the create profile page. The page displays a form for the user to enter their first name, last name and telephone number.

### Edit Profile Page
- The user can navigate to this page by clicking on the edit profile link in the navigation bar. This page will display the current profile details with a form below for the user to update any details.

### Menu Page
- The restaurant opening times are displayed at the top of the page.
- A menu that is displayed in 3 sections by the food category.

### Contact Page
- An information section that displays the restaurant telephone number, email address, opening times and address.
- A contact form that requires the user to enter their full name, email address and a message. The form is already pre-filled with the user's full name (if the user is logged in and has created a profile).
- A Google maps iframe of the restaurant location.

### Create Booking Page
- A form that requires the user to enter/select the booking details.
Full name and contact telephone number are prefilled if the user has created a profile.
The user will then need to select a date, time, number of guests and enter any allergy information if needed.
- The date input field has JavaScript code so the default value is today's date and the user cannot select a date that is previous to today.
- When clicking the make reservation button the booking will then be requested to the restaurant owner for approval.
- As the restaurant is only open from 2 PM, if the user selects a time before that, the form will display an error, prompting the customer to select a later time.
![booking_time_error](documentation_assets/images/booking_time_error.png)

### Manage Booking Page
- Displays all user-related bookings in a list view within a card.
- Each card will show a booking reference, booking status, booking date, booking time, guest count. It will also contain a button to change booking details and a cancel booking button.

### Edit Booking Page
- This page will display the current booking details with a form below for the user to update any details.
- When the changes are submitted, the booking will be processed as the booking requested status.

### Cancel Booking
- When the user clicks the cancel booking button they will be redirected to a confirmation page.

<a name="technologies-used"></a>

## 3. Technologies Used

[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project uses HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project uses Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project uses JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project uses Python.
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -   The project uses Bootstrap 5.
-   [Gitpod](https://www.gitpod.io/)
    -   The project uses Gitpod.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project uses Chrome to debug and test the source code using HTML5.
-   [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.
-   [Google Fonts](https://fonts.google.com/)
    -   Google fonts were used to import the "Be Vietnam Pro" font into the style.css file which is used on all pages throughout the project.
-   [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.

<a name="testing"></a>

# 4. Testing

[Go to the top](#table-of-contents)

### Google Developer Tools
For every element that I added to my HTML, I would add the basic CSS to my stylesheet. I would then use the inspect element to try different styles. Once I've got it to my liking I would try to see if I can implement the styling with bootstrap, if I could not replicate the styling I would copy the CSS from google and paste it into my CSS stylesheet. This allows me to keep track of the code I am using.

I also checked the accessibility of the page using lighthouse.
![google_lighthouse](documentation_assets/images/google_lighthouse.png)

### Responsive Tools
I used [Am I Responsive](http://ami.responsivedesign.is) to make sure that all my pages are responsive to all devices.

### W3C Validator Tools
#### HTML:
I used [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) to check for any errors within the HTML pages.

I had an error on the base.html template:
![base.html_error](documentation_assets/images/base.html_error.png)

This was then rectified by adding the lang attribute to the current HTML tag and deleting the other one.
![base.html_fix](documentation_assets/images/base.html_fix.png)

I had an error on the contact.html template:
![contact.html_error](documentation_assets/images/contact.html_error.png)

This was then rectified by removing the width styling of 100% and replacing it with a class="w-100".
![contact.html_fix](documentation_assets/images/contact.html_fix.png)

#### CSS:
I used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to check for any errors within my CSS stylesheet.

I had no errors in my CSS file:
![css_validation](documentation_assets/images/css_validation.png)

### JavaScript:
I used [JS Hint](https://jshint.com/) to check for any errors within my JavaScript file.

I had no errors in my JavaScript files:
![javascript_validation](documentation_assets/images/javascript_validation.png)

### Python:

## Manual Testing
I have tested my site on Safari and google chrome on multiple devices.

These include:
-   iPhone X
-   iPhone XS Max
-   iPad Pro
-   MacBook Pro

Please find below my testing process for all pages via mobile and web:

### Navigation Bar

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home page | When clicking the "home" button in the navigation bar, the browser redirects me to the home page. The is active styling will appear as the home button has a red background. | PASS
Menu page | When clicking the "menu" button in the navigation bar, the browser redirects me to the menu page. The is active styling will appear as the menu button has a red background. | PASS
Contact page | When clicking the "contact" button in the navigation bar, the browser redirects me to the contact page. The is active styling will appear as the contact button has a red background. | PASS
Book now page | When clicking the "book now" button in the navigation bar, the browser redirects me to the book now page. The is active styling will appear as the book now button has a red background.| PASS
Manage booking page | When clicking the "manage bookings" button in the navigation bar, the browser redirects me to the manage booking page. The user will know they are on this page by the heading. | PASS
Edit profile page | Checked foreground information is not distracted by backgrounds| PASS
Register page | When clicking the "register" button in the navigation bar, the browser redirects me to the register page. The user will know they are on this page by the heading. | PASS
Login / Logout page | When clicking the "login" or "logout button in the navigation bar, the browser redirects me to the login or logout page. The user will know they are on this page by the heading. | PASS
Foreground & background colour | Checked foreground information is not distracted by background animation. | PASS
Text | Checked that all fonts and colours used are consistent. | PASS

### Footer
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Facebook | When clicking the Facebook icon, a new tab opens and redirects to the Facebook website. | PASS
Twitter | When clicking the Twitter icon, a new tab opens and redirects to the Twitter website. | PASS
Instagram | When clicking the Instagram icon, a new tab opens and redirects to the Instagram website. | PASS

### Home page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS

![index_google_lighthouse](documentation_assets/images/index_google_lighthouse.png)

### Menu page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS

![menu_google_lighthouse](documentation_assets/images/menu_google_lighthouse.png)

### Contact page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Contact Form | Checked the form submits only when all fields are filled out. | Pass

![contact_google_lighthouse](documentation_assets/images/contact_google_lighthouse.png)

### Booking page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Booking Form | Checked the form submits only when all required fields are filled out. | Pass
If not signed in | Checked to see if the user has not signed in the booking form should not show and a message displays prompting the user to signup/sign-in first. | Pass

![booking_google_lighthouse](documentation_assets/images/booking_google_lighthouse.png)

### Edit booking page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit Booking Form | Checked the form submits only when all required fields are filled out. | Pass

![edit_booking_google_lighthouse](documentation_assets/images/edit_booking_google_lighthouse.png)

### Manage booking page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit booking button | Checked that the button redirects to the edit booking page with the correct booking instance. | Pass
Cancel booking button | Checked that the button redirects to the cancel booking page with the correct booking instance. | Pass

![manage_booking_google_lighthouse](documentation_assets/images/manage_booking_google_lighthouse.png)

### Edit profile page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit profile form | Checked the form submits only when all required fields are filled out. | Pass
If the profile has not been created | Checked to see if the user has created a profile, if not it will redirect the user to the create profile page | Pass

![edit_profile_google_lighthouse](documentation_assets/images/edit_profile_google_lighthouse.png)

### Register page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Register form | Checked the form submits only when all required fields are filled out. | Pass
Sign in link | Checked the sign-in link redirects to the sign-in page. | Pass

![signup_google_lighthouse](documentation_assets/images/sign_up_google_lighthouse.png)

### Sign in page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Sign in form | Checked the form submits only when all required fields are filled out. | Pass
Signup link | Checked the signup link redirects to the signup page. | Pass

![sign_in_google_lighthouse](documentation_assets/images/sign_in_google_lighthouse.png)

<a name="development-cycle"></a>

# 5. Development Cycle

[Go to the top](#table-of-contents)

## Project Checklist
- Install Django and the supporting libraries
    -  Install Django and Gunicorn. Gunicorn is the server I am using to run Django on Heroku.
    - Install support libraries including psycopg2, this is used to connect the PostgreSQL database
    - Install Cloudinary libraries, this is a host provider service that stores images
    - Create the requirements.txt file. This includes the project's dependencies allowing us to run the project in Heroku.

- Create a new, blank Django Project
    - Create a new project
    - Create the app
    - Add restaurant_booking to the installed apps in settings.py
    - Migrate all new changes to the database
    - Run the server to test

- Setup project to use Cloudinary and PostgreSQL
    - Create new Heroku app
        - Sign into Heroku
        - Select New
        - Select create new app
        - Enter a relevant app name
        - Select appropriate region
        - Select the create app button

    - Attach PostgreSQL database
        - In Heroku go to resources
        - Search for Postgres in the add-ons box
        - Select Heroku Postgres
        - Submit order form

    - Prepare the environment and settings.py file
        - Create env.py file
        - Add DATABASE_URL with the Postgres URL from Heroku
        - Add SECRET_KEY with a randomly generated key
        - Add SECRET_KEY and generated key to the config vars in Heroku
        - Add if statement to settings.py to prevent the production server from erroring
        - Replace insecure key with the environment variable for the SECRET_KEY
        - Add Heroku database as the back end
        - Migrate changes to new database

    - Get static media files stored on Cloudinary
        - Create a Cloudinary account
        - From the dashboard, copy the API Environment variable
        - In the settings.py file create a new environment variable for CLOUDINARY_URL
        - Add the CLOUDINARY_URL variable to Heroku
        - Add a temporary config var for DISABLE_COLLECTSTATIC
        - In settings.py add Cloudinary as an installed app
        - Add static and media file variables
        - Add templates directory
        - Change DIR's key to point to TEMPALTES_DIR
        - Add Heroku hostname to allowed hosts
        - Create directories for media, static and templates in the project workspace
        - Create a Procfile

- Deploy new empty project to Heroku
![initial_heroku_deployment](documentation_assets/images/initial_deployment_successful.png)

<a name="deployment"></a>

# 6. Deployment

[Go to the top](#table-of-contents)


<a name="end-product"></a>

# 7. End Product

[Go to the top](#table-of-contents)

Home Page:
![home_page_desktop_preview](documentation_assets/images/homepage_desktop_preview.png)

![home_page_mobile_preview](documentation_assets/images/homepage_mobile_preview.png)

Menu Page:
![menu_desktop_preview](documentation_assets/images/menu_desktop_preview.png)

![menu_mobile_preview](documentation_assets/images/menu_mobile_preview.png)

Contact Page:
![contact_desktop_preview](documentation_assets/images/contact_deskop_preview.png)

![contact_mobile_preview](documentation_assets/images/contact_mobile_preview.png)

Book Now Page:
![booking_desktop_preview](documentation_assets/images/booking_desktop_preview.png)

![booking_mobile_preview](documentation_assets/images/booking_mobile_preview.png)

Manage Booking Page:
![manage_booking_desktop_preview](documentation_assets/images/manage_booking_desktop_preview.png)

![manage_booking_mobile_preview](documentation_assets/images/manage_booking_mobile_preview.png)

Edit Booking Page:
![edit_booking_desktop_preview](documentation_assets/images/edit_booking_desktop_preview.png)

![edit_booking_mobile_preview](documentation_assets/images/edit_booking_mobile_preview.png)

Edit Profile Page:
![edit_profile_desktop_preview](documentation_assets/images/edit_profile_desktop_preview.png)

![edit_profile_mobile_preview](documentation_assets/images/edit_profile_mobile_preview.png)

Register Page:
![register_desktop_preview](documentation_assets/images/register_desktop_preview.png)

![register_mobile_preview](documentation_assets/images/register_mobile_preview.png)

Sign In Page:
![sign_in_desktop_preview](documentation_assets/images/sign_in_desktop_preview.png)

![sign_in_mobile_preview](documentation_assets/images/sign_in_mobile_preview.png)

Sign Out Page:
![sign_out_desktop_preview](documentation_assets/images/sign_out_desktop_preview.png)

![sign_out_mobile_preview](documentation_assets/images/sign_out_mobile_preview.png)


<a name="known-bugs"></a>

# 8. Known Bugs

[Go to the top](#table-of-contents)

- Some items in the navigation bar don't have a is active red background to show the user they are on the selected page.

<a name="credits"></a>

# 9. Credits

[Go to the top](#table-of-contents)

### Code
-   The navigation bar came from [Bootstrap](https://getbootstrap.com/docs/5.0/components/navbar).

- The JavaScript code to set the online booking form to default to the current date came from [Stack Overflow](https://stackoverflow.com/questions/6982692/how-to-set-input-type-dates-default-value-to-today).

- The JavaScript code to disable any previous dates on the online booking form came from [Demo2s](https://www.demo2s.com/javascript/javascript-input-date-input-type-date-disable-dates-before-today.html).

### Content
-   The restaurant logo came from [Adobe Creative Cloud Express logo maker](https://www.adobe.com/express/create/logo).

-   The dragon image from the home page came from [PNGItem](https://www.pngitem.com/middle/wRmbRx_red-dragon-png-red-chinese-dragon-png-transparent/).

-   The banner image from the home page came from [PNGItem](https://pngtree.com/freebackground/chinese-food-pasta-simple-white-banner_1059420.html).

-   The Chinese food image on the menu page came from [Google Images](tinyurl.com/68hzut9u).

-   The Chinese food image on the menu page came from [Google Maps](https://www.maps.ie/create-google-map/).