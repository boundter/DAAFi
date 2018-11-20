# DAAFi - Data Analysis and Administration for Finances

This program will handle the administration of finances with extended data analysis using machine learning.

## Getting Started

Getting started is, at least for now, not automated

### Docker - recommended

Create a container from the Dockerfile. It exposes the port 5000 of the container. The program can than be run with the following command (assuming the container is called daafi)

`docker run --rm -d -p 5000:5000 daafi`

The interface is then accessible in the browser under localhost:5000.

**For now the database is not saved and properly initialized.**

#### Dev Mode

To prepare the system, a new group has to be added. In the container the daafi user has the uid 5555 and the daafi grouo the gid 5555. To allow the program to write to the database, the whole project should be owned by the group with the gid 5555. This means adding the group

`sudo groupadd -g 5555 daafi`,

adding the user to the group

`sudo usermod -a -G daafi $(whoami)`

and change the ownership of the project

`chgrp -R daafi DAAFi`.

The dev mode of flask can be accessed by running

`docker run --rm -p 5000:5000 -e 'FLASK_ENV=development' -v $APPLOCATION:/app daafi`,

where $APPLOCATION is the directory containing the app. Afterwards the database needs to be initialized by running

`flask init_db`

in the container.
