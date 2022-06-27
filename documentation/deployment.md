# **Deployment**

This project was created in Gitpod and deployed on Heroku. I deployed a first time right after its initial setup, in order to ensure everything was in order and automatic developments were enabled.  
These are the steps to deploy:
* Create a Heroku app  
   - After installing Django and the supporting libraries needed, log in to Heroku.
   - On the personal dashboard, click the *New* button in the top-right portion of the page, then *Create new app*. Choose a name for the app, then a location ("Europe", in this case).
   - After the app is created, click on the *Resources* tab in the menu bar, then search for *Heroku Postgres* to add a database to the current app.
   - Click on the *Settings* tab in the menu bar, then *Reveal Config Vars*, then copy the database URL.
* Attach the database
   - In Gitpod, create an *env.py* file.
   - In the *env.py* file, import the os library: 
     ```
     import os
     ```
   - Then, set the environment variables: 
     ```
     os.environ["DATABASE_URL"] = "Heroku DATABASE_URL Link here"
     ```
   - Add a secret key: 
     ```
     os.environ["SECRET_KEY"] = "Personal SecretKey here"
     ```
   - In Heroku's *Config Vars*, paste the SECRET_KEY: 
     ```
     SECRET_KEY, “randomSecretKey”
     ```
* Prepare environment and settings.py file
   - In *settings.py*, reference the *env.py* file: 
      ```
      import os
      import dj_database_url
      if os.path.isfile("env.py"): import env 
      ```
   - Remove the previous secret key and create a link to the new one now present on Heroku:
     ```
     SECRET_KEY = os.environ.get('SECRET_KEY')
     ```
   - Comment out the pre-set database information and add a new one that links to the DATABASE_URL variable created on Heroku:
      ```
      # DATABASES = {
      #    'default': {
      #        'ENGINE': 'django.db.backends.sqlite3',
      #        'NAME': BASE_DIR / 'db.sqlite3',
      #  } 
      #}
      ```
   - Add new database section:
     ```
     DATABASES = { 
         'default':
      dj_database_url.parse(os.environ.get("DATABASE_ URL"))
      }
     ```
   - From the Terminal, save all files and make migrations:
      ```
      python3 manage.py migrate
      ```
* Get static and media files stored on Cloudinary
   - On Cloudinary, create an account if in lack of one.
   - From the Cloudinary dashboard, copy the API environment variable, then add it to the *env.py* file on Gitpod:
      ```
      os.environ["CLOUDINARY_URL"] = "cloudinary://************************"
      ```
   - On Heroku, add a CLOUDINARY_URL variable to the *Config Vars* section, then paste the previously copied environment variable:
      ```
      CLOUDINARY_URL, cloudinary://************************
      ```
   - On Heroku, add an additional, temporary DISABLE_COLLECTSTATIC variable, settings its value to 1. This will be deleted before the final deployment:
      ```
      DISABLE_COLLECTSTATIC, 1
      ```
   - Move back to the *settings.py* file. Add Cloudinary libraries to installed apps. Make sure to follow this order:
      ```
      INSTALLED_APPS = [ ...,
         'cloudinary_storage',
         'django.contrib.staticfiles',
         'cloudinary',
         ..., ]
      ```
   - Set up Django to use Cloudinary for the storage of media and static files:
      ```
      STATIC_URL = '/static/'
      STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudin aryStorage'
      STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
      STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
      MEDIA_URL = '/media/' DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStor age'
      ```
   - Under BASE_DIR, link file to the templates directory:
      ```
      TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
      ```
   - Change the templates directory to TEMPLATES_DIR:
      ```
      TEMPLATES = [ 
         {
            ...,
            'DIRS': [TEMPLATES_DIR], 
            ...,
               ], 
            },
         }, 
      ]
      ```
   - Add Heroku name to ALLOWED_HOSTS:
      ```
      ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]
      ```
   - In Gitpod, add three folders in the top-level directory: "media", "static" and "templates"
   - Add a Procfile in the top-level directory.
   - In the Procfile, add : 
      ```
      web: gunicorn PROJ_NAME.wsgi
      ```
   - In the terminal, add all files, commit as "Deployment commit", then push.
   - In Heroku, go to the *Deploy* tab in the menu bar, connect the app to the GitHub repository and enable automatic deployments.
* Before the final deployment:
  - In the project's *settings.py* file, Ensure "Debug" is set to "False.
  - Delete the DISABLE_COLLECTSTATIC from the *Config Vars* on Heroku.