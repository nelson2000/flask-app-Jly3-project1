FROM python:3.9-slim-buster
# create the work directory
RUN mkdir /app
# move to the work directory
WORKDIR /app
# copy the requirements.txt to the work directory 
COPY requirements.txt /app/requirements.txt

RUN  python3.9 -m pip install -r requirements.txt

EXPOSE 5000

COPY . /app

# USER flask
ENV FLASK_RUN_HOST=0.0.0.0
# run the application
CMD [ "python3.9", "app.py" ]