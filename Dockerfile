FROM python:3.7.0-alpine3.8

# create working dir
WORKDIR /app

# copy all necessary files in the working dir
COPY requirements.txt /app/
COPY DAAFi/ /app/DAAFi

# install the packages
RUN pip install -r requirements.txt

# make the usual flask port available
EXPOSE 5000

# set the executable of the Flak app
RUN cd /app
ENV FLASK_APP DAAFi

CMD ["flask", "run", "--host", "0.0.0.0"]
