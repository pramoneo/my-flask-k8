FROM python:3.7-alpine
WORKDIR /project
COPY . /project
RUN pip install -r requirement.txt
CMD ["python","app.py"]
