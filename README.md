# Instructions

## Install project

```
pipenv install
```

## Run API

```
pipenv shell
```

Then

```
FLASK_APP=$PWD/server/routes.py FLASK_ENV=development pipenv run python -m flask run --port 4433
```

or

```
FLASK_APP=server/routes.py FLASK_ENV=development pipenv run python3 -m flask run --port 4433
```

## Exit pipenv

```
exit
```

## Some personal notes

To make a python directory:

```
mkdir -p path/to/directory
```

Work with fork from one's own repo: http://deanmalone.net/post/how-to-fork-your-own-repo-on-github/
