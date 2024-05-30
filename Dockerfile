FROM python:3.12.3

# Set the working directory to /app
WORKDIR /app

# Copy only the requirements file to the container and install dependencies
COPY requirements.txt /app/

# Install the dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app

EXPOSE 8080
ENTRYPOINT ["streamlit", "run", "reco.py", "--server.port=8080"]