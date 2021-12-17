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
  serialized_pb=b'\n\x10\x64ispatcher.proto\x12\x03\x64oc\"\x12\n\x10\x44ocumentsRequest\"4\n\x14\x44ocumentInfoResponse\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\"!\n\x10\x44ocServerRequest\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\"/\n\x11\x44ocServerResponse\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x32\x9a\x01\n\x11\x44ispatcherService\x12\x44\n\x0cGetDocuments\x12\x15.doc.DocumentsRequest\x1a\x19.doc.DocumentInfoResponse\"\x00\x30\x01\x12?\n\x0cGetDocServer\x12\x15.doc.DocServerRequest\x1a\x16.doc.DocServerResponse\"\x00\x62\x06proto3'
)




_DOCUMENTSREQUEST = _descriptor.Descriptor(
  name='DocumentsRequest',
  full_name='doc.DocumentsRequest',
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
  serialized_start=25,
  serialized_end=43,
)


_DOCUMENTINFORESPONSE = _descriptor.Descriptor(
  name='DocumentInfoResponse',
  full_name='doc.DocumentInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docId', full_name='doc.DocumentInfoResponse.docId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='doc.DocumentInfoResponse.title', index=1,
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
  serialized_start=45,
  serialized_end=97,
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
  serialized_start=99,
  serialized_end=132,
)


_DOCSERVERRESPONSE = _descriptor.Descriptor(
  name='DocServerResponse',
  full_name='doc.DocServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='doc.DocServerResponse.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='doc.DocServerResponse.port', index=1,
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
  serialized_start=134,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['DocumentsRequest'] = _DOCUMENTSREQUEST
DESCRIPTOR.message_types_by_name['DocumentInfoResponse'] = _DOCUMENTINFORESPONSE
DESCRIPTOR.message_types_by_name['DocServerRequest'] = _DOCSERVERREQUEST
DESCRIPTOR.message_types_by_name['DocServerResponse'] = _DOCSERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DocumentsRequest = _reflection.GeneratedProtocolMessageType('DocumentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTSREQUEST,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocumentsRequest)
  })
_sym_db.RegisterMessage(DocumentsRequest)

DocumentInfoResponse = _reflection.GeneratedProtocolMessageType('DocumentInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTINFORESPONSE,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocumentInfoResponse)
  })
_sym_db.RegisterMessage(DocumentInfoResponse)

DocServerRequest = _reflection.GeneratedProtocolMessageType('DocServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOCSERVERREQUEST,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocServerRequest)
  })
_sym_db.RegisterMessage(DocServerRequest)

DocServerResponse = _reflection.GeneratedProtocolMessageType('DocServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOCSERVERRESPONSE,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocServerResponse)
  })
_sym_db.RegisterMessage(DocServerResponse)



_DISPATCHERSERVICE = _descriptor.ServiceDescriptor(
  name='DispatcherService',
  full_name='doc.DispatcherService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=184,
  serialized_end=338,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDocuments',
    full_name='doc.DispatcherService.GetDocuments',
    index=0,
    containing_service=None,
    input_type=_DOCUMENTSREQUEST,
    output_type=_DOCUMENTINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDocServer',
    full_name='doc.DispatcherService.GetDocServer',
    index=1,
    containing_service=None,
    input_type=_DOCSERVERREQUEST,
    output_type=_DOCSERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISPATCHERSERVICE)

DESCRIPTOR.services_by_name['DispatcherService'] = _DISPATCHERSERVICE

# @@protoc_insertion_point(module_scope)
