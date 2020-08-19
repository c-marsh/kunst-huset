This project uses Django to build a site for artists to sell art. It works on premise of artists being able to list their works, but the site taking payment and handling distribution as a physical gallery might.

# Design

## User Stories

<details>
  <summary>Click to view user Stories!</summary>

| Id         | As a/an | I want to be able to:                          | So I can                                                          |
| ---------- | ------- | ---------------------------------------------- | ----------------------------------------------------------------- |
| Admin      |         |                                                |                                                                   |
| 1          | Artist  | add work                                       | Add info and image of work                                        |
| 2          | Artist  | edit work                                      | Edit info and image of work                                       |
| 3          | Artist  | Remove work                                    | Remove info and image of work                                     |
| 4          | Artist  | sell work                                      | Add info and image of work                                        |
| 5          | Artist  | create a profile                               | Add info/create a portal about myself                             |
| Browsing   |         |                                                |                                                                   |
| 6          | Buyers  | Can browse/look for work                       | To see an array of available works                                |
| 7          | Buyers  | Can view details                               | To see more info about the piece of work                          |
| 8          | Buyers  | Can view info about artist                     | To find pieces of work                                            |
| 9          | Buyers  | Can search/filter                              | To find work by criteria                                          |
| Accounts   |         |                                                |                                                                   |
| 10         | Buyer   | Can make account                               | Create an account to access history of purchases/save information |
| 11         | Artist  | Can make account                               | To manage profile information and see a history of works sold     |
| 12         | Buyer   | Can edit account                               | To update info                                                    |
| 13         | Artist  | Can edit account                               | To update info                                                    |
| 14         | Buyer   | Can delete account                             | To remove info                                                    |
| 15         | Artist  | Can delete account                             | To remove info                                                    |
| Purchasing |         |                                                |                                                                   |
| 16         | Buyer   | Can complete a payment                         | securely complete a Strip transaction                             |
| 17         | Buyer   | Can view purchase details/total before payment | ensure purchase details are correct                               |
| 18         | Buyer   | Can provide shipping details                   | input correct info                                                |
| 19         | Buyer   | View a puchase history                         |                                                                   |
| 20         | Artist  | View a history of items sold                   |                                                                   |

</details>

## Design

The site is designed using a minimalist colour scheme. This is to allow the art to stand out from the site, while the site primarily uses smooth movements of menus and cards to complement the products on sale.

## Pages

The site is made up of the following pages:

### Home Page
<details>
  <summary> The Home page features</summary>

A featured artist, link to see more about them, and a link to more art.

<details>
  <summary> Wireframe</summary>

  ![Imgur](https://i.imgur.com/RIkZLxh.png)

</details>

### Gallery
<details>
  <summary> The gallery page features</summary>

-   a gallery view of cards of the art
    -   filterable ascending or descending by
        -   price,
        -   title,
        -   artist,
        -   category
    -   Searchable by
        -   description,
        -   title,
        -   artist,
        -   medium
    -   The search and filter provides feedback about what search terms have been used, how many items are returned, and provides a reset button.
-   The cards feature:
    -   a cropped window into the artwork
    -   a badge displaying the price, or "Sold" if the piece has been sold
-   On hover the cards additionally show:
    -   the title
    -   artist of the piece.
-   Clicking on the card takes one to the Detail page of the art.
-   A back to top button is provided for easy navigation.

</details>

<details>
  <summary>Wireframe</summary>

![Imgur](https://i.imgur.com/MKlyx5r.png)

</details>

### Artwork Page

<details>
  <summary> The Artwork page features</summary>

-   an overview of the piece
    -   A clickable thumbnail of the piece
        -   This opens a full screen view in a new tab
    -   title,
    -   artist,
    -   year/date produced,
    -   description,
    -   medium,
    -   dimensions/weight/duration as relevant
    -   quantity available
-   if the piece is available to buy:
    -   A field to add a quantity to cart, limited by the quantity available
    -   A button back to the gallery
-   if the piece has been sold
    -   A button back to the gallery

<details>
  <summary>Wireframe</summary>

![Imgur](https://i.imgur.com/1gjQQUG.png)

</details>

</details>

### Basket

<details>
  <summary> The basket page features</summary>

If there is nothing in the basket, text indicates the basket is empty and a button is provided to take the viewer back to the gallery. If the basket holds contents the display provides:

-   A summary of
    -   sub total
    -   shipping
    -   VAT/sales tax
    -   Grand Total
-   an overview of the pieces in the basket displayed as cards similar to those in the Gallery view so the view has a visual ideas of artworks in the basket, however with the following changes:
    -   A remove button to remove from basket
    -   quantity and total price shown on the card
    -   title,
    -   artist
    -   medium
    -   the cards aren't clickable other than the remove button.
-   The page features buttons to checkout, or return to gallery.

</details>

### Checkout

<details>
  <summary> The Checkout page features</summary>

-   A summary of
    -   sub total
    -   shipping
    -   VAT/sales tax
    -   Grand Total
-   an overview of the pieces in the basket displayed as cards exactly as shown in the basket view, however with remove button removed.
    -   A 3 step slider for input of:
        -   contact details on slide
        -   shipping details on second page
            -   with an option to store if logged in,
                -   or otherwise providing a log-in or register link
        -   payment details on the third page.
        -   An order summary presented after checkout
        -   Defensive design that ensures an order is created from return stripe webhook, in the case of a failure on the front end to create an order.

<details>
<summary>Wireframe: Checkout</summary>

![Imgur](https://i.imgur.com/WL5sImW.png)

</details>

<details>
<summary>Wireframe: Order Summary</summary>

![Imgur](https://i.imgur.com/CARuymk.png)

</details>

</details>

## Additional Features

### Administration

Custom styled login/out/account admin pages.

<summary>Wireframe</summary>

![Imgur](https://i.imgur.com/i9n8X2Z.png)

</details>


### Notifications

Notifications are provided by colour coded toasts to provide the user with feedback and assurance. These dismissable Toasts also feature a basket preview when items are added, and a button to take the browser to the basket.

### Menus

Two Menus are provided via means of hamburger icons at either end of the menu bar. These are:

<details>
  <summary> The Gallery Menu</summary>

This provides navigation of the art related elements with filters for categories, direct links to artists profiles, home and the unfiltered gallery.

![Imgur](https://i.imgur.com/UOJLItV.gif)

</details>

<details>
  <summary> The Account Menu</summary>

This provides navigation of the account and purchasing related elements and displays:

-   for non-logged in users:
    -   login/register options
    -   basket total and link
-   for logged in users:
    -   account management
    -   logout option
    -   basket total and link
-   for superusers:
    -   Administration portal
    -   account management
    -   logout option
    -   basket total and link

    ![Imgur](https://i.imgur.com/UOJLItV.gif)

</details>

### Profile/Artist Page

<details>
<summary>Artist page</summary>

This page acts as public for the artists. It shows:
- A profile image
- Name
- Location
- A biography
- Their work listed on the site.

The artists when logged in can see a button to edit the profile.


<details>
<summary>Database Design</summary>

![Imgur](https://i.imgur.com/QgniTCN.png)
</details>

</details>

## Database

<details>
<summary>Database Design</summary>

![Imgur](https://i.imgur.com/b1gJf8g.png)

</summary>

## Backend
This Project used Django, with Python, JavaScript, CSS and HTML as lanaguages to build the site. A number of python libraries were used which can be seen in the requirements.txt file along with Bootstrap and Jquery.

The project was built in Gitpod as an IDE, used Github for git control, and has been deployed to Heroku with static and media files served by Amazon AWS.


# Bugs

## Major

-   ~~Poor Database structure - Artist DB may be obsolete~~

-   ~~Order history not saving to profiles~~

-   While more items than inventory can't be added to a basket from the page, this could be added again by revisting the page. Ideally the basket should verify against the inventory of an item to prevent buying more than is in stock.

-   Checkout does not update inventory of stock or show an update an item as sold if the inventory is sold out. Ideally this would happen from the payment webhook.

-   Currently a user doesn't have to provide a name on signup. This could populate the list of Artists with a lot of blank entries. This could be solved by creating a custom sign up page to include name (most secure), redirecting to the edit profile page on sign-up (however this could be navigated aawy from without completing the form).


## Minor

-   ~~Artists disappear from menu on some pages~~
- Profile Deletion isn't functioning, and has been removed.

### Cosmetic

-   Artist fields for adding art displaying all users not just artists
-   Buttons on some form pages too close to text
-   Make right hand menu bass responsive to number of menu items.
-   image upload fields need styling

## Future Developement

- Outstanding issues
- Sign-up including more profile data
- Implement better use of the is_artist/is_customer fields to streamline menus.
- Better gallery filtering including filtering out sold pieces.

# Testing

## Test Driven Developement

While automated testing hasn't been used in development, continual testing of feature while being implemented has to ensure they work while being made. While a thorough record of this hasn't been kept, the commit list evidences some of this, and an example here exists of validating webhooks:

<details>
  <summary> Evidence of full successful payment process by disabling JS </summary>

![Imgur](https://i.imgur.com/b0iow7k.gif)

</details>

## Validation

Powermapper has been used for automated validation and assesment of the site. It provides a useful basis from which to start a testing regime on the front end.

<details>
  <summary> Results</summary>
**Issue Report **

Site quality report for https://cmh-kh.herokuapp.com/ produced on Tuesday, August 18, 2020.

**Category Results**

Overall Quality ██████████ 12 pages with quality issues

Errors ██████████ 12 pages with broken links or other errors

Accessibility ██████████ 12 pages with accessibility problems

Compatibility ██████████ 0 pages with browser specific issues

Search ██████████ 12 pages with search engine issues

Standards ██████████ 12 pages have W3C standards issues

Usability ██████████ 12 pages with usability issues

Totals 34 pages and images checked

<details>
  <summary> Errors </summary>

This section shows site quality issues, including broken links and server mis-configurations.

<details>
  <summary> Priority 1 </summary>

1 issues on 12 pages

<details>

  <summary><strike>This link is broken. The src or href is an empty string.</strike> FIXED</summary>

href='' or src='' can cause unexpected effects such as traffic spikes or cookie corruption, and causes JavaScript error events to fire on Firefox.

Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/> line 104\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/accounts/login/> line 117\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/accounts/password/reset/> line 117\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/accounts/signup/> line 117\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/artworks/> line 116\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 116\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 116\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 116\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 116\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 116\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/artworks/2/> line 113\
Link: Christopher Marsh-Hilfiker URL is empty.\
<https://cmh-kh.herokuapp.com/basket/> line 116

**Informative**

These messages are for information only and do not indicate errors

Spell checking was not enabled for this scan.

If you want to check spelling, set the language using the Edit Scan command in OnDemand.

<https://cmh-kh.herokuapp.com/> line 1

</details>

</details>

</details>

<details>

  <summary> Accessibility </summary>

This section shows accessibility issues, indicating problems for older users, people with disabilities or accessibility needs. Automated testing cannot detect all accessibility issues, so should be used alongside human testing.

<details>
  <summary> Level A</summary>

6 issues on 12 pages

<details>
  <summary> All fieldset elements should be labeled with legend elements. *</summary>

The first child element inside a fieldset must be a legend element, which provides a label or description for the group. legend elements in other positions may be ignored.

<https://cmh-kh.herokuapp.com/accounts/login/> line 146\
<https://cmh-kh.herokuapp.com/accounts/signup/> line 147

Guideline: [WCAG 2.1 A H71](https://www.w3.org/TR/WCAG-TECHS/H71.html) [Section 508 (2017) A H71](https://www.w3.org/TR/WCAG-TECHS/H71.html)

</details>

This applies to built in field sets by Django Auth. 

<details>
  <summary><strike>Each a element must contain text or an img with an alt attribute.</strike> FIXED</summary>

A link name allows screen readers to voice what the links does. If there is no link text or the `alt` text is blank, screen readers have nothing to read, so read out the URL instead. To add a name do one of the following:\

-   Add text between thea\
-   element start and end tags\
-   Add anaria-label\
-   attribute\
-   Add anaria-labelledby\
-   attribute\
-   Add an\
    img alt\
-   attribute if the link contains an\
    img\
-   element

<https://cmh-kh.herokuapp.com/artworks/> line 141\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 141\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 141\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 141\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 141\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 141

Guideline: [WCAG 2.1 A F89](https://www.w3.org/TR/WCAG-TECHS/F89.html) [Section 508 (2017) A F89](https://www.w3.org/TR/WCAG-TECHS/F89.html)

</details>

<details>
  <summary><strike>HTML form control has no accessible name.</strike> FIXED</summary>

A label (or name) linked to the control allows screen readers to voice the label correctly when reading the control. To add a label do one of the following:\

-   Use alabel\
-   element with thefor\
-   attribute set to the ID of the form control\
-   Wrap alabel\
-   element around the form control\
-   Add atitle\
-   attribute\
-   Add anaria-label\
-   attribute\
-   Add an\
    aria-labelledby\
-   attribute

<https://cmh-kh.herokuapp.com/accounts/login/> line 57\
<https://cmh-kh.herokuapp.com/accounts/password/reset/> line 57\
<https://cmh-kh.herokuapp.com/accounts/signup/> line 57\
<https://cmh-kh.herokuapp.com/artworks/> line 56 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 56 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 56 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 56 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 56 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 56 162 171\
<https://cmh-kh.herokuapp.com/artworks/2/> line 53 156\
<https://cmh-kh.herokuapp.com/basket/> line 56

Guideline: [WCAG 2.1 A F68](https://www.w3.org/TR/WCAG20-TECHS/F68.html) [Section 508 (2017) A F68](https://www.w3.org/TR/WCAG20-TECHS/F68.html)

</details>

<details>
  <summary><strike>Some pages have the same title, so the title cannot be used to distinguish pages.</strike>FIXED</summary>

Change the title elements so they are unique for each page.

'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/accounts/login/> line 48\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/accounts/password/reset/> line 48\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/artworks/> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/artworks/2/> line 44\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/> .\
<https://cmh-kh.herokuapp.com/basket/> line 47

Guideline: [WCAG 2.1 A F25](https://www.w3.org/TR/WCAG20-TECHS/F25.html) [Section 508 (2017) A F25](https://www.w3.org/TR/WCAG20-TECHS/F25.html)

</details>

<details>
  <summary>The label element is blank.*</summary>

Add text to the label describing the associated control.

<https://cmh-kh.herokuapp.com/> line 33\
<https://cmh-kh.herokuapp.com/accounts/login/> line 58\
<https://cmh-kh.herokuapp.com/accounts/password/reset/> line 58\
<https://cmh-kh.herokuapp.com/accounts/signup/> line 58\
<https://cmh-kh.herokuapp.com/artworks/> line 57\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 57\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 57\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 57\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 57\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 57\
<https://cmh-kh.herokuapp.com/artworks/2/> line 54\
<https://cmh-kh.herokuapp.com/basket/> line 57

Guideline: [WCAG 2.1 A 4.1.2](https://www.w3.org/TR/UNDERSTANDING-WCAG20/ensure-compat-rsv.html) [Section 508 (2017) A 4.1.2](https://www.w3.org/TR/UNDERSTANDING-WCAG20/ensure-compat-rsv.html)

</details>
*Fixed for the most part. A few places are the result of forms.

<details>
  <summary><strike>This button element is empty and has no accessible name.</strike> FIXED</summary>

A programmatically determined name allows screen readers to tell users what the control does. To add a name do one of the following:\

-   Add text between thebutton\
-   start and end tags\
-   Add atitle\
-   attribute\
-   Add anaria-label\
-   attribute\
-   Add anaria-labelledby\
-   attribute\
-   Add an\
    img alt\
-   attribute if the button contains an\
    img\
-   element

<https://cmh-kh.herokuapp.com/artworks/> line 156\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 156\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 156\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 156\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 156\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 156\
<https://cmh-kh.herokuapp.com/artworks/2/> line 152 158

Guideline: [WCAG 2.1 A 4.1.2](https://www.w3.org/WAI/WCAG21/Understanding/name-role-value.html) [Section 508 (2017) A 4.1.2](https://www.w3.org/WAI/WCAG21/Understanding/name-role-value.html)

</details>

</details>

<details>
  <summary>Level AA</summary>

2 issues on 1 pages

<details>
  <summary>Ensure that text and background colors have enough contrast.*</summary>

Some users find it hard to read light gray text on a white background, dark gray text on a black background and white text on a red background.\

-   The contrast ratio should be 3.0 or more for 18 point text, or larger\
-   The contrast ratio should be 3.0 or more for 14 point bold text, or larger\
-   The contrast ratio should be 4.5 or more for all other text

The text color to background color contrast ratio is:\
3.14 with color: rgb(108,117,125);background-color: rgb(40,40,40);font-size: 16.50pt;font-weight: 400;\
<https://cmh-kh.herokuapp.com/> line 133

Guideline: [WCAG 2.1 AA 1.4.3](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html) [Section 508 (2017) AA 1.4.3](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html)

</details>

*This applies to the copyright text in the footer. It is non-essential information.

<details>
  <summary>Provide information about the general layout of a site using a site map or table of contents.</summary>

You should provide a link labeled 'Site Map' or 'Sitemap' or the equivalent in your language, on every page.

<https://cmh-kh.herokuapp.com/> line 1

Guideline: [WCAG 2.1 AA 2.4.5](https://www.w3.org/TR/UNDERSTANDING-WCAG20/navigation-mechanisms-mult-loc.html) [Section 508 (2017) AA 2.4.5](https://www.w3.org/TR/UNDERSTANDING-WCAG20/navigation-mechanisms-mult-loc.html)

</details>

</details>

</details>

<details>
  <summary>Compatibility</summary>

This section shows pages that exhibit browser-specific behavior, or trigger browser bugs.

![Imgur](https://i.imgur.com/MJakhCF.png)

</details>

<details>
  <summary>Search</summary>

This section shows search engine guideline violations, and pages that don't comply with search optimization best practices.

<details>
  <summary>Priority 1</summary>

2 issues on 2 pages

<details>
  <summary>
Offer an HTML site map to your users with links that point to the important parts of your site.*</summary> 

Links embedded in menus, list boxes, and similar elements are not accessible to web crawlers unless they appear in your site map. If the site map is larger than 100 or so links, you may want to break the site map into separate pages.

<https://cmh-kh.herokuapp.com/> line 1

Guideline: [Google](https://www.google.com/webmasters/guidelines.html) [Bing](https://www.bing.com/webmaster/help/webmaster-guidelines-30fba23a)

</details>

*Low Priority for a first release

<details>
  <summary>
<strike>This page has no h1 element, which violates Bing webmaster guidelines.</strike>FIXED</summary>

Add an h1 element just before the main content describing the page.

<https://cmh-kh.herokuapp.com/artworks/2/> line 47

Guideline: [Bing](https://www.bing.com/webmaster/help/webmaster-guidelines-30fba23a)

</details>

</details>

<details>
  <summary>Priority 2</summary>

1 issues on 10 pages

<details>
  <summary><strike>This page title is not unique. Assign unique, descriptive title elements to every page</strike> FIXED</summary>

'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/accounts/login/> line 48\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/accounts/password/reset/> line 48\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/2/> line 44\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/basket/> line 47

Guideline: [Google](https://support.google.com/webmasters/bin/answer.py?answer=35624) [Bing](https://www.bing.com/webmaster/help/webmaster-guidelines-30fba23a)

</details>

</details>

<details>
  <summary>Priority 3</summary>

1 issues on 10 pages

<details>
  <summary><strike>No meta description tag found. Use a description tag that accurately describes the contents of a web page.</strike>FIXED</summary>

A well-written meta description attracts more clicks in search results than an irrelevant or missing description.

<https://cmh-kh.herokuapp.com/> line 1\
<https://cmh-kh.herokuapp.com/accounts/login/> line 1\
<https://cmh-kh.herokuapp.com/accounts/signup/> line 1\
<https://cmh-kh.herokuapp.com/artworks/> line 1\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 1\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 1\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 1\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 1\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 1\
<https://cmh-kh.herokuapp.com/basket/> line 1

Guideline: [Yahoo](https://help.yahoo.com/kb/search/search-content-quality-guidelines-sln2245.html) [Google](https://support.google.com/webmasters/bin/answer.py?answer=35624#1) [Bing](https://www.bing.com/webmaster/help/webmaster-guidelines-30fba23a)

</details>

</details>

Informative

These messages are for information only and do not indicate errors

No search keywords are set in SortSite, so no keyword optimization rules have been run.

If you want to check keyword optimization, set the keywords using the Edit Scan command in the OnDemand edition.

<https://cmh-kh.herokuapp.com/> line 1

Search engines cannot index areas of sites that require a log in.

<https://cmh-kh.herokuapp.com/accounts/login/> line 151\
<https://cmh-kh.herokuapp.com/accounts/signup/> line 154 155

Guideline: [Google Blogs](https://www.mattcutts.com/blog/guest-post-vanessa-fox-on-organic-site-review-session/)

</details>

</details>

</details>

<details>
  <summary>Standards</summary>

This section shows pages that do not comply with W3C standards.

<details>
  <summary>Priority 1</summary>

7 issues on 12 pages

<details>
  <summary><strike>Element div not allowed as child element in this context.</strike>FIXED</summary>

<https://cmh-kh.herokuapp.com/> line 55\
<https://cmh-kh.herokuapp.com/accounts/login/> line 59\
<https://cmh-kh.herokuapp.com/accounts/password/reset/> line 59\
<https://cmh-kh.herokuapp.com/accounts/signup/> line 59\
<https://cmh-kh.herokuapp.com/artworks/> line 58\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 58\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 58\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 58\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 58\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 58\
<https://cmh-kh.herokuapp.com/artworks/2/> line 55\
<https://cmh-kh.herokuapp.com/basket/> line 58

Guideline: [HTML5](https://html.spec.whatwg.org/multipage/)

</details>

<details>
  <summary><strike>End tag for body seen, but there were unclosed elements.</strike>FIXED</summary>

<https://cmh-kh.herokuapp.com/accounts/login/> line 200\
<https://cmh-kh.herokuapp.com/artworks/> line 240\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 227\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 227\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 227\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 240\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 227

Guideline: [HTML5](https://html.spec.whatwg.org/multipage/)

</details>

<details>
  <summary>The allowtransparency attribute on the iframe element is obsolete.*</summary> 
  
  Use CSS instead.

<https://cmh-kh.herokuapp.com/> line 144

Guideline: [HTML5](https://www.w3.org/TR/html5-diff/#obsolete-elements)

</details>

*This iframe is a result of Stripes security features and can't be modified.

<details>
  <summary><strike>The charset attribute on the link element is obsolete. Use an HTTP Content-Type header on the linked resource instead.</strike>FIXED</summary>

<https://cmh-kh.herokuapp.com/> line 10\
<https://cmh-kh.herokuapp.com/accounts/login/> line 21 30\
<https://cmh-kh.herokuapp.com/accounts/password/reset/> line 21 30\
<https://cmh-kh.herokuapp.com/accounts/signup/> line 21 30\
<https://cmh-kh.herokuapp.com/artworks/> line 21\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 21\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 21\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 21\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 21\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 21\
<https://cmh-kh.herokuapp.com/artworks/2/> line 21\
<https://cmh-kh.herokuapp.com/basket/> line 21

Guideline: [HTML5](https://html.spec.whatwg.org/multipage/)

</details>

<details>
  <summary>The frameborder attribute on the iframe element is obsolete. Use CSS instead.*</summary>

<https://cmh-kh.herokuapp.com/> line 144

Guideline: [HTML5](https://www.w3.org/TR/html5-diff/#obsolete-elements)

</details>

*The iframe is built as part of Stripes security features and can't be tampered with.

<details>
  <summary>The scrolling attribute on the iframe element is obsolete. Use CSS instead.*</summary>

<https://cmh-kh.herokuapp.com/> line 144

Guideline: [HTML5](https://www.w3.org/TR/html5-diff/#obsolete-elements)

</details>

*The iframe is built as part of Stripes security features and can't be tampered with.

<details>
  <summary><strike>Unclosed element div.</strike>FIXED</summary>

<https://cmh-kh.herokuapp.com/accounts/login/> line 200\
<https://cmh-kh.herokuapp.com/artworks/> line 240\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 227\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 227\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 227\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 240\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 227

Guideline: [HTML5](https://html.spec.whatwg.org/multipage/)

</details>

</details>

</details>

<details>
  <summary>Usability</summary>

This section shows general usability issues, indicating navigation problems for all users.

<details>
  <summary>Priority 2</summary>

6 issues on 12 pages

<details>
  <summary>An active 'Home' link on the home page makes some users think that it's not the home page.</summary>

<https://cmh-kh.herokuapp.com/> line 79

Guideline: [Usability.gov 5:6](https://www.powermapper.com/products/sortsite/rules/usegov5.6.2/)

</details>

<details>
  <summary><strike>Omitting img width or height attributes makes the page layout jump about as images load.</strike>FIXED</summary>

This makes the page very hard to read or click while it's loading. Fix by adding width and height attributes to the img tag matching the image dimensions. In responsive layouts, specifying width and height prevents layout jumping because the browser can pre-calculate the final image size when CSS like this is used: img { max-width: 100%; height: auto }

<https://cmh-kh.herokuapp.com/> line 115\
<https://cmh-kh.herokuapp.com/artworks/2/> line 130

Guideline: [Usability.gov 14:3](https://www.powermapper.com/products/sortsite/rules/usegov14.3/) [W3C](https://developer.mozilla.org/en-US/docs/Web/Media/images/aspect_ratio_mapping)

</details>

<details>
  <summary>Provide a search option on each page of content-rich web sites.*</summary>

A search option should be provided on all pages where it may be useful - users should not have to return to the homepage to conduct a search. Search engines can be helpful on content-rich web sites, but do not add value on other types of sites.

<https://cmh-kh.herokuapp.com/> line 1\
<https://cmh-kh.herokuapp.com/accounts/password/reset/> line 1\
<https://cmh-kh.herokuapp.com/accounts/signup/> line 1\
<https://cmh-kh.herokuapp.com/artworks/2/> line 1\
<https://cmh-kh.herokuapp.com/basket/> line 1

Guideline: [Usability.gov 17:4](https://www.powermapper.com/products/sortsite/rules/usegov17.4/)

</details>

*A search is provided on the gallery page which acts as the same function

<details>
  <summary><strike>This page title is not unique. Each page should have a descriptive and meaningfully different title.</strike>FIXED</summary>

Title refers to the text displayed on browser tabs, favorites, and in search engines results pages. If two or more pages have the same title, they cannot be differentiated by users or the Favorites capability of the browser.

'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/accounts/login/> line 48\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/accounts/password/reset/> line 48\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 47\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/artworks/2/> line 44\
'Kunst Huset ' is also used on <https://cmh-kh.herokuapp.com/>\
<https://cmh-kh.herokuapp.com/basket/> line 47

Guideline: [Usability.gov 9:2](https://www.powermapper.com/products/sortsite/rules/usegov9.2.2/)

</details>

<details>
  <summary><strike>Use label elements for each data entry field to show what data is expected.</strike>FIXED</summary>

Make sure each input field has an associated label describing the field.

<https://cmh-kh.herokuapp.com/artworks/> line 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=3d> line 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=multimedia> line 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=painting> line 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=photography> line 162 171\
<https://cmh-kh.herokuapp.com/artworks/?category=video> line 162 171

Guideline: [Usability.gov 13:5](https://www.powermapper.com/products/sortsite/rules/usegov13.5/)

</details>

<details>
  <summary>Use text links rather than image links. In general, text links are more easily recognized as clickable.*</summary>

Text links usually download faster, are preferred by users, and should change colors after being selected. It is usually easier to convey a link's destination in text, rather than with the use of an image. Users often find it hard to tell which images are clickable without moving the cursor over them ('minesweeping'). Another benefit to using text links is that users with text-only and deactivated graphical browsers can see the navigation options.

<https://cmh-kh.herokuapp.com/artworks/2/> line 130

Guideline: [Usability.gov 10:6](https://www.powermapper.com/products/sortsite/rules/usegov10.6/)

</details>

*This refers to clickable cards on the gallery page which clearly are links, and to images on the art detail pages, which is intuitive in that clicking on an image opens it up. 

</details>

<details>
  <summary>Priority 4</summary>

1 issues on 1 pages

<details>
  <summary>Use site maps for web sites that have many pages.</summary>

Site maps provide an overview of the Web site. They may display the hierarchy of the Web site, may be designed to resemble a traditional table of contents, or may be a simple index.

<https://cmh-kh.herokuapp.com/> line 1

Guideline: [Usability.gov 7:10](https://www.powermapper.com/products/sortsite/rules/usegov7.10/)

</details>

</details>

</details>

</details>

</details>

### Testing User Stories
<details>
  <summary>Click to view user Stories!</summary>

| Id         | As a/an | I want to be able to:                          | So I can                                                          |
| ---------- | ------- | ---------------------------------------------- | ----------------------------------------------------------------- |
| Admin      |         |                                                |                                                                   |


<details>
  <summary>| 5          | Artist  | create a profile                               | Add info/create a portal about myself                             |</summary>

Gif shows adding name to profile info to appear in Artist list.
![Imgur](https://i.imgur.com/e2Epljw.gif)

</details>

<details>
  <summary>| 1          | Artist  | add work                                       | Add info and image of work                                        |</summary>

![Imgur](https://i.imgur.com/JBzwFd7.gif)


</details>
<details>
  <summary>| 2          | Artist  | edit work                                      | Edit info and image of work                                       |</summary>

  ![Imgur](https://i.imgur.com/yLtEIpP.gif)

</details>
<details>
  <summary>| 3          | Artist  | Remove work                                    | Remove info and image of work                                     |</summary>

  ![Imgur](https://i.imgur.com/M5UR3bN.gif)

</details>
<details>
  <summary>| 4          | Artist  | sell work                                      | Add info and image of work                                        |</summary>

The artist can list and the consumer can buy.
</details>


| Browsing   |         |                                                |                                                                   |

<details>
  <summary>| 7          | Buyers  | Can view details                               | To see more info about the piece of work                          |</summary>
  
  ![Imgur](https://i.imgur.com/MbJGJDV.gif)
</details>
<details>
  <summary>| 8          | Buyers  | Can view info about artist                     | To find pieces of work                                            |</summary>

![Imgur](https://i.imgur.com/Byt8aZu.gif)

![Imgur](https://i.imgur.com/VzlvHQ1.gif)

</details>
<details>
  <summary>| 6 / 9          | Buyers  | Can browse/look for work / Can search/filter                              | To find work by criteria                                          |</summary>

Search by filter. A bug in the video shows that artist filter is by id number.
![Imgur](https://i.imgur.com/eZ0SXsk.gif)

Back to top button
![Imgur](https://i.imgur.com/AzpgLZL.gif)

</details>

| Accounts   |         |                                                |                                                                   ||

<details>
  <summary>| 10 / 11        | Buyer / Artist    | Can make account                               | Create an account to access history of purchases/save information |</summary>

Creating an account
  ![Imgur](https://i.imgur.com/X2d8teU.gif)

Logging in
  ![Imgur](https://i.imgur.com/5yM9sfa.gif)

</details>
<details>
  <summary>| 12 / 13        | Buyer / Artist   | Can edit account                               | To update info                                                    |</summary>
</details>

This can be done from the menu on the right

</details>
<details>
  <summary>| 14 /15         | Buyer / Artist  | Can delete account                             | To remove info                                                    |</summary>

  This currently can't be done.

</details>

| Purchasing |         |                                                |                                                                   |
</details>


<details>
  <summary>| 17         | Buyer   | Can view purchase details/total before payment | ensure purchase details are correct                               |</summary>

  Part 1: add to cart
  ![Imgur](https://i.imgur.com/DasYFyy.gif)

  PArt 2: see whats in cart and remove:
  ![Imgur](https://i.imgur.com/jSaEOup.gif)


</details>
<details>
  <summary>| 16/18         | Buyer   | Can provide shipping details / Can complete a payment                   | input correct info                                                |</summary>

  ![Imgur](https://i.imgur.com/RPi1X33.gif)
</details>
<details>
  <summary>| 19         | Buyer   | View a purchase history                         |                                                                   |</summary>
  
  This shows the order overview, how the rows are clickable to the full order page, and how the back button returns to the order history page.
  ![Imgur](https://i.imgur.com/5258Nss.gif)
</details>
<details>
  <summary>| 20         | Artist  | View a history of items sold                   |                                                                   |</summary>

This is a feature to be implemented at a later date. Artists can contact a superuser for this info.

</details>

These video cover most functionality on the site. All buttons have been tested, and the site has been viewed and checked for visual Compatibility on Chrome, Edge and Firefox.

<details>
  <summary>The site is responsive, and here are snapshots to demonstrate.</summary>

![Imgur](https://i.imgur.com/MZYnlC9.png)
![Imgur](https://i.imgur.com/jtrAzhK.png)
![Imgur](https://i.imgur.com/BxrkFzx.png)
![Imgur](https://i.imgur.com/ue8ZtEx.png)
![Imgur](https://i.imgur.com/arKcz9c.png)
![Imgur](https://i.imgur.com/bhPE2LK.png)
![Imgur](https://i.imgur.com/BxKawxu.png)
![Imgur](https://i.imgur.com/1QtNj5V.png)
![Imgur](https://i.imgur.com/CIQ8Y73.png)
![Imgur](https://i.imgur.com/0ofjhDS.png)
![Imgur](https://i.imgur.com/7u8gsXU.png)

</details>

# Deployment

This website was deployed on Heroku and can be found at https://kunst-huset.herokuapp.com/

## Heroku Deployment

First login and create your app on the Heroku site, and select a region. Then in the app settings, under ‘Config Vars’ you can should set the following Stripe keys which can be easily found on their dashboard after signing up.

-   STRIPE_WH_SECRET as your WH key
-   STRIPE_SECRET_KEY as the Stripe secret key
-   STRIPE_PUBLIC_KEY for the Stripe Public Key

Under the resources start a PostGres Database

Then create a ‘requirements’ file, which lists all the dependencies by typing in the following command in the bash terminal:

```
pip3 freeze > requirements.txt
```

Copy the postgres URL from Heroku config vars into the placeholder: `dj_database_url.parse(os.environ.get(POSTGRES URL))`

Run migrations to the new database with `python3 manage.py migrate`

Then use `python3 manage.py loaddata categories`. Due to the artworks dependencies on user profiles, it can't be migrated across.

Finally create a superuser with `python3 manage.py createsuperuser`.

This is now deployed to the Heroku PostGres database.

```
pip3 install gunicorn
pip3 freeze > requirements.txt
```

Will install gunicorn which acts as a webserver.

You will then need to create a ‘Procfile’, which lists the process types in an application:

```
echo web: gunicorn kunst-huset.wsgi:application > Procfile
```

This should then be commited to your repository before Pushing to Heroku:

```
Git add . > git commit -m “Setup Heroku” > git push
```

Add the app to ALLOWED_HOSTS in settings.py

This will update your repository.

Back on the Heroku site, under 'Deploy' , select Select 'Heroku Git'- which allows CLI interaction from the IDE terminal and use the following commands:

```
$ heroku login
Press any key except q and (key in your credentials in the preview window)
heroku config:set DISABLE_COLLECTSTATIC=1 --app kunst-huset
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

# Resources and Acknowledgements
Nav bars based on: https://demos.creative-tim.com/navbar-with-icons/index.html?_ga=2.98554264.649268495.1596619877-1871526498.1594128054 and from https://codepen.io/stevenrzy/pen/pogXXEB
Sliding button based on  - https://codepen.io/mrnathan8/pen/wvaJREX 
Font: https://www.fontsquirrel.com/fonts/Latin-Modern-Mono 
Icons from Fontawesome
Body Font: https://fonts.google.com/specimen/Open+Sans+Condensed?standard-styles=&sidebar.open=true&selection.family=Open+Sans+Condensed:ital,wght@0,300;0,700;1,300
Adapted from Code Institute Boutique Ado: https://github.com/ckz8780/boutique_ado_v1/blob/master/products/forms.py

Art from my instagram, Arabella Hilfiker, and the [MOMA](https://www.moma.org/collection/works/401353?locale=en&page=1&with_images=true) collection. 

I'm grateful for the huge amount Cormac Lawlors patience which has gone into chasing gunicorns in this project, the help of my mentor Akshat Garg, and the staff of Code Institute.