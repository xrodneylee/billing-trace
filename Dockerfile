FROM python:3-alpine
MAINTAINER guanpu.lee "xrodneylee@gmail.com"
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "run.py" ]