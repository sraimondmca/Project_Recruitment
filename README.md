# Project_Recruitment


# To fetch source code
git clone https://github.com/sraimondmca/Project_Recruitment.git

# Create a virtualenv 
mkvirtualenv --python=/usr/bin/python2.7 mysite-virtualenv
#TIP: if you see an error saying mkvirtualenv: command not found, check out InstallingVirtualenvWrapper.

# install dependencies
 pip install -r requirements.txt
 
 # Migrate
 start a bash console, use cd to navigate to the directory where Django project's manage.py lives, then run

./manage.py migrate

# Run django server
./manage.py runserver 

and then open in your browser localhost:port number
