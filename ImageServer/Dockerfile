FROM python:3.12

#working directory in the container
WORKDIR /app

#copying the server code to the container
COPY server.py /app/server.py


#exposing the port where the server runs
EXPOSE 8000

#command to start the server when the container starts
CMD ["python", "server.py"]
