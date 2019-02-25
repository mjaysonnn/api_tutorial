# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='example.photoservice',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rexample.proto\x12\x14\x65xample.photoservice\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/protobuf/field_mask.proto\"9\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"[\n\x05Photo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1e\n\x0eGetUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"u\n\x11UpdateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x04user\x18\x02 \x01(\x0b\x32\x1a.example.photoservice.User\x12(\n\x04mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"P\n\x12\x43reatePhotoRequest\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12*\n\x05photo\x18\x03 \x01(\x0b\x32\x1b.example.photoservice.Photo\"\xb4\x01\n\x11ListPhotosRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x41\n\x08order_by\x18\x02 \x01(\x0e\x32/.example.photoservice.ListPhotosRequest.OrderBy\x12\x12\n\npage_token\x18\x03 \x01(\t\"8\n\x07OrderBy\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x10\n\x0c\x44ISPLAY_NAME\x10\x01\x12\x0e\n\nCREATED_AT\x10\x02\"Z\n\x12ListPhotosResponse\x12+\n\x06photos\x18\x01 \x03(\x0b\x32\x1b.example.photoservice.Photo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x1f\n\x0fGetPhotoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\"\n\x12\x44\x65letePhotoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"^\n\x0ePhotoDataBlock\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ndata_block\x18\x03 \x01(\x0c\x12\x17\n\x0f\x64\x61ta_block_hash\x18\x04 \x01(\t\x12\x11\n\tdata_hash\x18\x05 \x01(\t2\xfa\x05\n\x13\x45xamplePhotoService\x12\x44\n\nCreateUser\x12\x1a.example.photoservice.User\x1a\x1a.example.photoservice.User\x12K\n\x07GetUser\x12$.example.photoservice.GetUserRequest\x1a\x1a.example.photoservice.User\x12Q\n\nUpdateUser\x12\'.example.photoservice.UpdateUserRequest\x1a\x1a.example.photoservice.User\x12T\n\x0b\x43reatePhoto\x12(.example.photoservice.CreatePhotoRequest\x1a\x1b.example.photoservice.Photo\x12_\n\nListPhotos\x12\'.example.photoservice.ListPhotosRequest\x1a(.example.photoservice.ListPhotosResponse\x12N\n\x08GetPhoto\x12%.example.photoservice.GetPhotoRequest\x1a\x1b.example.photoservice.Photo\x12O\n\x0b\x44\x65letePhoto\x12(.example.photoservice.DeletePhotoRequest\x1a\x16.google.protobuf.Empty\x12M\n\x0bUploadPhoto\x12$.example.photoservice.PhotoDataBlock\x1a\x16.google.protobuf.Empty(\x01\x12V\n\x0cStreamPhotos\x12%.example.photoservice.GetPhotoRequest\x1a\x1b.example.photoservice.Photo(\x01\x30\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])



_LISTPHOTOSREQUEST_ORDERBY = _descriptor.EnumDescriptor(
  name='OrderBy',
  full_name='example.photoservice.ListPhotosRequest.OrderBy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_NAME', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATED_AT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=645,
  serialized_end=701,
)
_sym_db.RegisterEnumDescriptor(_LISTPHOTOSREQUEST_ORDERBY)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='example.photoservice.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.photoservice.User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='example.photoservice.User.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='example.photoservice.User.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=192,
)


_PHOTO = _descriptor.Descriptor(
  name='Photo',
  full_name='example.photoservice.Photo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.photoservice.Photo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='example.photoservice.Photo.display_name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='example.photoservice.Photo.created_at', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=285,
)


_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='example.photoservice.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.photoservice.GetUserRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=317,
)


_UPDATEUSERREQUEST = _descriptor.Descriptor(
  name='UpdateUserRequest',
  full_name='example.photoservice.UpdateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.photoservice.UpdateUserRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='example.photoservice.UpdateUserRequest.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask', full_name='example.photoservice.UpdateUserRequest.mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=436,
)


_CREATEPHOTOREQUEST = _descriptor.Descriptor(
  name='CreatePhotoRequest',
  full_name='example.photoservice.CreatePhotoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='example.photoservice.CreatePhotoRequest.parent', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='photo', full_name='example.photoservice.CreatePhotoRequest.photo', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=518,
)


_LISTPHOTOSREQUEST = _descriptor.Descriptor(
  name='ListPhotosRequest',
  full_name='example.photoservice.ListPhotosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='example.photoservice.ListPhotosRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='example.photoservice.ListPhotosRequest.order_by', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='example.photoservice.ListPhotosRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTPHOTOSREQUEST_ORDERBY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=701,
)


_LISTPHOTOSRESPONSE = _descriptor.Descriptor(
  name='ListPhotosResponse',
  full_name='example.photoservice.ListPhotosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photos', full_name='example.photoservice.ListPhotosResponse.photos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='example.photoservice.ListPhotosResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=703,
  serialized_end=793,
)


_GETPHOTOREQUEST = _descriptor.Descriptor(
  name='GetPhotoRequest',
  full_name='example.photoservice.GetPhotoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.photoservice.GetPhotoRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=795,
  serialized_end=826,
)


_DELETEPHOTOREQUEST = _descriptor.Descriptor(
  name='DeletePhotoRequest',
  full_name='example.photoservice.DeletePhotoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.photoservice.DeletePhotoRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=828,
  serialized_end=862,
)


_PHOTODATABLOCK = _descriptor.Descriptor(
  name='PhotoDataBlock',
  full_name='example.photoservice.PhotoDataBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.photoservice.PhotoDataBlock.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_block', full_name='example.photoservice.PhotoDataBlock.data_block', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_block_hash', full_name='example.photoservice.PhotoDataBlock.data_block_hash', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_hash', full_name='example.photoservice.PhotoDataBlock.data_hash', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=864,
  serialized_end=958,
)

_PHOTO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATEUSERREQUEST.fields_by_name['user'].message_type = _USER
_UPDATEUSERREQUEST.fields_by_name['mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CREATEPHOTOREQUEST.fields_by_name['photo'].message_type = _PHOTO
_LISTPHOTOSREQUEST.fields_by_name['order_by'].enum_type = _LISTPHOTOSREQUEST_ORDERBY
_LISTPHOTOSREQUEST_ORDERBY.containing_type = _LISTPHOTOSREQUEST
_LISTPHOTOSRESPONSE.fields_by_name['photos'].message_type = _PHOTO
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Photo'] = _PHOTO
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['UpdateUserRequest'] = _UPDATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreatePhotoRequest'] = _CREATEPHOTOREQUEST
DESCRIPTOR.message_types_by_name['ListPhotosRequest'] = _LISTPHOTOSREQUEST
DESCRIPTOR.message_types_by_name['ListPhotosResponse'] = _LISTPHOTOSRESPONSE
DESCRIPTOR.message_types_by_name['GetPhotoRequest'] = _GETPHOTOREQUEST
DESCRIPTOR.message_types_by_name['DeletePhotoRequest'] = _DELETEPHOTOREQUEST
DESCRIPTOR.message_types_by_name['PhotoDataBlock'] = _PHOTODATABLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.User)
  ))
_sym_db.RegisterMessage(User)

Photo = _reflection.GeneratedProtocolMessageType('Photo', (_message.Message,), dict(
  DESCRIPTOR = _PHOTO,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.Photo)
  ))
_sym_db.RegisterMessage(Photo)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERREQUEST,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.GetUserRequest)
  ))
_sym_db.RegisterMessage(GetUserRequest)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERREQUEST,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.UpdateUserRequest)
  ))
_sym_db.RegisterMessage(UpdateUserRequest)

CreatePhotoRequest = _reflection.GeneratedProtocolMessageType('CreatePhotoRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEPHOTOREQUEST,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.CreatePhotoRequest)
  ))
_sym_db.RegisterMessage(CreatePhotoRequest)

ListPhotosRequest = _reflection.GeneratedProtocolMessageType('ListPhotosRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPHOTOSREQUEST,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.ListPhotosRequest)
  ))
_sym_db.RegisterMessage(ListPhotosRequest)

ListPhotosResponse = _reflection.GeneratedProtocolMessageType('ListPhotosResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPHOTOSRESPONSE,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.ListPhotosResponse)
  ))
_sym_db.RegisterMessage(ListPhotosResponse)

GetPhotoRequest = _reflection.GeneratedProtocolMessageType('GetPhotoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPHOTOREQUEST,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.GetPhotoRequest)
  ))
_sym_db.RegisterMessage(GetPhotoRequest)

DeletePhotoRequest = _reflection.GeneratedProtocolMessageType('DeletePhotoRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEPHOTOREQUEST,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.DeletePhotoRequest)
  ))
_sym_db.RegisterMessage(DeletePhotoRequest)

PhotoDataBlock = _reflection.GeneratedProtocolMessageType('PhotoDataBlock', (_message.Message,), dict(
  DESCRIPTOR = _PHOTODATABLOCK,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.photoservice.PhotoDataBlock)
  ))
_sym_db.RegisterMessage(PhotoDataBlock)



_EXAMPLEPHOTOSERVICE = _descriptor.ServiceDescriptor(
  name='ExamplePhotoService',
  full_name='example.photoservice.ExamplePhotoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=961,
  serialized_end=1723,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='example.photoservice.ExamplePhotoService.CreateUser',
    index=0,
    containing_service=None,
    input_type=_USER,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='example.photoservice.ExamplePhotoService.GetUser',
    index=1,
    containing_service=None,
    input_type=_GETUSERREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateUser',
    full_name='example.photoservice.ExamplePhotoService.UpdateUser',
    index=2,
    containing_service=None,
    input_type=_UPDATEUSERREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreatePhoto',
    full_name='example.photoservice.ExamplePhotoService.CreatePhoto',
    index=3,
    containing_service=None,
    input_type=_CREATEPHOTOREQUEST,
    output_type=_PHOTO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListPhotos',
    full_name='example.photoservice.ExamplePhotoService.ListPhotos',
    index=4,
    containing_service=None,
    input_type=_LISTPHOTOSREQUEST,
    output_type=_LISTPHOTOSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPhoto',
    full_name='example.photoservice.ExamplePhotoService.GetPhoto',
    index=5,
    containing_service=None,
    input_type=_GETPHOTOREQUEST,
    output_type=_PHOTO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeletePhoto',
    full_name='example.photoservice.ExamplePhotoService.DeletePhoto',
    index=6,
    containing_service=None,
    input_type=_DELETEPHOTOREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UploadPhoto',
    full_name='example.photoservice.ExamplePhotoService.UploadPhoto',
    index=7,
    containing_service=None,
    input_type=_PHOTODATABLOCK,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamPhotos',
    full_name='example.photoservice.ExamplePhotoService.StreamPhotos',
    index=8,
    containing_service=None,
    input_type=_GETPHOTOREQUEST,
    output_type=_PHOTO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXAMPLEPHOTOSERVICE)

DESCRIPTOR.services_by_name['ExamplePhotoService'] = _EXAMPLEPHOTOSERVICE

# @@protoc_insertion_point(module_scope)
