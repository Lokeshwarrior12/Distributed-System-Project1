# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x05image\"#\n\x0cImageRequest\x12\x13\n\x0bobject_name\x18\x01 \x01(\t\"#\n\rImageResponse\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x32K\n\x0cImageService\x12;\n\x0eGetRandomImage\x12\x13.image.ImageRequest\x1a\x14.image.ImageResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_IMAGEREQUEST']._serialized_start=23
  _globals['_IMAGEREQUEST']._serialized_end=58
  _globals['_IMAGERESPONSE']._serialized_start=60
  _globals['_IMAGERESPONSE']._serialized_end=95
  _globals['_IMAGESERVICE']._serialized_start=97
  _globals['_IMAGESERVICE']._serialized_end=172
# @@protoc_insertion_point(module_scope)
