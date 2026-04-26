FROM python:3.8.3-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install PyMySQL
RUN pip install -r requirements.txt
RUN pip install --upgrade 'SQLAlchemy<1.4'
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
