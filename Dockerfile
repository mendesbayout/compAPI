FROM python:3.11

# Create the app folder and set the workdir for subsequent instructions
ENV APP_FOLDER=/opt/app
WORKDIR $APP_FOLDER

# Specify the requirements file, the default is requirements.txt
ARG REQUIREMENTS_FILE=requirements.txt

# Install dependencies
COPY $REQUIREMENTS_FILE .
RUN pip install pip-tools==7.3.0 && \
  pip-sync $REQUIREMENTS_FILE


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
