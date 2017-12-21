
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Hi there! Welcome to Cloud9 IDE!

To get you started, create some files, play with the terminal,
or visit http://docs.c9.io for our documentation.
If you want, you can also go watch some training videos at
http://www.youtube.com/user/c9ide.
 
## Activate virtual environment
source myvenv/bin/activate

## Run the server
python manage.py runserver 0.0.0.0:8080

## Start django shell
python manage.py shell

## Query user list from db
from django.contrib.auth.models import User
User.objects.all()

## Setting up venv on windows for python 2.x
- Install python 2.x without setting the paths
- Install virtualenv
`C:\Python27\Scripts\pip.exe install virtualenv`

Create the virtualenv with the name `myenv`
`C:\Python27\Scripts\virtualenv.exe myvenv`

- install using the requirements files
`pip install -r requirements.txt`

## Debugging django
- install pdbpp into the virtualenv
- run `python --pdb manage.py runserver 0.0.0.0:8080`
  - add a breakpoint `import pdb; pdb.set_trace()`
  - ll -> display function source
  - c -> continue
  - n -> next