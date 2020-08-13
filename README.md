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

</details>

## Additional Features

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







Nav bar based on: https://demos.creative-tim.com/navbar-with-icons/index.html?_ga=2.98554264.649268495.1596619877-1871526498.1594128054
Font: https://www.fontsquirrel.com/fonts/Latin-Modern-Mono
Body Font: https://fonts.google.com/specimen/Open+Sans+Condensed?standard-styles=&sidebar.open=true&selection.family=Open+Sans+Condensed:ital,wght@0,300;0,700;1,300