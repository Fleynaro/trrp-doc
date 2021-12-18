# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dispatcher.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dispatcher.proto',
  package='doc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x64ispatcher.proto\x12\x03\x64oc\"!\n\x10\x44ocServerRequest\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\"\'\n\tDocServer\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"K\n\x13\x41\x64\x64\x44ocServerRequest\x12!\n\tdocServer\x18\x01 \x01(\x0b\x32\x0e.doc.DocServer\x12\x11\n\tsecretKey\x18\x02 \x01(\t\"\x16\n\x14\x41\x64\x64\x44ocServerResponse2\x93\x01\n\x11\x44ispatcherService\x12\x37\n\x0cGetDocServer\x12\x15.doc.DocServerRequest\x1a\x0e.doc.DocServer\"\x00\x12\x45\n\x0c\x41\x64\x64\x44ocServer\x12\x18.doc.AddDocServerRequest\x1a\x19.doc.AddDocServerResponse\"\x00\x62\x06proto3'
)




_DOCSERVERREQUEST = _descriptor.Descriptor(
  name='DocServerRequest',
  full_name='doc.DocServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docId', full_name='doc.DocServerRequest.docId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=25,
  serialized_end=58,
)


_DOCSERVER = _descriptor.Descriptor(
  name='DocServer',
  full_name='doc.DocServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='doc.DocServer.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='doc.DocServer.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=60,
  serialized_end=99,
)


_ADDDOCSERVERREQUEST = _descriptor.Descriptor(
  name='AddDocServerRequest',
  full_name='doc.AddDocServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docServer', full_name='doc.AddDocServerRequest.docServer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secretKey', full_name='doc.AddDocServerRequest.secretKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=101,
  serialized_end=176,
)


_ADDDOCSERVERRESPONSE = _descriptor.Descriptor(
  name='AddDocServerResponse',
  full_name='doc.AddDocServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=178,
  serialized_end=200,
)

_ADDDOCSERVERREQUEST.fields_by_name['docServer'].message_type = _DOCSERVER
DESCRIPTOR.message_types_by_name['DocServerRequest'] = _DOCSERVERREQUEST
DESCRIPTOR.message_types_by_name['DocServer'] = _DOCSERVER
DESCRIPTOR.message_types_by_name['AddDocServerRequest'] = _ADDDOCSERVERREQUEST
DESCRIPTOR.message_types_by_name['AddDocServerResponse'] = _ADDDOCSERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DocServerRequest = _reflection.GeneratedProtocolMessageType('DocServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOCSERVERREQUEST,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocServerRequest)
  })
_sym_db.RegisterMessage(DocServerRequest)

DocServer = _reflection.GeneratedProtocolMessageType('DocServer', (_message.Message,), {
  'DESCRIPTOR' : _DOCSERVER,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocServer)
  })
_sym_db.RegisterMessage(DocServer)

AddDocServerRequest = _reflection.GeneratedProtocolMessageType('AddDocServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDDOCSERVERREQUEST,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:doc.AddDocServerRequest)
  })
_sym_db.RegisterMessage(AddDocServerRequest)

AddDocServerResponse = _reflection.GeneratedProtocolMessageType('AddDocServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDDOCSERVERRESPONSE,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:doc.AddDocServerResponse)
  })
_sym_db.RegisterMessage(AddDocServerResponse)



_DISPATCHERSERVICE = _descriptor.ServiceDescriptor(
  name='DispatcherService',
  full_name='doc.DispatcherService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=203,
  serialized_end=350,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDocServer',
    full_name='doc.DispatcherService.GetDocServer',
    index=0,
    containing_service=None,
    input_type=_DOCSERVERREQUEST,
    output_type=_DOCSERVER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddDocServer',
    full_name='doc.DispatcherService.AddDocServer',
    index=1,
    containing_service=None,
    input_type=_ADDDOCSERVERREQUEST,
    output_type=_ADDDOCSERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISPATCHERSERVICE)

DESCRIPTOR.services_by_name['DispatcherService'] = _DISPATCHERSERVICE

# @@protoc_insertion_point(module_scope)
