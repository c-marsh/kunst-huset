This project uses Django to build a site for artists to sell art. It works on premise of artists being able to list their works, but the site taking payment and handling distribution as a physical gallery might.
# Design
## User Stories
<details>
  <summary>Click to view user Stories!</summary>

|   Id          	|   As a/an    	|   I want to be able to:                           	|   So I can                                                           	|
|---------------	|--------------	|---------------------------------------------------	|----------------------------------------------------------------------	|
|   Admin       	|              	|                                                   	|                                                                      	|
| 1             	|   Artist     	|   add work                                        	|   Add info and image of work                                         	|
| 2             	|   Artist     	|   edit work                                       	|   Edit info and image of work                                        	|
| 3             	|   Artist     	|   Remove work                                     	|   Remove info and image of work                                      	|
| 4             	|   Artist     	|   sell work                                       	|   Add info and image of work                                         	|
| 5             	|   Artist     	|   create a profile                                	|   Add info/create a portal about myself                              	|
|   Browsing    	|              	|                                                   	|                                                                      	|
| 6             	|   Buyers     	|   Can browse/look for work                        	|    To see an array of available works                                	|
| 7             	|   Buyers     	|   Can view details                                	|   To see more info about the piece of work                           	|
| 8             	|   Buyers     	|   Can view info about artist                      	|   To find pieces of work                                             	|
| 9             	|   Buyers     	|   Can search/filter                               	|   To find work by criteria                                           	|
|   Accounts    	|              	|                                                   	|                                                                      	|
| 10            	|   Buyer      	|   Can make account                                	|    Create an account to access history of purchases/save information 	|
| 11            	|   Artist     	|   Can make account                                	|    To manage profile information and see a history of works sold     	|
| 12            	|   Buyer      	|   Can edit account                                	|    To update info                                                    	|
| 13            	|   Artist     	|   Can edit account                                	|    To update info                                                    	|
| 14            	|   Buyer      	|   Can delete account                              	|    To remove info                                                    	|
| 15            	|   Artist     	|   Can delete account                              	|    To remove info                                                    	|
|   Purchasing  	|              	|                                                   	|                                                                      	|
| 16            	|   Buyer      	|   Can complete a payment                          	|    securely complete a Strip transaction                             	|
| 17            	|   Buyer      	|   Can view purchase details/total before payment  	|    ensure purchase details are correct                               	|
| 18            	|   Buyer      	|   Can provide shipping details                    	|    input correct info                                                	|
| 19            	|   Buyer      	|   View a puchase history                          	|                                                                      	|
| 20            	|   Artist     	|   View a history of items sold                    	|                                                                      	|
</details>

## Design
The site is designed using a minimalist colour scheme. This is to allow the art to stand out from the site, while the site primarily uses smooth movements of menus and cards to complement the products on sale.

## Pages
The site is made up of the following pages:

### Home Page

### Gallery Page

<details>
  <summary> The gallery page features</summary> 

- a gallery view of cards of the art
    - filterable ascending or descending by
        - price, 
        - title, 
        - artist, 
        - category
    - Searchable by
        - description, 
        - title, 
        - artist, 
        - medium
    - The search and filter provides feedback about what search terms have been used, how many items are returned, and provides a reset button.
- The cards feature: 
    - a cropped window into the artwork
    - a badge displaying the price, or "Sold" if the piece has been sold 
- On hover the cards additionally show: 
    - the title 
    - artist of the piece.
- Clicking on the card takes one to the Detail page of the art.
- A back to top button is provided for easy navigation.


</details>


### Artwork Page

<details>
  <summary> The Artwork page features</summary> 

- an overview of the piece
    - A clickable thumbnail of the piece
        - This opens a full screen view in a new tab
    - title, 
    - artist,
    - year/date produced, 
    - description, 
    - medium, 
    - dimensions/weight/duration as relevant 
    - quantity available
 - if the piece is available to buy:
    - A field to add a quantity to cart, limited by the quantity available
    - A button back to the gallery
 - if the piece has been sold
     - A button back to the gallery

</details>

### Basket
<details>
  <summary> The basket page features</summary> 

If there is nothing in the basket, text indicates the basket is empty and a button is provided to take the viewer back to the gallery.
If the basket holds contents the display provides:
- A summary of
    - sub total
    - shipping
    - VAT/sales tax
    - Grand Total
- an overview of the pieces in the basket displayed as cards similar to those in the Gallery view so the view has a visual ideas of artworks in the basket, however with the following changes:
    - A remove button to remove from basket
    - quantity and total price shown on the card
    - title,
    - artist
    - medium 
    - the cards aren't clickable other than the remove button.
 - The page features buttons to checkout, or return to gallery.

</details>

### Checkout

<details>
  <summary> The Checkout page features</summary> 

- A summary of
    - sub total
    - shipping
    - VAT/sales tax
    - Grand Total
- an overview of the pieces in the basket displayed as cards exactly as shown in the basket view, however with remove button removed.
    - A 3 step slider for input of:
        - contact details on slide
        - shipping details on second page
            - with an option to store if logged in,
                - or otherwise providing a log-in or register link
        - payment details on the third page.
        - An order summary presented after checkout
        - Defensive design that ensures an order is created from return stripe webhook, in the case of a failure on the front end to create an order.

</details>

## Additional Features
### Administration
Custom styled login/out/account admin pages.

### Notifications
Notifications are provided by colour coded toasts to provide the user with feedback and assurance. These dismissable Toasts also feature a basket preview when items are added, and a button to take the browser to the basket.

### Menus
Two Menus are provided via means of hamburger icons at either end of the menu bar. These are:
<details>
  <summary> The Gallery Menu</summary> 

This provides navigation of the art related elements with filters for categories, direct links to artists profiles, home and the unfiltered gallery.

</details>

<details>
  <summary> The Account Menu</summary> 

This provides navigation of the account and purchasing related elements and displays:
 - for non-logged in users:
    - login/register options
    - basket total and link
 - for logged in users:
    - account management
    - logout option
    - basket total and link
 - for superusers:
    - Administration portal
    - account management
    - logout option
    - basket total and link

</details>

### Profile/Artist Page

# Bugs
## Major
 - ~~Poor Database structure - Artist DB may be obsolete~~
 - ~~Order history not saving to profiles~~
 - checkout does not update inventory of stock

## Minor
- Artists disappear from menu on some pages

### Cosmetic
- Artist fields for adding art displaying all users not just artists
- Buttons on some form pages too close to text
- Make right hand menu bass responsive to number of menu items.
- image upload fields need styling


# Future Developement
 - Show all art from an artist on their public profile
 - Sign-up including more profile data
 - Implement better use of the is_artist/is_customer fields to streamline menus.
 - Better gallery filtering including filtering out sold pieces.



# Deployment
This website was deployed on Heroku and can be found at https://kunst-huset.herokuapp.com/

## Heroku Deployment
First login and create your app on the Heroku site, and select a region. Then in the app settings, under ‘Config Vars’ you can should set the following Stripe keys which can be easily found on their dashboard after signing up.
- STRIPE_WH_SECRET as your WH key
- STRIPE_SECRET_KEY as the Stripe secret key 
- STRIPE_PUBLIC_KEY for the Stripe Public Key

Under the resources start a PostGres Database

Then create a ‘requirements’ file, which lists all the dependencies by typing in the following command in the bash terminal:

```
pip3 freeze > -v requirements.txt
```

Copy the postgres URL from Heroku config vars into the placeholder: ```dj_database_url.parse(os.environ.get(POSTGRES URL))```

Run migrations to the new database with ```python3 manage.py migrate```

Then use ```python3 manage.py loaddata categories```. Due to the artworks dependencies on user profiles, it can't be migrated across.

Finally create a superuser with ```python3 manage.py createsuperuser```.


You will then need to create a ‘Procfile’, which lists the process types in an application.:
```
Echo web: python run. py > Procfile
```

This should then be commited to your repository before Pushing to Heroku:
```
Git add . > git commit -m “Setup Heroku” > git push
```

This will update your repository.


Back on the Heroku site, under 'Deploy' , select Select 'Heroku Git'- which allows CLI interaction from the IDE terminal and use the following commands:
```
$ heroku login 
Press any key except q and (key in your credentials in the preview window)
$ git add .
$ git commit -am “initial commit to heroku”
$ git push Heroku master
```


On Heroku, select ‘Open app’ to see your live app.

## Local Deployment
This can be done by clicking ‘clone or download’ on my GitHub Repository.

Then install all the dependencies listed in the requirements.txt file

Create a .gitignore file containing, to prevent sensitive information being revealed in commits.
```
env.py
__pychache__
```
Then create an ‘env.py’ file in the root directory with the following code:
```
import os

os.environos.environ["STRIPE_PUBLIC_KEY"] = key
os.environ["STRIPE_SECRET_KEY"] = key
os.environ["STRIPE_WH_SECRET"] = key
```

For the rest reference the Django documentation.



Nav bar based on: https://demos.creative-tim.com/navbar-with-icons/index.html?_ga=2.98554264.649268495.1596619877-1871526498.1594128054
Font: https://www.fontsquirrel.com/fonts/Latin-Modern-Mono
Body Font: https://fonts.google.com/specimen/Open+Sans+Condensed?standard-styles=&sidebar.open=true&selection.family=Open+Sans+Condensed:ital,wght@0,300;0,700;1,300