Simple REST interface to EUDAT services
=======================================

Installation
------------

Required python packages:

- flask
- requests
- Flask-SQLAlchemy
- marshmallow


Instructions:

  pip install flask requests Flask-SQLAlchemy marshmallow

  git clone https://github.com/EudatHttpApi/http-api.git

  git clone https://code.google.com/p/irodspython/
  # follow install instructions in irodspython/PyRods/

  cd http-api
  ./service\_twistd.sh start

Find more detailed instructions including how to install in a virtualenv here:
https://github.com/EudatHttpApi/http-api/wiki/Installation-guide


Coding Style
------------
Primarily all code has to adhere to PEP8 http://legacy.python.org/dev/peps/pep-0008/.
We only divert from this using 2 spaces indentation instead of 4 spaces.
This must be followed as well.
