# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import data_retrieval_pb2 as data__retrieval__pb2


class DataRetrivalStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.setData = channel.unary_unary(
        '/com.data.retrieval.DataRetrival/setData',
        request_serializer=data__retrieval__pb2.Employee.SerializeToString,
        response_deserializer=data__retrieval__pb2.ResponseMsg.FromString,
        )
    self.getData = channel.unary_unary(
        '/com.data.retrieval.DataRetrival/getData',
        request_serializer=data__retrieval__pb2.Version.SerializeToString,
        response_deserializer=data__retrieval__pb2.EmployeeList.FromString,
        )


class DataRetrivalServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def setData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataRetrivalServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'setData': grpc.unary_unary_rpc_method_handler(
          servicer.setData,
          request_deserializer=data__retrieval__pb2.Employee.FromString,
          response_serializer=data__retrieval__pb2.ResponseMsg.SerializeToString,
      ),
      'getData': grpc.unary_unary_rpc_method_handler(
          servicer.getData,
          request_deserializer=data__retrieval__pb2.Version.FromString,
          response_serializer=data__retrieval__pb2.EmployeeList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.data.retrieval.DataRetrival', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
