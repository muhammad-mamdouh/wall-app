# Wall App
> This is a social-app with the main features you need in any social app. You can create 
your own account to share new messages on the wall with others, you can read others' messages, 
you can comment on any shared messages, you can draft messages to be shared later and 
if you have some app and want wall app's data as a service you can use the provided Messages-API.

## Usage
To be able to make this app up and running follow along with me.

#### 1. Go and clone wall app's repo. 

#### 2. Create & Run a virtual environment for this app.
> Open your terminal, go to the wall app's cloned repo's directory, and run this command

```
# Make sure you installed virtualenv
pip install --upgrade virtualenv
```

```
# Create a virtual environment for the wall app
virtualenv wallvenv
```

```
# Activate the wallvenv virtual environment
source wallvenv/bin/activate
```

#### 3. Install all of the needed packages.
> From your terminal running your wallvenv, run the following command

```
cd src/
pip install -r requirements.txt
```

#### 4. If you'll use my test db, you don't need this step.
> Run the migrations

```
python manage.py makemigrations
```

```
python manage.py migrate
```


#### 5. Now, your configs are completed just run the application.
```
python manage.py runserver
```

## Features Screenshots
[Go to this link, you'll find a directory with screens to all of the site's features](https://drive.google.com/drive/folders/1_Qr1wBXU7BVw0_CeBwSAefInk-BU5c7U)