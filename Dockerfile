# Використовуємо базовий образ Python
FROM python:3.9

# Встановлюємо залежності
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копіюємо проект
COPY . .

# Запускаємо додаток
CMD ["python", "app.py"]

