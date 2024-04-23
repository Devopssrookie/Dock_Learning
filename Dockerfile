FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /usr/src/app
COPY . /code/
COPY Requirement.txt ./
RUN pip install --no-cache-dir -r Requirement.txt
# Expose the port that the Django app will run on
EXPOSE 8000
 
# Define the command to run the Django app when the container starts
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
