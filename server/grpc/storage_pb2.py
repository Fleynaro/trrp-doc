# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import document_content_pb2 as document__content__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='storage.proto',
  package='doc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rstorage.proto\x12\x03\x64oc\x1a\x16\x64ocument_content.proto\"\x12\n\x10\x44ocumentsRequest\"y\n\x11\x44ocumentsResponse\x12\x36\n\tdocuments\x18\x01 \x03(\x0b\x32#.doc.DocumentsResponse.DocumentInfo\x1a,\n\x0c\x44ocumentInfo\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t2\xa4\x01\n\x0eStorageService\x12?\n\x0cGetDocuments\x12\x15.doc.DocumentsRequest\x1a\x16.doc.DocumentsResponse\"\x00\x12Q\n\x12GetDocumentContent\x12\x1b.doc.DocumentContentRequest\x1a\x1c.doc.DocumentContentResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[document__content__pb2.DESCRIPTOR,])




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
  serialized_start=46,
  serialized_end=64,
)


_DOCUMENTSRESPONSE_DOCUMENTINFO = _descriptor.Descriptor(
  name='DocumentInfo',
  full_name='doc.DocumentsResponse.DocumentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docId', full_name='doc.DocumentsResponse.DocumentInfo.docId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='doc.DocumentsResponse.DocumentInfo.title', index=1,
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
  serialized_start=143,
  serialized_end=187,
)

_DOCUMENTSRESPONSE = _descriptor.Descriptor(
  name='DocumentsResponse',
  full_name='doc.DocumentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='documents', full_name='doc.DocumentsResponse.documents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DOCUMENTSRESPONSE_DOCUMENTINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=187,
)

_DOCUMENTSRESPONSE_DOCUMENTINFO.containing_type = _DOCUMENTSRESPONSE
_DOCUMENTSRESPONSE.fields_by_name['documents'].message_type = _DOCUMENTSRESPONSE_DOCUMENTINFO
DESCRIPTOR.message_types_by_name['DocumentsRequest'] = _DOCUMENTSREQUEST
DESCRIPTOR.message_types_by_name['DocumentsResponse'] = _DOCUMENTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DocumentsRequest = _reflection.GeneratedProtocolMessageType('DocumentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTSREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocumentsRequest)
  })
_sym_db.RegisterMessage(DocumentsRequest)

DocumentsResponse = _reflection.GeneratedProtocolMessageType('DocumentsResponse', (_message.Message,), {

  'DocumentInfo' : _reflection.GeneratedProtocolMessageType('DocumentInfo', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENTSRESPONSE_DOCUMENTINFO,
    '__module__' : 'storage_pb2'
    # @@protoc_insertion_point(class_scope:doc.DocumentsResponse.DocumentInfo)
    })
  ,
  'DESCRIPTOR' : _DOCUMENTSRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocumentsResponse)
  })
_sym_db.RegisterMessage(DocumentsResponse)
_sym_db.RegisterMessage(DocumentsResponse.DocumentInfo)



_STORAGESERVICE = _descriptor.ServiceDescriptor(
  name='StorageService',
  full_name='doc.StorageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=190,
  serialized_end=354,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDocuments',
    full_name='doc.StorageService.GetDocuments',
    index=0,
    containing_service=None,
    input_type=_DOCUMENTSREQUEST,
    output_type=_DOCUMENTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDocumentContent',
    full_name='doc.StorageService.GetDocumentContent',
    index=1,
    containing_service=None,
    input_type=document__content__pb2._DOCUMENTCONTENTREQUEST,
    output_type=document__content__pb2._DOCUMENTCONTENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STORAGESERVICE)

DESCRIPTOR.services_by_name['StorageService'] = _STORAGESERVICE

# @@protoc_insertion_point(module_scope)
