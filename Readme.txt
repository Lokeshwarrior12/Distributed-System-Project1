Project Description:

This project involves building a multi-threaded server and client for a simple image search engine using gRPC for communication and Docker for containerization. The server randomly returns an image containing the object specified by the user's search keyword. The system supports basic functionalities, including searching with object class keywords (e.g., "dog") and returning a randomly selected image matching the keyword.


How to Run the Project:
1. Setting Up the Environment:
Ensure you have Python, Docker, and Protocol Buffers installed on your system.

2. Building Docker Images:
Follow the guides for Python and Java to build Docker images for both server and client applications.

Imageserver Folder:
1. Build and Run the Server:

# Navigate to the Imageserver folder
cd Imageserver

# Build the Docker image for the server
docker build -t imageserver .

# Run the server container with imagepath mounted as a volume and port 8000 exposed
docker run -v /path/to/image/directory:/Images -p 8000:8000 imageserver

3. Running the Client:
Use Docker to run the client container:
grpcclient Folder:
1. Run the Client:
# Navigate to the grpcclient folder
cd grpcclient

# Run the Python client
python3 client.py

4. Running the Server:
Use Docker to run the multi-threaded server container:
grpcserver Folder:
1. Build and Run the Server with gRPC:
# Navigate to the grpcserver folder
cd grpcserver

# Build the Docker image for the server
docker build -t imageserver .

# Create a Docker network for gRPC communication
docker network create grpc-network

# Run the server container with network, imagepath, and port 8000 exposed
docker run --network grpc-network -v /path/to/image/directory:/Images -p 8000:8000 imageserver


5. Testing the System:
Design and execute 5 different test cases to validate the server-client interaction.




Project Structure:

1. /server:
Contains server-side code, including server.py and Dockerfile.server.

2./client:
Contains client-side code, including client.py and Dockerfile.client.

3. /proto:
Contains Protocol Buffers files (image_search.proto) and generated Python files (image_search_pb2.py and image_search_pb2_grpc.py).



How to Compile and Run:

Server:

Navigate to the /server directory.
Build Docker image for the server:
docker build -t image-search-server -f Dockerfile.server .

Run the server container:
docker run -d --name image-search-server-container image-search-server

Client:

Navigate to the /client directory.
Build Docker image for the client:
docker build -t image-search-client -f Dockerfile.client .

Run the client container:
docker run -d --name image-search-client-container image-search-client

Requirements Installation:
1. Install Docker Desktop
2. Install python, java in your computer 
then 
pip install -r requirements.txt








