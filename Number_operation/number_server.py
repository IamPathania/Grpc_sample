from concurrent import futures

import time
import grpc

import number_ops_pb2
import number_ops_pb2_grpc

_ONE_DAY_IN_SECONDS = 60*60*24

class DataRetrival():

    def __init__(self):
        self.square1 = 0
        self.square2 = 0
        self.addition = 0
        self.multiply = 0

    def inputData(self,request,context):
        print'Server side -- Data in request : ', request
        print'Num1', request.a
        print'Num2', request.b
        a= int(request.a)
        b= int(request.b)
        self.square1 = a*a
        self.square2 = b*b
        self.addition =a+b
        self.multiply =a*b

        return number_ops_pb2.Output(square1=self.square1,square2=self.square2,
                                     addition=self.addition,multiply=self.multiply )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    number_ops_pb2_grpc.add_DataRetrivalServicer_to_server(DataRetrival(),server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
