# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import example_pb2 as example__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ExamplePhotoServiceStub(object):
  """Service definitions
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateUser = channel.unary_unary(
        '/example.photoservice.ExamplePhotoService/CreateUser',
        request_serializer=example__pb2.User.SerializeToString,
        response_deserializer=example__pb2.User.FromString,
        )
    self.GetUser = channel.unary_unary(
        '/example.photoservice.ExamplePhotoService/GetUser',
        request_serializer=example__pb2.GetUserRequest.SerializeToString,
        response_deserializer=example__pb2.User.FromString,
        )
    self.UpdateUser = channel.unary_unary(
        '/example.photoservice.ExamplePhotoService/UpdateUser',
        request_serializer=example__pb2.UpdateUserRequest.SerializeToString,
        response_deserializer=example__pb2.User.FromString,
        )
    self.CreatePhoto = channel.unary_unary(
        '/example.photoservice.ExamplePhotoService/CreatePhoto',
        request_serializer=example__pb2.CreatePhotoRequest.SerializeToString,
        response_deserializer=example__pb2.Photo.FromString,
        )
    self.ListPhotos = channel.unary_unary(
        '/example.photoservice.ExamplePhotoService/ListPhotos',
        request_serializer=example__pb2.ListPhotosRequest.SerializeToString,
        response_deserializer=example__pb2.ListPhotosResponse.FromString,
        )
    self.GetPhoto = channel.unary_unary(
        '/example.photoservice.ExamplePhotoService/GetPhoto',
        request_serializer=example__pb2.GetPhotoRequest.SerializeToString,
        response_deserializer=example__pb2.Photo.FromString,
        )
    self.DeletePhoto = channel.unary_unary(
        '/example.photoservice.ExamplePhotoService/DeletePhoto',
        request_serializer=example__pb2.DeletePhotoRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UploadPhoto = channel.stream_unary(
        '/example.photoservice.ExamplePhotoService/UploadPhoto',
        request_serializer=example__pb2.PhotoDataBlock.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StreamPhotos = channel.stream_stream(
        '/example.photoservice.ExamplePhotoService/StreamPhotos',
        request_serializer=example__pb2.GetPhotoRequest.SerializeToString,
        response_deserializer=example__pb2.Photo.FromString,
        )


class ExamplePhotoServiceServicer(object):
  """Service definitions
  """

  def CreateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreatePhoto(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPhotos(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPhoto(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePhoto(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadPhoto(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamPhotos(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExamplePhotoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=example__pb2.User.FromString,
          response_serializer=example__pb2.User.SerializeToString,
      ),
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=example__pb2.GetUserRequest.FromString,
          response_serializer=example__pb2.User.SerializeToString,
      ),
      'UpdateUser': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateUser,
          request_deserializer=example__pb2.UpdateUserRequest.FromString,
          response_serializer=example__pb2.User.SerializeToString,
      ),
      'CreatePhoto': grpc.unary_unary_rpc_method_handler(
          servicer.CreatePhoto,
          request_deserializer=example__pb2.CreatePhotoRequest.FromString,
          response_serializer=example__pb2.Photo.SerializeToString,
      ),
      'ListPhotos': grpc.unary_unary_rpc_method_handler(
          servicer.ListPhotos,
          request_deserializer=example__pb2.ListPhotosRequest.FromString,
          response_serializer=example__pb2.ListPhotosResponse.SerializeToString,
      ),
      'GetPhoto': grpc.unary_unary_rpc_method_handler(
          servicer.GetPhoto,
          request_deserializer=example__pb2.GetPhotoRequest.FromString,
          response_serializer=example__pb2.Photo.SerializeToString,
      ),
      'DeletePhoto': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePhoto,
          request_deserializer=example__pb2.DeletePhotoRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UploadPhoto': grpc.stream_unary_rpc_method_handler(
          servicer.UploadPhoto,
          request_deserializer=example__pb2.PhotoDataBlock.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StreamPhotos': grpc.stream_stream_rpc_method_handler(
          servicer.StreamPhotos,
          request_deserializer=example__pb2.GetPhotoRequest.FromString,
          response_serializer=example__pb2.Photo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'example.photoservice.ExamplePhotoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
