FROM python:3.12-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip pipenv

COPY Pipfile* ./

RUN pipenv install --deploy --ignore-pipfile

COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]