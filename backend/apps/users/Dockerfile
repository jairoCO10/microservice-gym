FROM python:3.10

WORKDIR /users

COPY ./libraries/requirements.txt .

RUN apt-get update && apt-get install -y build-essential libssl-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 8060

CMD [ "python", "main.py" ]