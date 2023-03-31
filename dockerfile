# Set base image to Python
FROM python:3.10

# Set working directory to /app
WORKDIR /app

# Copy the rest of the application files to the container
COPY . .
# # Copy the poetry files to the container
# COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Set environment variable for Flask
ENV FLASK_APP=just_compare_backend/backend.py

# Expose port 5001 for the Flask server
EXPOSE 5001

# Start the Flask server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
