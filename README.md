[![Build Status](https://travis-ci.org/EricGaona/dolcetto.svg?branch=master)](https://travis-ci.org/EricGaona/dolcetto)

# Dolcetto

This is the e-commerce website for the final project of the course Full Stack Web Development in Code Institute. The features of the web application are:

Show users a variety of pastry products especially cakes as well as a section of vegan products, in a way that allows them to select the products they want
and buy them with a delivery service.
The website also gives users the opportunity to create a profile where the user's data will be saved along with the history of the purchases made by
themselves on the website in order to re- order their favourite treats easier and quicker.  
It must also be highlighted that the web application gives super users (authorised users) access to the database allowing them to create, modify and
delete products.

The main goal of this website is to best display all products the company sells and to make the UX and sales process of those products as seamless as
possible in order to drive online sales and grow the business.

## UX

My intention has been to create an easy to use and intuitive site that would allow the user to navigate informally through the different sections.
To draw the attention of users, I have placed an image of a succulent cheesecake that looks very appetizing.

As the site sells dairy and vegan products, both have been separated into two sections although there is an option to browse all the products together
if the client wishes. When you enter the website, you will visually find different sections placed on the home page and also a "Shop now" tab on the
body where all products are shown together.

### User Stories

1. As a user, I would like to buy a birthday cake for my son who is a fanatic of football.
2. I really like patry when I organise meetings with my friends every weekend and it is very handy to have the possibility to choose among this variety
   and they offer you a delivery service.
3. I have a vegan friend and sometimes he cannot eat most of the food in my birthday parties, not all of us are vegan and I would like to have some vegan
   products on my table and also a cake. Then, we can try this products that might like them.
4. We are a couple who are planning our wedding and we would like to order a wedding cake for next month and they can deliver it in the restaurant the same day.

## Features

- This website lets users buy the products on the website without the need for creating a user profile.
- Once a user create an account, they can keep their purchases and their personal details.
- All the products are organised by different sections (Price, Ranking and Categories).
- There is a searcher on the top of the page where you can type the name of the product or the characteristics of the product that you are looking for.
- Also, here, you will find the option to search the different products and keep them in the cart and return to the list of products to add more to
  your shopping list.

### Features Left to Implement

- When users log in their profile, it would have been ideal to include the picture of the products that the client has bought and not only a title.
  Then, customers have a better visualization of our products.
- It would be a great idea to add a contact form in order to have a personal and more direct contact with our customers in case they have any inquiry
  in relation to any product.

## Technologies Used

- [HTML5](https://www.w3schools.com/html/)
  - The project uses HTML5 to build and style.
- [CSS3](https://developer.mozilla.org/es/docs/Archive/CSS3)
  - The project uses CSS3 to further style and hide/show content for game flow
- [Google fonts](https://fonts.google.com/)
  - The project uses Google fonts for fonts
- [FontAwesome](https://fontawesome.com/)
  - The project uses font awesome icons
- [Bootstrap](https://getbootstrap.com/)
  - The project uses Bootstrap, helpers and the grid system
- [Javascript](https://www.w3schools.com/js/)
  - The project uses Javascript for an interactive user experience and to control stripe
- [Python](https://www.python.org/)
  - The project uses Python to handle and run django
- [Django](https://www.djangoproject.com/)
  - The project uses the Django wireframe to speed up production and handle a lot of the python back end requests
- [Stripe](https://stripe.com/es-ie)
  - The project uses stripe to handle payments
- [Heroku](https://www.heroku.com/)
  - The project uses Heroku for Postgres database and hosting
- [Amazon Web Services](https://aws.amazon.com/es/)
  - The project uses AWS for hosting of static files and the images
- [Github](https://github.com/)
  - The project uses Github to host the repository
- [Gitpod](https://www.gitpod.io/)
  - The project uses Gitpod as IDE

## Testing

Testing is done using Travis.

### HTML & CSS

All my HTML and CSS are valid and checked with the following validators:

- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)

#### Review all functionality and responsiveness:

This website was tested across multiple browsers including Chrome, Opera, Internet Explorer, Firefox and on multiple movie devices including
iPhone 4, 5, and 7. Also on Samsung and Xaomi to ensure compatibility and responsiveness.

## Deployment

- First, I created a repository in Github using the template provided by Code Institute.
- This project has been developed using Gitpod and the following commands: git add, git commit -m and git push (To Github).
- Use the command “pip3 freeze > requirements.txt”
- Create the Procfile
- I created an app on Heroku website and I connected with the repository previously created by Github. Therefore, all the folders in Github were copied in Heroku
  as well I activated Enable Automatic Deploys, so that every time you make a push in to Github it will automatically be changed into heroku too.
- In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables as follows:

  - AWS_ACCESS_KEY_ID <your secret key>
  - AWS_SECRET_ACCESS_KEY <your secret key>
  - DATABASE_URL <your postgres database url>
  - EMAIL_HOST_PASS <your secret key>
  - EMAIL_HOST_USER <your email address>
  - SECRET_KEY <your secret key>
  - STRIPE_PUBLIC_KEY <your Stripe Public key>
  - STRIPE_SECRET_KEY <your Stripe Secret key>
  - STRIPE_WH_SECRET <your Stripe Webhooks key>
  - USE_AWS <True>

- I build a bucket in Amazon web service where all the pictures and the static file were hosted.
- In the Dolcetto settings.py file:

  - The if/else statement that handles the database location.
  - The DEBUG, ALLOWED_HOSTS were set up too.

- Click these links to access the project in Github or Heroku:

  - [Dolcetto Heroku](https://dolcetto.herokuapp.com/)
  - [Dolcetto Github](https://github.com/EricGaona/dolcetto)

## Credits

### Content

All the content has been created either by me and my friend Tony Pérez who is a pastry chef in Bilbao, Spain.

### Media

The photos used in this site were obtained from [pixabay](https://pixabay.com/es/), [bbcgoodfoog](https://www.bbcgoodfood.com/).

### Acknowledgements

Last but no least, I deeply grateful to my mentor Brian Macharia who helped me so much in getting through this project. Also a massive thank you to all the
Code Institute's student support team who helped me so many times, especially to Michael and Xavier for their recommendations of this project.
Also, I would like to express my gratitude to my friend Tony Pérez who inspired me to design this website.
