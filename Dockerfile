FROM python:3.7

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8081

ENTRYPOINT [ "uvicorn app:app --port 8081" ]