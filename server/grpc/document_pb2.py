# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: document.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='document.proto',
  package='doc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x64ocument.proto\x12\x03\x64oc\"E\n\x12\x41\x64\x64\x44ocumentRequest\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tsecretKey\x18\x03 \x01(\t\"\x15\n\x13\x41\x64\x64\x44ocumentResponse\"\'\n\x16\x44ocumentContentRequest\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\"8\n\x17\x44ocumentContentResponse\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\"\xf1\x01\n\x0f\x44ocumentChanges\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12,\n\x07\x63hanges\x18\x03 \x03(\x0b\x32\x1b.doc.DocumentChanges.Change\x1aR\n\x06\x43hange\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.doc.DocumentChanges.ChangeType\x12\x0b\n\x03pos\x18\x02 \x01(\x03\x12\x0c\n\x04text\x18\x03 \x01(\t\"<\n\nChangeType\x12\x16\n\x12\x43HANGE_TYPE_INSERT\x10\x00\x12\x16\n\x12\x43HANGE_TYPE_DELETE\x10\x01\"8\n\x16\x44ocumentChangesRequest\x12\r\n\x05\x64ocId\x18\x01 \x01(\x03\x12\x0f\n\x07version\x18\x02 \x01(\x05\"\x19\n\x17\x44ocumentChangesResponse2\xc6\x02\n\x0f\x44ocumentService\x12\x42\n\x0b\x41\x64\x64\x44ocument\x12\x17.doc.AddDocumentRequest\x1a\x18.doc.AddDocumentResponse\"\x00\x12W\n\x18GetActualDocumentContent\x12\x1b.doc.DocumentContentRequest\x1a\x1c.doc.DocumentContentResponse\"\x00\x12I\n\x12GetDocumentChanges\x12\x1b.doc.DocumentChangesRequest\x1a\x14.doc.DocumentChanges\"\x00\x12K\n\x13SendDocumentChanges\x12\x14.doc.DocumentChanges\x1a\x1c.doc.DocumentChangesResponse\"\x00\x62\x06proto3'
)



_DOCUMENTCHANGES_CHANGETYPE = _descriptor.EnumDescriptor(
  name='ChangeType',
  full_name='doc.DocumentChanges.ChangeType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHANGE_TYPE_INSERT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_TYPE_DELETE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=398,
  serialized_end=458,
)
_sym_db.RegisterEnumDescriptor(_DOCUMENTCHANGES_CHANGETYPE)


_ADDDOCUMENTREQUEST = _descriptor.Descriptor(
  name='AddDocumentRequest',
  full_name='doc.AddDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docId', full_name='doc.AddDocumentRequest.docId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='doc.AddDocumentRequest.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secretKey', full_name='doc.AddDocumentRequest.secretKey', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=23,
  serialized_end=92,
)


_ADDDOCUMENTRESPONSE = _descriptor.Descriptor(
  name='AddDocumentResponse',
  full_name='doc.AddDocumentResponse',
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
  serialized_start=94,
  serialized_end=115,
)


_DOCUMENTCONTENTREQUEST = _descriptor.Descriptor(
  name='DocumentContentRequest',
  full_name='doc.DocumentContentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docId', full_name='doc.DocumentContentRequest.docId', index=0,
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
  serialized_start=117,
  serialized_end=156,
)


_DOCUMENTCONTENTRESPONSE = _descriptor.Descriptor(
  name='DocumentContentResponse',
  full_name='doc.DocumentContentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='doc.DocumentContentResponse.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='doc.DocumentContentResponse.text', index=1,
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
  serialized_start=158,
  serialized_end=214,
)


_DOCUMENTCHANGES_CHANGE = _descriptor.Descriptor(
  name='Change',
  full_name='doc.DocumentChanges.Change',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='doc.DocumentChanges.Change.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos', full_name='doc.DocumentChanges.Change.pos', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='doc.DocumentChanges.Change.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=314,
  serialized_end=396,
)

_DOCUMENTCHANGES = _descriptor.Descriptor(
  name='DocumentChanges',
  full_name='doc.DocumentChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docId', full_name='doc.DocumentChanges.docId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='doc.DocumentChanges.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='changes', full_name='doc.DocumentChanges.changes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DOCUMENTCHANGES_CHANGE, ],
  enum_types=[
    _DOCUMENTCHANGES_CHANGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=458,
)


_DOCUMENTCHANGESREQUEST = _descriptor.Descriptor(
  name='DocumentChangesRequest',
  full_name='doc.DocumentChangesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docId', full_name='doc.DocumentChangesRequest.docId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='doc.DocumentChangesRequest.version', index=1,
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
  serialized_start=460,
  serialized_end=516,
)


_DOCUMENTCHANGESRESPONSE = _descriptor.Descriptor(
  name='DocumentChangesResponse',
  full_name='doc.DocumentChangesResponse',
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
  serialized_start=518,
  serialized_end=543,
)

_DOCUMENTCHANGES_CHANGE.fields_by_name['type'].enum_type = _DOCUMENTCHANGES_CHANGETYPE
_DOCUMENTCHANGES_CHANGE.containing_type = _DOCUMENTCHANGES
_DOCUMENTCHANGES.fields_by_name['changes'].message_type = _DOCUMENTCHANGES_CHANGE
_DOCUMENTCHANGES_CHANGETYPE.containing_type = _DOCUMENTCHANGES
DESCRIPTOR.message_types_by_name['AddDocumentRequest'] = _ADDDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['AddDocumentResponse'] = _ADDDOCUMENTRESPONSE
DESCRIPTOR.message_types_by_name['DocumentContentRequest'] = _DOCUMENTCONTENTREQUEST
DESCRIPTOR.message_types_by_name['DocumentContentResponse'] = _DOCUMENTCONTENTRESPONSE
DESCRIPTOR.message_types_by_name['DocumentChanges'] = _DOCUMENTCHANGES
DESCRIPTOR.message_types_by_name['DocumentChangesRequest'] = _DOCUMENTCHANGESREQUEST
DESCRIPTOR.message_types_by_name['DocumentChangesResponse'] = _DOCUMENTCHANGESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddDocumentRequest = _reflection.GeneratedProtocolMessageType('AddDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDDOCUMENTREQUEST,
  '__module__' : 'document_pb2'
  # @@protoc_insertion_point(class_scope:doc.AddDocumentRequest)
  })
_sym_db.RegisterMessage(AddDocumentRequest)

AddDocumentResponse = _reflection.GeneratedProtocolMessageType('AddDocumentResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDDOCUMENTRESPONSE,
  '__module__' : 'document_pb2'
  # @@protoc_insertion_point(class_scope:doc.AddDocumentResponse)
  })
_sym_db.RegisterMessage(AddDocumentResponse)

DocumentContentRequest = _reflection.GeneratedProtocolMessageType('DocumentContentRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTCONTENTREQUEST,
  '__module__' : 'document_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocumentContentRequest)
  })
_sym_db.RegisterMessage(DocumentContentRequest)

DocumentContentResponse = _reflection.GeneratedProtocolMessageType('DocumentContentResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTCONTENTRESPONSE,
  '__module__' : 'document_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocumentContentResponse)
  })
_sym_db.RegisterMessage(DocumentContentResponse)

DocumentChanges = _reflection.GeneratedProtocolMessageType('DocumentChanges', (_message.Message,), {

  'Change' : _reflection.GeneratedProtocolMessageType('Change', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENTCHANGES_CHANGE,
    '__module__' : 'document_pb2'
    # @@protoc_insertion_point(class_scope:doc.DocumentChanges.Change)
    })
  ,
  'DESCRIPTOR' : _DOCUMENTCHANGES,
  '__module__' : 'document_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocumentChanges)
  })
_sym_db.RegisterMessage(DocumentChanges)
_sym_db.RegisterMessage(DocumentChanges.Change)

DocumentChangesRequest = _reflection.GeneratedProtocolMessageType('DocumentChangesRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTCHANGESREQUEST,
  '__module__' : 'document_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocumentChangesRequest)
  })
_sym_db.RegisterMessage(DocumentChangesRequest)

DocumentChangesResponse = _reflection.GeneratedProtocolMessageType('DocumentChangesResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTCHANGESRESPONSE,
  '__module__' : 'document_pb2'
  # @@protoc_insertion_point(class_scope:doc.DocumentChangesResponse)
  })
_sym_db.RegisterMessage(DocumentChangesResponse)



_DOCUMENTSERVICE = _descriptor.ServiceDescriptor(
  name='DocumentService',
  full_name='doc.DocumentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=546,
  serialized_end=872,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddDocument',
    full_name='doc.DocumentService.AddDocument',
    index=0,
    containing_service=None,
    input_type=_ADDDOCUMENTREQUEST,
    output_type=_ADDDOCUMENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetActualDocumentContent',
    full_name='doc.DocumentService.GetActualDocumentContent',
    index=1,
    containing_service=None,
    input_type=_DOCUMENTCONTENTREQUEST,
    output_type=_DOCUMENTCONTENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDocumentChanges',
    full_name='doc.DocumentService.GetDocumentChanges',
    index=2,
    containing_service=None,
    input_type=_DOCUMENTCHANGESREQUEST,
    output_type=_DOCUMENTCHANGES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendDocumentChanges',
    full_name='doc.DocumentService.SendDocumentChanges',
    index=3,
    containing_service=None,
    input_type=_DOCUMENTCHANGES,
    output_type=_DOCUMENTCHANGESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DOCUMENTSERVICE)

DESCRIPTOR.services_by_name['DocumentService'] = _DOCUMENTSERVICE

# @@protoc_insertion_point(module_scope)
