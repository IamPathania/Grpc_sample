from concurrent import futures

import time
import grpc

import data_retrieval_pb2
import data_retrieval_pb2_grpc

_ONE_DAY_IN_SECONDS = 60*60*24

class DataRetrival():

    def __init__(self):
        self.emp_name_list = list()
        self.emp_id_list = list()
        self.emp_desig_list = list()

    def setData(self,request,context):
           print ('Server side -- Data in request : ',request)
           # print'Name', request.name
           # print'ID', request.emp_id
           # print'Name', request.designation

           self.emp_name_list.append(request.name)
           self.emp_id_list.append(request.emp_id)
           self.emp_desig_list.append(request.designation)

           return data_retrieval_pb2.ResponseMsg(msg = "Server side -- Data Is Recieved")

    def getData(self,request,context):
           return data_retrieval_pb2.EmployeeList(emp_id = self.emp_id_list,  name = self.emp_name_list, designation = self.emp_desig_list)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_retrieval_pb2_grpc.add_DataRetrivalServicer_to_server(DataRetrival(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

