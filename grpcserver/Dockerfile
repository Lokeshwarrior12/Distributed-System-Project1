# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install grpcio grpcio-tools protobuf

# Generate the gRPC code and run the server
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/server.proto
CMD ["python", "imageserver.py"]
