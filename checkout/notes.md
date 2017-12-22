Models for check out page

name
rev
display
ip
serial number
ID
firmware
location

availability_status{
    inuse
    offline
    available
}

We need to following functionality

- add new machines
- update existing machines
- claim existing machines

### Initialize database
After you specify the model, run the following to create
the migration

python manage.py makemigrations checkout

Where `checkout` is the name of the app


To apply the migration

`python manage.py migrate checkout`


This will apply the changes to the database

## Register the model
You can register the model in admin.py
 
`admin.site.register(Elvis)`

Make sure you have a user set update
https://tutorial.djangogirls.org/en/django_admin/

## Handling tables in templates
One way to do it would be using the cycle tag
https://stackoverflow.com/questions/9388064/django-template-turn-array-into-html-table

