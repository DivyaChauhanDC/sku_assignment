# start by pulling the python image
FROM python:3.8-buster

# copy the requirements file into the image
COPY ./requirements/local.txt medpay/local.txt

# switch working directory
WORKDIR /medpay

RUN pip install --upgrade pip

# install the dependencies and packages in the requirements file
RUN pip install -r local.txt

# copy every content from the local file to the image
COPY . /medpay

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]