# Instructions

### This is for development purposes, to deploy to production:

https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/

## _todo: put things in sh files_

Install project with:

```
pipenv install
```

Also, from the app/http/web/ directory:

```
npm i
npm run build
```

Activate virtual environment with:

```
pipenv shell
```

Exit with:

```
exit
```

To run API on port 4433:

```
FLASK_APP=$PWD/app/http/api/endpoints.py FLASK_ENV=development pipenv run python -m flask run --port 4433
```

or

```
FLASK_APP=app/http/api/endpoints.py FLASK_ENV=development pipenv run python3 -m flask run --port 4433
```

To make a python directory:

```
mkdir -p path/to/directory
```
