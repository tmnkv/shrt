# URL Shortener

##Work with

### Generate piblic SSH key
```bash
ssh-keygen
```

###Clone project repository
```bash
git clone git@github.com:tmnkv/shrt.git
```

###Rename repository dir for the visibility
```bash
mv shrt/ shrt_project
```

###Go to the repository level dir
```bash
cd shrt_project/
```

###Make virtual environment with python interprener
```bash
virtualenv -p python3 env
```

###Generate SECRET_KEY at [this site](http://www.miniwebtool.com/django-secret-key-generator/).

###Place your prod environment variables into activate file
```bash
vim env/bin/activate
```

###Activate your virtual environment
```bash
source env/bin/activate
```

###Go to the project level dir
```bash
cd shrt_project/
```

###Install project dependencies
```bash
pip install -r requirements/production.txt
```

###Collect static files
```bash
python manage.py collectstatic
```

###Test gunicorn
```bash
gunicorn config.wsgi:application --bind <your IP>:8000
```