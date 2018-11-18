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

The dev mode of flask can be accessed by running

`docker run --rm -p 5000:5000 -e 'FLASK_ENV=development' -v $APPLOCATION:/app daafi`

, where $APPLOCATION is the directory containing the app. Afterwards the database needs to be initialized by running

`flask init_db`

in the container.
