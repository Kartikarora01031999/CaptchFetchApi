# CaptchFetchApi
repo for randeep


Commands to deploy on Heroku:

Create a copy of the folder
 
cp -r CaptchaFetch/ Deploy/

move to that folder:

cd Deploy/

Remove existing git:

sudo  rm -r .git/

Initialize a new git repo:

git init

Add files:

git add .

Make commit :

git commit -m <message>

Do heroku login:

heroku login 

or

 heroku login -i

Create a heroku app:

heroku create <appName>

Deploy to heroku:

git push heroku master
