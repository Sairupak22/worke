# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\nuser.proto\x12\nuser_proto"\x14\n\x06UserId\x12\n\n\x02id\x18\x01 \x01(\t"\xae\x01\n\x08UserInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x66name\x18\x02 \x01(\t\x12\r\n\x05lname\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\r\n\x05\x63\x63ode\x18\x05 \x01(\t\x12\x14\n\x0cphone_number\x18\x06 \x01(\t\x12\x10\n\x08username\x18\x07 \x01(\t\x12\r\n\x05image\x18\x08 \x01(\t\x12\r\n\x05utype\x18\t \x01(\t\x12\x14\n\x0corganisation\x18\n \x01(\t"?\n\x13UserPermissionCheck\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06method\x18\x03 \x01(\t"\x1f\n\x0b\x42ooleanData\x12\x10\n\x08verified\x18\x01 \x01(\x08\x32\x94\x01\n\x08UserData\x12\x35\n\x07GetUser\x12\x12.user_proto.UserId\x1a\x14.user_proto.UserInfo"\x00\x12Q\n\x13\x43heckUserPermission\x12\x1f.user_proto.UserPermissionCheck\x1a\x17.user_proto.BooleanData"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "user_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _USERID._serialized_start = 26
    _USERID._serialized_end = 46
    _USERINFO._serialized_start = 49
    _USERINFO._serialized_end = 223
    _USERPERMISSIONCHECK._serialized_start = 225
    _USERPERMISSIONCHECK._serialized_end = 288
    _BOOLEANDATA._serialized_start = 290
    _BOOLEANDATA._serialized_end = 321
    _USERDATA._serialized_start = 324
    _USERDATA._serialized_end = 472
# @@protoc_insertion_point(module_scope)