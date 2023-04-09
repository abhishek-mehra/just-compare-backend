# Set base image to Python
FROM python:3.10

# Set working directory to /app
WORKDIR /app

# Copy the rest of the application files to the container
COPY . .

# Install Poetry and dependencies
RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev


#entry point as main:
# CMD ["python","just_compare_backend/backend.py"]

CMD ["gunicorn", "just_compare_backend.backend:app", "-b", "0.0.0.0:5001"]
