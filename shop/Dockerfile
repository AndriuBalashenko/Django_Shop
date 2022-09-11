# pull official base image
FROM python:3.10
# set work directory
WORKDIR ./shop
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . /shop/

RUN mv -f fix_trans.py /usr/local/lib/python3.10/site-packages/django/utils/translation/__init__.py
ENTRYPOINT ["/shop/entrypoint.sh"]