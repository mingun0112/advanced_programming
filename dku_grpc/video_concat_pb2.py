# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: video_concat.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'video_concat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12video_concat.proto\"5\n\x0c\x46rameRequest\x12\x12\n\nframe_data\x18\x01 \x01(\x0c\x12\x11\n\tclient_id\x18\x02 \x01(\t\"#\n\rFrameResponse\x12\x12\n\nframe_data\x18\x01 \x01(\x0c\x32K\n\x16VideoProcessingService\x12\x31\n\x0cStreamFrames\x12\r.FrameRequest\x1a\x0e.FrameResponse(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'video_concat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FRAMEREQUEST']._serialized_start=22
  _globals['_FRAMEREQUEST']._serialized_end=75
  _globals['_FRAMERESPONSE']._serialized_start=77
  _globals['_FRAMERESPONSE']._serialized_end=112
  _globals['_VIDEOPROCESSINGSERVICE']._serialized_start=114
  _globals['_VIDEOPROCESSINGSERVICE']._serialized_end=189
# @@protoc_insertion_point(module_scope)
