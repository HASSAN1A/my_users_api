# start by pulling the python image
FROM python:3.8-alpine
# Run commands from /app directory inside container
WORKDIR /app
# Copy requirements from local to docker image
COPY requirements.txt /app
# Install requirements
RUN apk add libffi-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir
# Copy everything from the current dir to the image
COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "run.py" ] 
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

