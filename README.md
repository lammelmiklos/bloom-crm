# bloom-crm
CRM for student growth management

Git commands to setup GitHub repo (if the GitHub repo got created after the local commits):
git remote add origin git@github.com:lammelmiklos/bloom-crm.git
git pull origin master --allow-unrelated-histories
git push -u origin master

Commands:
django-admin startproject <projectname>
python manage.py runserver
python manage.py startapp <appname>

This creates a much nicer Django shell
pip install ipython 
python manage.py shell


TODO: 
- fix the secret key issue



Set up Vs Code for Django - put this in settings.json:

  "files.associations": {
    "**/*.html": "html",
    "**/templates/**/*.html": "django-html",
    "**/templates/**/*": "django-txt",
    "**/requirements{/**,*}.{txt,in}": "pip-requirements",
  },
    
  "emmet.includeLanguages": {"django-html": "html"},

