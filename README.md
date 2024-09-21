# Fast API integration and testing API

This project is more structured as I started with a testing environment, i used FastApi and SQLAlchemy to make a database using Python simulating a client with specifications and different attributes that the database needed

I first created a connection between docker and alembic so I could push the updates inside the docker container, also I made a different database called test so I could test the updates before going into the production database

With this setup, i could develop my models in the app with the features specified by the client and also have some template tests I could modify or check the errors I could have with said database, making it more organized and secure if this were a professional environment, also making it ready to deployment thanks to docker

This is more a showcase on my ways to work with this kind of methodology and serves as an experience for future apps in need of a more sophisticated data pipeline with testing and integration included
