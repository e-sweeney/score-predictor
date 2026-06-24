FROM python:3.8

WORKDIR /opt/Student_score
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN python3 model.py
EXPOSE 5000
CMD ["python3.8", "flaskapp.py"]

