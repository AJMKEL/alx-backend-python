# Messaging App - Docker Setup

## Build the Docker image
```bash
docker build -t messaging-app:latest .
```

## Run the container
```bash
docker run -d -p 8000:8000 --name messaging-app-container messaging-app:latest
```

## Access the application
Open your browser and navigate to: http://localhost:8000
