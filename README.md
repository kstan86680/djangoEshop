# DjangoEshop
DjangoEshop is an E commerce platform from where people can purchase clothings.
<hr>

### User Experience 
This E commerce platform is for the people who want easy shopping through credit card. There is a list view of every product and detailed view as well so that one can choose a product by keeping various things in mind.

#### User story

 - As a customer I want to see a list of products so that I can choose
   from different of varieties.
 - As a customer I want to have online transaction available so that I
   can 	   purchase from home
 - As an admin I want to have a dashboard from where I can control
   everything    
 - As an admin I want to have my payments gathered in one    place.

#### Existing Features

-   Feature 1 - allows customers to login, by having them fill out login form
- Feature 2 - allows customers to register, by having them fill out signup form
- Feature 3 - allows customers to view list and details of products
- Feature 4 - allows customers add products to cart, remove products form cart
   

#### Features Left to Implement

-  Implement a machine learning model to recommend a product for a specific user
- Implement Access control for the entire platform

### Technology Used
 - Django : A python web framework
	 - Django provides easy implementation of MVC pattern. Which serves our purpose very well
 - Heroku : A platform to host web application 
	 - Heroku is a software as a service which made deployment very efficient and easy. It is also able to scale the web app
 -  Frontend : HTML, CSS, JavaScript, JQuery
	  - All of this mandatory frontend technologies are used for simplify browser dom manipulation.  And styling the whole project.

### Testing 
**stripe**  is tested using `4242 4242 4242 4242` and a US zip code `99501` as its verified by US

 - Testing stripe with mentioned card number leaves with a error for the zip code. Which fix was not easy to find. 

**Forms** are tested by manual inputs
**Product**  CRUD are tested manually form admin panel

### Deployment
Deployment is entirely done with heroku. Difference between development and Deployment version is mentioned below

Deployment
 - Have proc file 
 - DEBUG: False 
 - Database: SQLite3 
 - Static files served from local

Development
 - Dont Have proc file 
 - DEBUG: True 
 - Database: PostgreSQL 
 - Static files served from whitenoise (a python library) storage

### Credits

**Media**

-   The photos used in this site were obtained from google.com
    

**Acknowledgements**

-   I received inspiration for this project from my family