FROM python:3.10.2

# Add codebase inside image
ADD ./app /wind-turbine

# Copy requirements files
COPY requirements/requirements.txt /requirements.txt

WORKDIR /wind-turbine

# Upgrade pip3 and install requirements
RUN pip3 install pip -U \
    && pip3 install -r /requirements.txt

EXPOSE 8000

# start uvicorn server in autoreload mode
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000", "--reload"]