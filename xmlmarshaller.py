#!/usr/bin/python3

import xml.etree.ElementTree as ET


class XMLMarshaller:
    _primitive_types = ['int', 'bool', 'float', 'complex', 'bytes', 'bytearray', 'str']
    _sequence_types = ['list', 'set', 'frozenset', 'tuple', 'dict']
    _none = ['NoneType']
    _builtin = _primitive_types + _sequence_types + _none
    _declaration = "<?xml version='1.0' encoding='utf-8'?>"

    def marshal(self, data):
        _root = ET.Element('object')
        _class = self._get_class(data)
        _root.set('type', _class)
        self._recursive_marshal(data, _root)
        _tree = ET.tostring(_root).decode()
        _tree = self._declaration + _tree
        return _tree

    def _recursive_marshal(self, data, root, name=None):
        _class = self._get_class(data)
        if self._is_primitive(_class):
            root.text = str(data)
            if name:
                root.set('name', name)
        elif self._is_sequence(_class):
            if name:
                root.set('name', name)
            if _class != 'dict':
                for element in data:
                    _fclass = self._get_class(element)
                    field = ET.SubElement(root, 'field')
                    field.set('type', _fclass)
                    self._recursive_marshal(element, field)

            else:
                for key, value in data.items():
                    _vclass = self._get_class(value)
                    _kclass = self._get_class(key)
                    field = ET.SubElement(root, 'field')
                    nkey = ET.SubElement(field, 'key')
                    nkey.set('type', _kclass)
                    nvalue = ET.SubElement(field, 'value')
                    nvalue.set('type', _vclass)
                    self._recursive_marshal(value, nvalue)
                    self._recursive_marshal(key, nkey)

        elif not self._is_builtin(_class):
            if name:
                root.set('name', name)
            _fields, _other = self._separate_attributes(data)
            _fields = self._sort_attributes(_fields)
            for value in _fields:
                _value = getattr(data, value)
                _fclass = self._get_class(_value)
                field = ET.SubElement(root, 'field')
                field.set('type', _fclass)
                self._recursive_marshal(_value, field, value)
        else:
            if name:
                root.set('name', name)

    def _sort_attributes(self, fields):
        _fields = []
        for field in fields:
            if field[0:2] != '__':
                _fields.append(field)
        return _fields

    def unmarshal(self, data):
        tree = ET.parse(data)
        root = tree.getroot()
        _type = self._get_type(root)
        if _type == 'NoneType':
            _type = 'None'
        obj = eval(_type)
        obj = self._recursive_unmarshal(obj, root)
        return obj

    def _recursive_unmarshal(self, obj, root):
        _type = self._get_type(root)
        if _type == 'NoneType':
            _type = 'None'
        if self._is_primitive(_type):
            obj = eval(_type +'("'+root.text+'")')
            return obj
        elif self._is_sequence(_type):
            if _type != 'dict':
                _children = root.getchildren()
                if _type == 'frozenset':
                    _type = 'set'
                obj = eval(_type +'()')
                for child in _children:
                    _ctype = self._get_type(child)
                    if _ctype == 'NoneType':
                        _ctype = 'None'
                    elem = eval(_ctype)
                    elem = self._recursive_unmarshal(elem, child)
                    if _type == 'list':
                        obj.append(elem)
                    elif _type == 'set' or _type == 'frozenset':
                        obj.add(elem)
                    elif _type == 'tuple':
                        obj += (elem,)
                _type = self._get_type(root)
                if _type == 'NoneType':
                    _type = 'None'
                if _type == 'frozenset':
                    obj = frozenset(obj)
                return obj
            else:
                _children = root.getchildren()
                obj = eval(_type)
                for child in _children:
                    key = ''
                    value = ''
                    for node in child.getchildren():
                        if node.tag == 'key':
                            _ntype = self._get_type(node)
                            if _ntype == 'NoneType':
                                _ntype = 'None'
                            key = eval(_ntype)
                            key = self._recursive_unmarshal(key, node)
                        elif node.tag == 'value':
                            _ntype = self._get_type(node)
                            if _ntype == 'NoneType':
                                _ntype = 'None'
                            value = eval(_ntype)
                            value = self._recursive_unmarshal(value, node)
                    obj.setdefault(key)
                    obj[key] = value
                return obj

        elif not self._is_builtin(_type):
            _children = root.getchildren()
            obj = eval(_type)
            for child in _children:
                _ctype = self._get_type(child)
                if _ctype == 'NoneType':
                    _ctype = 'None'
                elem = eval(_ctype)
                elem = self._recursive_unmarshal(elem, child)
                _name = self._get_name(child)

                setattr(obj, _name, elem)
            return obj
        else:
            pass

    def _get_type(self, obj):
        return obj.attrib['type']

    def _get_name(self, obj):
        return obj.attrib['name']

    def _get_class(self, obj):
        return type(obj).__name__

    def _separate_attributes(self, obj):
        _attributes = dir(obj)
        _fields = []
        _others = []
        _class = self._get_class(obj)
        for attr in _attributes:
            if callable(getattr(obj, attr)):
                _others.append(attr)
            else:
                _fields.append(attr)
        return _fields, _others

    def _is_builtin(self, obj):
        if obj in self._builtin:
            return True
        else:
            return False

    def _is_sequence(self, obj):
        if obj in self._sequence_types:
            return True
        else:
            return False

    def _is_primitive(self, obj):
        if obj in self._primitive_types:
            return True
        else:
            return False
