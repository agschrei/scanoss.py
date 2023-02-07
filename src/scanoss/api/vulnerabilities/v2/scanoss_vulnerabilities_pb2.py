# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scanoss/api/vulnerabilities/v2/scanoss-vulnerabilities.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from scanoss.api.common.v2 import scanoss_common_pb2 as scanoss_dot_api_dot_common_dot_v2_dot_scanoss__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<scanoss/api/vulnerabilities/v2/scanoss-vulnerabilities.proto\x12\x1escanoss.api.vulnerabilities.v2\x1a*scanoss/api/common/v2/scanoss-common.proto\"\x8d\x01\n\x14VulnerabilityRequest\x12I\n\x05purls\x18\x01 \x03(\x0b\x32:.scanoss.api.vulnerabilities.v2.VulnerabilityRequest.Purls\x1a*\n\x05Purls\x12\x0c\n\x04purl\x18\x01 \x01(\t\x12\x13\n\x0brequirement\x18\x02 \x01(\t\"\xab\x01\n\x0b\x43peResponse\x12@\n\x05purls\x18\x01 \x03(\x0b\x32\x31.scanoss.api.vulnerabilities.v2.CpeResponse.Purls\x12\x35\n\x06status\x18\x02 \x01(\x0b\x32%.scanoss.api.common.v2.StatusResponse\x1a#\n\x05Purls\x12\x0c\n\x04purl\x18\x01 \x01(\t\x12\x0c\n\x04\x63pes\x18\x02 \x03(\t\"\xa3\x03\n\x15VulnerabilityResponse\x12J\n\x05purls\x18\x01 \x03(\x0b\x32;.scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Purls\x12\x35\n\x06status\x18\x02 \x01(\x0b\x32%.scanoss.api.common.v2.StatusResponse\x1a\x8f\x01\n\x0fVulnerabilities\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03\x63ve\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0f\n\x07summary\x18\x04 \x01(\t\x12\x10\n\x08severity\x18\x05 \x01(\t\x12\x11\n\tpublished\x18\x06 \x01(\t\x12\x10\n\x08modified\x18\x07 \x01(\t\x12\x0e\n\x06source\x18\x08 \x01(\t\x1au\n\x05Purls\x12\x0c\n\x04purl\x18\x01 \x01(\t\x12^\n\x0fvulnerabilities\x18\x02 \x03(\x0b\x32\x45.scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities2\xd4\x02\n\x0fVulnerabilities\x12O\n\x04\x45\x63ho\x12\".scanoss.api.common.v2.EchoRequest\x1a#.scanoss.api.common.v2.EchoResponse\x12l\n\x07GetCpes\x12\x34.scanoss.api.vulnerabilities.v2.VulnerabilityRequest\x1a+.scanoss.api.vulnerabilities.v2.CpeResponse\x12\x81\x01\n\x12GetVulnerabilities\x12\x34.scanoss.api.vulnerabilities.v2.VulnerabilityRequest\x1a\x35.scanoss.api.vulnerabilities.v2.VulnerabilityResponseBAZ?github.com/scanoss/papi/api/vulnerabilitiesv2;vulnerabilitiesv2b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'scanoss.api.vulnerabilities.v2.scanoss_vulnerabilities_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z?github.com/scanoss/papi/api/vulnerabilitiesv2;vulnerabilitiesv2'
  _VULNERABILITYREQUEST._serialized_start=141
  _VULNERABILITYREQUEST._serialized_end=282
  _VULNERABILITYREQUEST_PURLS._serialized_start=240
  _VULNERABILITYREQUEST_PURLS._serialized_end=282
  _CPERESPONSE._serialized_start=285
  _CPERESPONSE._serialized_end=456
  _CPERESPONSE_PURLS._serialized_start=421
  _CPERESPONSE_PURLS._serialized_end=456
  _VULNERABILITYRESPONSE._serialized_start=459
  _VULNERABILITYRESPONSE._serialized_end=878
  _VULNERABILITYRESPONSE_VULNERABILITIES._serialized_start=616
  _VULNERABILITYRESPONSE_VULNERABILITIES._serialized_end=759
  _VULNERABILITYRESPONSE_PURLS._serialized_start=761
  _VULNERABILITYRESPONSE_PURLS._serialized_end=878
  _VULNERABILITIES._serialized_start=881
  _VULNERABILITIES._serialized_end=1221
# @@protoc_insertion_point(module_scope)
