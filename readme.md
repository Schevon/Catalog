# **Item Catalog**

## **Project Description**
This web application  provides a list of Sporting Items within a variety of Sports as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## **Files**

<ul>
<li>app.py -- python script with flask main application</li>
<li>sportcatalog.db -- underlying sqlite database that supports the application</li>
<li>database_setup.py -- python script that uses SQLAlchemy ORM  to create the database schema</li>
<li>populate database.py -- python script to populate sportcatalog.db with sample data</li>
<li>client_secrets.json -- file that stores the app's client id, client_secret, and other OAuth 2.0 parameters provided by the Google API library</li>
<li>fb_secrets.json --file that stores the app's secret that generate login flows access tokens via the Facebook API library</li>
<li>static/styles.css -- css style for all views</li>
<li>templates/layout.html -- header included in all views</li>
<li>templates/main.html -- page with additional css and web page formatting views</li>
<li>templates/login.html --application login page</li>
<li>templates/deleteSportCategory.html -- template for deleting a sport category</li>
<li>templates/deleteSportItem.html -- template for deleting a sport  item</li>
<li>templates/editSportCategory.html -- template for editing a sport  category</li>
<li>templates/editSportItem.html -- template for editing a sport Item</li>
<li>templates/menuItem.html -- template for viewing sport item</li>
<li>templates/newmenuItem.html -- template for creating sport item </li>
<li>templates/publicsportscategory.html -- template for viewing  sport category </li>
<li>templates/newsportscategory.html -- template for creating sport category </li>
<li>templates/publicmenuitem.html -- template for a public view of  sport items </li>
<li>templates/publicsportscategory.html -- template for a public view of  sport category </li>
</ul>

## **How to Run**


Assuming that a database has been created and the necessary installations are present (see dependencies below):

$ cd vagrant<br/>
$ vagrant up<br/>
$ vagrant ssh<br/>

$ cd /vagrant/catalog<br/>
$ python app.py<br/>

Then navigate to http://localhost:5000/

## **Dependencies**
<ul>
<li>Vagrant</li>
<li>Virtual Box</li>
<li>Python</li>
<li>SQLAlchemy</li>
<li>Flask</li>
<li>Google Login</li>
<li>Facebook Login</li>
</ul>
