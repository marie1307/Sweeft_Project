FROM python:3.12.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt


RUN python manage.py collectstatic --noinput


EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "workout_plan.wsgi:application"]
