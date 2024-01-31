FROM python:3.8-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
COPY .env .env
ENV FIRST_SERVICE_URL "http://akram-server.h5f2c8d6dha6gsaf.eastus.azurecontainer.io/books"
EXPOSE 80
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
