FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения и зависимости
COPY app /app
COPY requirements.txt /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт, который будет прослушиваться
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
