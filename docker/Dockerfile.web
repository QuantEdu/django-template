# - start with python image
FROM python:3

# - set PYTHONBUFFERED value to 1
ENV PYTHONUNBUFFERED 1

# - add code folder inside
RUN mkdir /code

# - set the working directory for all further commands
WORKDIR /code

# - add file requirements.txt to /code/ inside image
ADD django/requirements.txt /code/

# - install all requirements
RUN pip install -r requirements.txt

# - copy all other files to /code/ directory
ADD ./django/ /code/
