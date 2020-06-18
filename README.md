The frontend for this project is at: https://github.com/Janell-Huyck/drf_shoestore_frontend

# drf_shoestore

This project is an exploration of the Django REST framework.  It creates an API for a potential "shoe store"
with models for Manufacturer, ShoeType, ShoeColor, and Shoe.  

Additionally, there is a custom manage.py command, "bootstrap_data" that will pre-populate the ShoeType and
ShoeColor tables with initial values.

## SetUp:
From your terminal:

* Make a clone of the project: $ git clone https://github.com/Janell-Huyck/drf_shoestore.git
* Set up the virtual environment via poetry: $ poetry install
* Activate the virtual environment: $ poetry shell
* Make and migrate the tables: 
  * $ python manage.py makemigrations
  * $ python manage.py migrate
* Run the custom command: $ python manage.py bootstrap_data
  * Note: because of the way this project is set up, this step is mandatory
* Make your own superuser: $ python manage.py createsuperuser
* Start the server locally: $ python manage.py runserver
* Navigate over to the admin panel ( http://127.0.0.1:8000/admin/ ) and add manufacturer(s) and shoe(s)

## Accessing the API
All API endpoints are accessed with the /api/ url.  For example, the main API on your local host is at http://127.0.0.1:8000/api/

## Easter Egg
There is a "plausible, but likely false, fact about Joe's life growing up on the African Savanna 
as a comment somewhere in the codebase". (As requested by the assessment's rubric)  Enjoy!



