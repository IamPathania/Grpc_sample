import grpc

import data_retrieval_pb2
import data_retrieval_pb2_grpc

def set_data():
    channel = grpc.insecure_channel('localhost:50051')
    stub = data_retrieval_pb2_grpc.DataRetrivalStub(channel)

    id   =   input('Please enter emp_id:')
    name = raw_input('Please enter name:')
    desig = raw_input('Please enter designation:')

    response = stub.setData(data_retrieval_pb2.Employee(emp_id= id, name=name, designation = desig))
    print("Client side -- set_data client service :" , response.msg)

    response = stub.getData(data_retrieval_pb2.Version(version='1'))
    print("Client side -- get_data client service : \n Rollno : %s \n Name : '%s' \n designation: '%s'"%
          (response.emp_id,response.name,response.designation))


if __name__ == '__main__':
    set_data()