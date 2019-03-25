# Building and running

The setup container is only meant to be run once when initially
creating the db and loading the csv.

    docker-compose build
    docker-compose up -d db
    docker-compose up -d setup # only run once
    docker-compose up -d app

The running app can be found at <http://localhost:8000/>

The API can be found at:

http://localhost:8000/api/ships/
http://localhost:8000/api/positions/9632179

# Running Tests

The tests need the db container to be up.
These two commands need to be done before running the tests:

    docker-compose build # if not already built
    docker-compose up -d db

And then:

    cd app
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python test.py
