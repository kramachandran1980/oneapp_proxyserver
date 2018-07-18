# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device_state_events.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import device_state_structures_pb2 as device__state__structures__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='device_state_events.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x64\x65vice_state_events.proto\x1a\x0c\x63ommon.proto\x1a\x1d\x64\x65vice_state_structures.proto\"1\n\x15\x43lientConnectionEvent\x12\x18\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x07.Device\"/\n\x14\x44\x65viceConnectedEvent\x12\x17\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x07.Device\".\n\x17\x44\x65viceDisconnectedEvent\x12\x13\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\t\">\n\x10\x44\x65viceErrorEvent\x12\x13\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\t\x12\x15\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x06.Error\"\xf3\x01\n\x0b\x44\x65viceEvent\x12\x32\n\x10\x63onnection_event\x18\x01 \x01(\x0b\x32\x16.ClientConnectionEventH\x00\x12\x37\n\x16\x64\x65vice_connected_event\x18\x02 \x01(\x0b\x32\x15.DeviceConnectedEventH\x00\x12=\n\x19\x64\x65vice_disconnected_event\x18\x03 \x01(\x0b\x32\x18.DeviceDisconnectedEventH\x00\x12/\n\x12\x64\x65vice_error_event\x18\x04 \x01(\x0b\x32\x11.DeviceErrorEventH\x00\x42\x07\n\x05\x65ventb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,device__state__structures__pb2.DESCRIPTOR,])




_CLIENTCONNECTIONEVENT = _descriptor.Descriptor(
  name='ClientConnectionEvent',
  full_name='ClientConnectionEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devices', full_name='ClientConnectionEvent.devices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=74,
  serialized_end=123,
)


_DEVICECONNECTEDEVENT = _descriptor.Descriptor(
  name='DeviceConnectedEvent',
  full_name='DeviceConnectedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='DeviceConnectedEvent.device', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=125,
  serialized_end=172,
)


_DEVICEDISCONNECTEDEVENT = _descriptor.Descriptor(
  name='DeviceDisconnectedEvent',
  full_name='DeviceDisconnectedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='DeviceDisconnectedEvent.device_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=174,
  serialized_end=220,
)


_DEVICEERROREVENT = _descriptor.Descriptor(
  name='DeviceErrorEvent',
  full_name='DeviceErrorEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='DeviceErrorEvent.device_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='DeviceErrorEvent.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=222,
  serialized_end=284,
)


_DEVICEEVENT = _descriptor.Descriptor(
  name='DeviceEvent',
  full_name='DeviceEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_event', full_name='DeviceEvent.connection_event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_connected_event', full_name='DeviceEvent.device_connected_event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_disconnected_event', full_name='DeviceEvent.device_disconnected_event', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_error_event', full_name='DeviceEvent.device_error_event', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='event', full_name='DeviceEvent.event',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=287,
  serialized_end=530,
)

_CLIENTCONNECTIONEVENT.fields_by_name['devices'].message_type = device__state__structures__pb2._DEVICE
_DEVICECONNECTEDEVENT.fields_by_name['device'].message_type = device__state__structures__pb2._DEVICE
_DEVICEERROREVENT.fields_by_name['error'].message_type = common__pb2._ERROR
_DEVICEEVENT.fields_by_name['connection_event'].message_type = _CLIENTCONNECTIONEVENT
_DEVICEEVENT.fields_by_name['device_connected_event'].message_type = _DEVICECONNECTEDEVENT
_DEVICEEVENT.fields_by_name['device_disconnected_event'].message_type = _DEVICEDISCONNECTEDEVENT
_DEVICEEVENT.fields_by_name['device_error_event'].message_type = _DEVICEERROREVENT
_DEVICEEVENT.oneofs_by_name['event'].fields.append(
  _DEVICEEVENT.fields_by_name['connection_event'])
_DEVICEEVENT.fields_by_name['connection_event'].containing_oneof = _DEVICEEVENT.oneofs_by_name['event']
_DEVICEEVENT.oneofs_by_name['event'].fields.append(
  _DEVICEEVENT.fields_by_name['device_connected_event'])
_DEVICEEVENT.fields_by_name['device_connected_event'].containing_oneof = _DEVICEEVENT.oneofs_by_name['event']
_DEVICEEVENT.oneofs_by_name['event'].fields.append(
  _DEVICEEVENT.fields_by_name['device_disconnected_event'])
_DEVICEEVENT.fields_by_name['device_disconnected_event'].containing_oneof = _DEVICEEVENT.oneofs_by_name['event']
_DEVICEEVENT.oneofs_by_name['event'].fields.append(
  _DEVICEEVENT.fields_by_name['device_error_event'])
_DEVICEEVENT.fields_by_name['device_error_event'].containing_oneof = _DEVICEEVENT.oneofs_by_name['event']
DESCRIPTOR.message_types_by_name['ClientConnectionEvent'] = _CLIENTCONNECTIONEVENT
DESCRIPTOR.message_types_by_name['DeviceConnectedEvent'] = _DEVICECONNECTEDEVENT
DESCRIPTOR.message_types_by_name['DeviceDisconnectedEvent'] = _DEVICEDISCONNECTEDEVENT
DESCRIPTOR.message_types_by_name['DeviceErrorEvent'] = _DEVICEERROREVENT
DESCRIPTOR.message_types_by_name['DeviceEvent'] = _DEVICEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientConnectionEvent = _reflection.GeneratedProtocolMessageType('ClientConnectionEvent', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTCONNECTIONEVENT,
  __module__ = 'device_state_events_pb2'
  # @@protoc_insertion_point(class_scope:ClientConnectionEvent)
  ))
_sym_db.RegisterMessage(ClientConnectionEvent)

DeviceConnectedEvent = _reflection.GeneratedProtocolMessageType('DeviceConnectedEvent', (_message.Message,), dict(
  DESCRIPTOR = _DEVICECONNECTEDEVENT,
  __module__ = 'device_state_events_pb2'
  # @@protoc_insertion_point(class_scope:DeviceConnectedEvent)
  ))
_sym_db.RegisterMessage(DeviceConnectedEvent)

DeviceDisconnectedEvent = _reflection.GeneratedProtocolMessageType('DeviceDisconnectedEvent', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEDISCONNECTEDEVENT,
  __module__ = 'device_state_events_pb2'
  # @@protoc_insertion_point(class_scope:DeviceDisconnectedEvent)
  ))
_sym_db.RegisterMessage(DeviceDisconnectedEvent)

DeviceErrorEvent = _reflection.GeneratedProtocolMessageType('DeviceErrorEvent', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEERROREVENT,
  __module__ = 'device_state_events_pb2'
  # @@protoc_insertion_point(class_scope:DeviceErrorEvent)
  ))
_sym_db.RegisterMessage(DeviceErrorEvent)

DeviceEvent = _reflection.GeneratedProtocolMessageType('DeviceEvent', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEEVENT,
  __module__ = 'device_state_events_pb2'
  # @@protoc_insertion_point(class_scope:DeviceEvent)
  ))
_sym_db.RegisterMessage(DeviceEvent)


# @@protoc_insertion_point(module_scope)