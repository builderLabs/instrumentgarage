## Site Usage:


**Navigation Basics**

The main page lists categories of musical instruments which may be clicked  
on to list individual instruments in the category.  As an alternative, users  
may also view instruments as listed by brand,  similar to the display alternative  
many online music retailers also offer.

Clicking on either a brand or a category heading will return a listing of the  
instruments available in either that category or brand.  The entries which  
appear here are summarizes/highlights of the instrument entries for which more  
detail may be accessed by following the 'More' link under each instrument.

Clicking on a 'More' link will render a full page dedicated to that particular  
instrument with full descriptive details including postage by user.

Instrument-page functionality is restricted to viewing-only if the user is  
either not registered or not logged-in.  Registering and/or logging-in gives  
the user the ability to post/edit/delete instrument listings.

Registration and sign-in is done via OAuth 2.0 using Google sign-in and new  
users are added to the user database based on authorizations agreed to by the  
client.

Posting functionality is made available to any signed-in user.  However,  
editing/deleting functionality is restricted to original posters of the  
respective items with a confirmation page used for deletions.  

A token 'Purchase' button reveals the contact information of the poster of  
the item (which in production would likely require an agreement in terms of  
use or be otherwise centrally handled for privacy purposes).


**Posting/Editing Items**

A category-subcategory parent-child relationship is enforced during  
the posting/editing process such that the specified subcategory for the posting  
(pianos) must be a child of the specified parent category (keyboards).  

Required fields are annotated with an asterisk on the posting page and include  
category, subcategory, brand, and condition.  The fields model, description, and  
price are optional for posting/editing purposes.

Errors are raised when any combination of missing required fields are 
not provided.  

In addition to the pre-canned categories/subcategories and instruments which  
come with the initial database, custom categories/subcategories/brands may be  
added.  Error checks are performed in these instances as well, to ensure  
data integrity/consistency.

Enjoy the demo project!
