import grpc
from concurrent import futures
import image_service_pb2
import image_service_pb2_grpc
import os
import random
import time

class ImageService(image_service_pb2_grpc.ImageServiceServicer):
    def GetRandomImage(self, request, context):
        obj_name = request.object_name
        images_directory = ''
        images = []
        path = '/Images/'  # Path for the images

        for name in os.listdir(path):
            if obj_name in name:
                images_directory = name

        images_path = path + images_directory

        for file in os.listdir(images_path):
            images.append(file)

        if images:
            rand_image = random.choice(images)
            print(rand_image)
            with open(os.path.join(images_path, rand_image), 'rb') as img_file:
                image_data = img_file.read()
                return image_service_pb2.ImageResponse(image_data=image_data)
        else:
            return image_service_pb2.ImageResponse(image_data=b'Image not found')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_service_pb2_grpc.add_ImageServiceServicer_to_server(ImageService(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    print("gRPC server running on [::]:8000")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
