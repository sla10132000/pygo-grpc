# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='hello',
  syntax='proto3',
  serialized_options=b'Z\001/',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bhello.proto\x12\x05hello\"\x1c\n\tMsgStruct\x12\x0f\n\x07message\x18\x01 \x01(\t28\n\x05Hello\x12/\n\x07PushMsg\x12\x10.hello.MsgStruct\x1a\x10.hello.MsgStruct\"\x00\x42\x03Z\x01/b\x06proto3'
)




_MSGSTRUCT = _descriptor.Descriptor(
  name='MsgStruct',
  full_name='hello.MsgStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='hello.MsgStruct.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=22,
  serialized_end=50,
)

DESCRIPTOR.message_types_by_name['MsgStruct'] = _MSGSTRUCT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgStruct = _reflection.GeneratedProtocolMessageType('MsgStruct', (_message.Message,), {
  'DESCRIPTOR' : _MSGSTRUCT,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.MsgStruct)
  })
_sym_db.RegisterMessage(MsgStruct)


DESCRIPTOR._options = None

_HELLO = _descriptor.ServiceDescriptor(
  name='Hello',
  full_name='hello.Hello',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=52,
  serialized_end=108,
  methods=[
  _descriptor.MethodDescriptor(
    name='PushMsg',
    full_name='hello.Hello.PushMsg',
    index=0,
    containing_service=None,
    input_type=_MSGSTRUCT,
    output_type=_MSGSTRUCT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLO)

DESCRIPTOR.services_by_name['Hello'] = _HELLO

# @@protoc_insertion_point(module_scope)
