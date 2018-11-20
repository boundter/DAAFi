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

# create a new daafi user with corresponding group
RUN addgroup --system --gid 5555 daafi \
    && adduser --system --no-create-home --uid 5555 --ingroup daafi daafi
USER daafi

# set the executable of the Flak app
WORKDIR /app
ENV FLASK_APP DAAFi

# add app directory to pythonpath for easier testing
ENV PYTHONPATH /app

CMD ["flask", "run", "--host", "0.0.0.0"]
