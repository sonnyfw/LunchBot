
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Run the Flask app with gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:app"]
