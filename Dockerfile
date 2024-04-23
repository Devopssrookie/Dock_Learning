# Use an official Python runtime as a parent image
FROM python:3.10-slim
 
# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
 
# Set the working directory in the container
#WORKDIR /code
WORKDIR /usr/src/app
# Copy the project files into the container at /code
COPY . /code/
COPY Requirement.txt ./
# Install dependencies
#RUN pip install --upgrade pip
#RUN pip install -r Requirement.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r Requirement.txt 
# Expose the port that the Django app will run on
EXPOSE 8000
 
# Define the command to run the Django app when the container starts
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
