FROM python:3.11-slim

WORKDIR /app

# העתקת קובץ הטסטים
COPY test.py .

# התקנת requests (נדרש עבור קריאות HTTP)
RUN pip install --no-cache-dir requests

# פקודת הריצה של הטסט
CMD ["python", "test.py"]
