import grpc
import number_ops_pb2
import number_ops_pb2_grpc

def input_data():
    channel = grpc.insecure_channel('localhost:50052')
    stub = number_ops_pb2_grpc.DataRetrivalStub(channel)

    num1 = raw_input('Please enter first number:')
    num2 = raw_input('Please enter second number:')

    response = stub.inputData(number_ops_pb2.InputNos(a=int(num1),b=int(num2)))
    print("Client side -- set_data client service")
    print 'Square of first number',response.square1
    print 'Square of second number',response.square2
    print 'Addition',response.addition
    print 'Multiply',response.multiply

if __name__ == '__main__':
    input_data()



