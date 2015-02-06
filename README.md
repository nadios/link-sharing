# link-sharing

## Link-sharing is a simple secure temporary file sharing service.
## The service meets the following requirements:
* Upload file form returns an HTTP link that can be used to retrieve the file contents.
* The files are stored encrypted
* HTTP links are expired after a day and stop working

## To run the application follow the steps:
1. Clone git repo into your local folder:
`git clone https://github.com/nadios/link-sharing.git`

2. Move on to *linksharing* folder:
`cd linksharing`

3. Install required python libs:
`pip install requirements.pip`

4. Setup database by running the migrations:
`python manage.py migrate`

4. The application is running on django test server, so to run it sumply run the command:
`python manage.py runserver`
or in case your local port 8000 is already used, try next command changing `8080` to any available port number:
`python manage.py runserver 8080`

5. That is it! Now try [http://localhost:8000/upload](http://localhost:8000/upload) URL in your browser.

## The application is very simple and consists of two screens:
1. To upload a file simply click on *Choose file* link and browse your directory for any file
2. Click *Upload* button
In case everything went OK, you will see success screen containing the link for an uploaded file and *Upload more* button.

##TODOs
1. The implementation should be covered with unit tests. I suggest to cover at least 60% of code.
2. Right now we just test the time of file/token expiration and return the file if it's not yet expired.
In the future we should apply the mechanism of cleaning the redundant files and tokens from the file system and db.
I suggest using some CRON-trigger to accomplish, let's say once a day, the file and token cleaning.
We could use [Celery for that](http://www.celeryproject.org/)
3. We should apply PyLint code quality checking to support python coding standards
4. We should move the application from the test Django server to some production solution, i.e. NGINX, Heroku
5. We should switch to production database, SQLite is also only for test purposes. So, we should decide what is best option for that MySQL, PostgreSQL, or maybe noSQL solution like MongoDB

##Improvements
1. We should pay more attention to app security, possibly we should transfer it onto HTTPS, which could be done once it is transferred from django test server
2. Also we should limit the file types that user could store, the system could be less vulnarable if we forbid uploading `javascript` files which could basically be executed and the user info could be stolen
3. We should add user membership functionality. So user could be able to register and manage the uploaded files
