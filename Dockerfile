FROM python:3.8

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app.py /app
COPY contact.py /app

EXPOSE 5500

CMD ["python", "Auto Mecânica\forms\contact2.py" && "python", "Auto Mecânica\forms\contact.py"] 
