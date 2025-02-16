# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: countries.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='countries.proto',
  package='countries',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63ountries.proto\x12\tcountries\"\x1e\n\x0e\x43ountryRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"8\n\nCurrencies\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\"\xaa\x01\n\x0f\x43ountryResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nalpha2Code\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61pital\x18\x03 \x01(\t\x12\x11\n\tsubregion\x18\x04 \x01(\t\x12\x12\n\npopulation\x18\x05 \x01(\x05\x12\x12\n\nnativeName\x18\x06 \x01(\t\x12)\n\ncurrencies\x18\x07 \x03(\x0b\x32\x15.countries.Currencies2L\n\x07\x43ountry\x12\x41\n\x06search\x12\x19.countries.CountryRequest\x1a\x1a.countries.CountryResponse\"\x00\x62\x06proto3'
)




_COUNTRYREQUEST = _descriptor.Descriptor(
  name='CountryRequest',
  full_name='countries.CountryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='countries.CountryRequest.name', index=0,
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
  serialized_start=30,
  serialized_end=60,
)


_CURRENCIES = _descriptor.Descriptor(
  name='Currencies',
  full_name='countries.Currencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='countries.Currencies.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='countries.Currencies.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='countries.Currencies.symbol', index=2,
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
  serialized_start=62,
  serialized_end=118,
)


_COUNTRYRESPONSE = _descriptor.Descriptor(
  name='CountryResponse',
  full_name='countries.CountryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='countries.CountryResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alpha2Code', full_name='countries.CountryResponse.alpha2Code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='capital', full_name='countries.CountryResponse.capital', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subregion', full_name='countries.CountryResponse.subregion', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='population', full_name='countries.CountryResponse.population', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nativeName', full_name='countries.CountryResponse.nativeName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currencies', full_name='countries.CountryResponse.currencies', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=121,
  serialized_end=291,
)

_COUNTRYRESPONSE.fields_by_name['currencies'].message_type = _CURRENCIES
DESCRIPTOR.message_types_by_name['CountryRequest'] = _COUNTRYREQUEST
DESCRIPTOR.message_types_by_name['Currencies'] = _CURRENCIES
DESCRIPTOR.message_types_by_name['CountryResponse'] = _COUNTRYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CountryRequest = _reflection.GeneratedProtocolMessageType('CountryRequest', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYREQUEST,
  '__module__' : 'countries_pb2'
  # @@protoc_insertion_point(class_scope:countries.CountryRequest)
  })
_sym_db.RegisterMessage(CountryRequest)

Currencies = _reflection.GeneratedProtocolMessageType('Currencies', (_message.Message,), {
  'DESCRIPTOR' : _CURRENCIES,
  '__module__' : 'countries_pb2'
  # @@protoc_insertion_point(class_scope:countries.Currencies)
  })
_sym_db.RegisterMessage(Currencies)

CountryResponse = _reflection.GeneratedProtocolMessageType('CountryResponse', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYRESPONSE,
  '__module__' : 'countries_pb2'
  # @@protoc_insertion_point(class_scope:countries.CountryResponse)
  })
_sym_db.RegisterMessage(CountryResponse)



_COUNTRY = _descriptor.ServiceDescriptor(
  name='Country',
  full_name='countries.Country',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=293,
  serialized_end=369,
  methods=[
  _descriptor.MethodDescriptor(
    name='search',
    full_name='countries.Country.search',
    index=0,
    containing_service=None,
    input_type=_COUNTRYREQUEST,
    output_type=_COUNTRYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COUNTRY)

DESCRIPTOR.services_by_name['Country'] = _COUNTRY

# @@protoc_insertion_point(module_scope)
