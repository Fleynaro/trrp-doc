# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dispatcher.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64ispatcher.proto\x12\x03\x64oc\"\x12\n\x10\x44ocumentsRequest\"4\n\x14\x44ocumentInfoResponse\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\"!\n\x10\x44ocServerRequest\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\"/\n\x11\x44ocServerResponse\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x32\x9a\x01\n\x11\x44ispatcherService\x12\x44\n\x0cGetDocuments\x12\x15.doc.DocumentsRequest\x1a\x19.doc.DocumentInfoResponse\"\x00\x30\x01\x12?\n\x0cGetDocServer\x12\x15.doc.DocServerRequest\x1a\x16.doc.DocServerResponse\"\x00\x62\x06proto3')



_DOCUMENTSREQUEST = DESCRIPTOR.message_types_by_name['DocumentsRequest']
_DOCUMENTINFORESPONSE = DESCRIPTOR.message_types_by_name['DocumentInfoResponse']
_DOCSERVERREQUEST = DESCRIPTOR.message_types_by_name['DocServerRequest']
_DOCSERVERRESPONSE = DESCRIPTOR.message_types_by_name['DocServerResponse']
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

_DISPATCHERSERVICE = DESCRIPTOR.services_by_name['DispatcherService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DOCUMENTSREQUEST._serialized_start=25
  _DOCUMENTSREQUEST._serialized_end=43
  _DOCUMENTINFORESPONSE._serialized_start=45
  _DOCUMENTINFORESPONSE._serialized_end=97
  _DOCSERVERREQUEST._serialized_start=99
  _DOCSERVERREQUEST._serialized_end=132
  _DOCSERVERRESPONSE._serialized_start=134
  _DOCSERVERRESPONSE._serialized_end=181
  _DISPATCHERSERVICE._serialized_start=184
  _DISPATCHERSERVICE._serialized_end=338
# @@protoc_insertion_point(module_scope)
