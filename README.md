# kusjesmachine

kusjesmachine.com website

# TODO

Design:

- Event layout: using Streamfield block with events
- Hide header when scrolling


Tech:

- Backup website content **
- Build js with gulpfile
- Restore content in dev env
- Use video plugin
- Use mechanisms from ansible-multi-django (multi app)

# Running gulp

cd kusjesmachine/static/base_theme
npm install
gulp


# Getting started

Install postgress.

Create the user and database in postgress:

    createuser --pwprompt kusjesmachine-dev
    createdb -Okusjesmachine-dev -Eutf8 kusjesmachine-dev

Create schema's:

    ./manage.py migrate

Run the server:

    ./manage.py runserver
