# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /front

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the current directory into the container
COPY . .

# Expose the port that your Streamlit app will be running on
EXPOSE 8501

# Set the command to run your Streamlit app
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]