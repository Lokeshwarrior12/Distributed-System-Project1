import grpc
import client_pb2
import client_pb2_grpc

def grpc_client():
    channel = grpc.insecure_channel('127.0.0.1:8000')
    stub = client_pb2_grpc.ImageServiceStub(channel)

    obj_name = input("Enter the image type: ")
    request = client_pb2.ImageRequest(object_name=obj_name)

    response = stub.GetRandomImage(request)
    
    if response.image_data == b'Image not found':
        print("Image not found")
    else:
        with open('recvImage.jpg', 'wb') as imagefile:
            imagefile.write(response.image_data)
        print("Image received as 'recvImage.jpg'")

if __name__ == '__main__':
    grpc_client()
