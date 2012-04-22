# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='les/mp_model/mp_model.proto',
  package='les.mp_model',
  serialized_pb='\n\x1bles/mp_model/mp_model.proto\x12\x0cles.mp_model\"+\n\x06MPTerm\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0b\x63oefficient\x18\x02 \x02(\x01\"J\n\nMPVariable\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x16\n\x0blower_bound\x18\x02 \x02(\x01:\x01\x30\x12\x16\n\x0bupper_bound\x18\x03 \x02(\x01:\x01\x31\"k\n\x0cMPConstraint\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0blower_bound\x18\x02 \x02(\x01\x12\x13\n\x0bupper_bound\x18\x03 \x02(\x01\x12#\n\x05terms\x18\x04 \x03(\x0b\x32\x14.les.mp_model.MPTerm\"N\n\x0bMPObjective\x12\x1a\n\x0cmaximization\x18\x01 \x02(\x08:\x04true\x12#\n\x05terms\x18\x02 \x03(\x0b\x32\x14.les.mp_model.MPTerm\"v\n\x07MPModel\x12\x0c\n\x04name\x18\x01 \x02(\t\x12,\n\tobjective\x18\x02 \x02(\x0b\x32\x19.les.mp_model.MPObjective\x12/\n\x0b\x63onstraints\x18\x03 \x02(\x0b\x32\x1a.les.mp_model.MPConstraint')




_MPTERM = descriptor.Descriptor(
  name='MPTerm',
  full_name='les.mp_model.MPTerm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='les.mp_model.MPTerm.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='coefficient', full_name='les.mp_model.MPTerm.coefficient', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=88,
)


_MPVARIABLE = descriptor.Descriptor(
  name='MPVariable',
  full_name='les.mp_model.MPVariable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='les.mp_model.MPVariable.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lower_bound', full_name='les.mp_model.MPVariable.lower_bound', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='upper_bound', full_name='les.mp_model.MPVariable.upper_bound', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=90,
  serialized_end=164,
)


_MPCONSTRAINT = descriptor.Descriptor(
  name='MPConstraint',
  full_name='les.mp_model.MPConstraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='les.mp_model.MPConstraint.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lower_bound', full_name='les.mp_model.MPConstraint.lower_bound', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='upper_bound', full_name='les.mp_model.MPConstraint.upper_bound', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='terms', full_name='les.mp_model.MPConstraint.terms', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=166,
  serialized_end=273,
)


_MPOBJECTIVE = descriptor.Descriptor(
  name='MPObjective',
  full_name='les.mp_model.MPObjective',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='maximization', full_name='les.mp_model.MPObjective.maximization', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='terms', full_name='les.mp_model.MPObjective.terms', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=275,
  serialized_end=353,
)


_MPMODEL = descriptor.Descriptor(
  name='MPModel',
  full_name='les.mp_model.MPModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='les.mp_model.MPModel.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='objective', full_name='les.mp_model.MPModel.objective', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='constraints', full_name='les.mp_model.MPModel.constraints', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=355,
  serialized_end=473,
)

_MPCONSTRAINT.fields_by_name['terms'].message_type = _MPTERM
_MPOBJECTIVE.fields_by_name['terms'].message_type = _MPTERM
_MPMODEL.fields_by_name['objective'].message_type = _MPOBJECTIVE
_MPMODEL.fields_by_name['constraints'].message_type = _MPCONSTRAINT
DESCRIPTOR.message_types_by_name['MPTerm'] = _MPTERM
DESCRIPTOR.message_types_by_name['MPVariable'] = _MPVARIABLE
DESCRIPTOR.message_types_by_name['MPConstraint'] = _MPCONSTRAINT
DESCRIPTOR.message_types_by_name['MPObjective'] = _MPOBJECTIVE
DESCRIPTOR.message_types_by_name['MPModel'] = _MPMODEL

class MPTerm(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MPTERM
  
  # @@protoc_insertion_point(class_scope:les.mp_model.MPTerm)

class MPVariable(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MPVARIABLE
  
  # @@protoc_insertion_point(class_scope:les.mp_model.MPVariable)

class MPConstraint(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MPCONSTRAINT
  
  # @@protoc_insertion_point(class_scope:les.mp_model.MPConstraint)

class MPObjective(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MPOBJECTIVE
  
  # @@protoc_insertion_point(class_scope:les.mp_model.MPObjective)

class MPModel(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MPMODEL
  
  # @@protoc_insertion_point(class_scope:les.mp_model.MPModel)

# @@protoc_insertion_point(module_scope)