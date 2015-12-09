#!/usr/bin/python3

import xml.etree.ElementTree as ET
import marshal as stdm
import types


class XMLMarshaller:
    """
    A class that provides object marshalling into xml and vice versa.
    By default its not marshal fields that starts with '__'.
    This can be changed by '_depth' flag.
    Use:
        marshal(<object>)       -> string
        unmarshal('<filename>') -> object
    Default types:
        int
        bool
        float
        complex
        bytes
        bytearray
        str
        list
        set
        frozenset
        tuple
        dict
        None | NoneType
    """
    _primitive_types = ['int', 'bool', 'float', 'complex', 'bytes', 'bytearray', 'str']
    _sequence_types = ['list', 'set', 'frozenset', 'tuple', 'dict']
    _callable = ['function']
    _none = ['NoneType', 'None']
    _builtin = _primitive_types + _sequence_types + _none
    _declaration = "<?xml version='1.0' encoding='utf-8'?>"
    _depth = False

    def set_deep_marshalling(self, flag):
        """
        Sets the depth of the marshalling.
        """
        if isinstance(flag, bool):
            self._depth = flag

    def marshal(self, data):
        """
        Input: object.
        Output: xml as string.
        """
        _root = ET.Element('object')
        _class = self._get_class(data)
        _root.set('type', _class)
        self._recursive_marshal(data, _root)
        _tree = ET.tostring(_root).decode()
        _tree = self._declaration + _tree
        return _tree

    def _recursive_marshal(self, data, root, name=None):
        """
        Recursive xml tree builder.
        """
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
            for attr in _other:
                bound = getattr(data, attr)
                _type = self._get_class(bound)
                if callable(bound) and self._is_callable(_type):
                    _code = stdm.dumps(bound.__code__)
                    meth = ET.SubElement(root, 'callable')
                    meth.set('name', attr)
                    meth.text = str(_code)
                    meth.set('type', _type)
                    #print(attr)
                    #print (type(_code))
                    #print(_code)
                    #print(str(_code))
                    #print(type(str(_code)))
                    #obj = eval(str(_code))
                    #print(type(obj))

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
        """
        Check depth of the marshalling.
        """
        _fields = []
        for field in fields:
            if self._depth:
                _fields.append(field)
            elif field[0:2] != '__':
                _fields.append(field)
        return _fields

    def unmarshal(self, data):
        """
        Input: filename as string.
        Output: object.
        """
        tree = ET.parse(data)
        root = tree.getroot()
        _type = self._get_type(root)
        if _type == 'NoneType':
            _type = 'None'

        if not self._is_builtin(_type):
            _path = _type.split('.')
            _module = __import__(".".join(_path[0:-1]), fromlist=[_path[-1:]])
            obj = getattr(_module, _path[-1:][0])
            obj = eval("obj()")
            obj = self._recursive_unmarshal(obj, root)
        else:
            obj = eval(_type)
        return obj

    def _recursive_unmarshal(self, obj, root):
        """
        Get the parent object and init all fields of it.
        Output: reinited object.
        """
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

                if not self._is_builtin(_type):
                    _path = _type.split('.')
                    _module = __import__(".".join(_path[0:-1]), fromlist=[_path[-1:]])
                    obj = getattr(_module, _path[-1:][0])
                else:
                    obj = eval(_type)

                for child in _children:
                    _ctype = self._get_type(child)
                    if _ctype == 'NoneType':
                        _ctype = 'None'
                    if not self._is_builtin(_ctype):
                        _path = _ctype.split('.')
                        _module = __import__(".".join(_path[0:-1]), fromlist=[_path[-1:]])
                        elem = getattr(_module, _path[-1:][0])
                    else:
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

                if not self._is_builtin(_type):
                    _path = _type.split('.')
                    _module = __import__(".".join(_path[0:-1]), fromlist=[_path[-1:]])
                    obj = getattr(_module, _path[-1:][0])
                else:
                    obj = eval(_type)

                for child in _children:
                    key = ''
                    value = ''
                    for node in child.getchildren():
                        if node.tag == 'key':
                            _ntype = self._get_type(node)
                            if _ntype == 'NoneType':
                                _ntype = 'None'

                            if not self._is_builtin(_ntype):
                                _path = _ntype.split('.')
                                _module = __import__(".".join(_path[0:-1]), fromlist=[_path[-1:]])
                                key = getattr(_module, _path[-1:][0])
                            else:
                                key = eval(_ntype)

                            key = self._recursive_unmarshal(key, node)
                        elif node.tag == 'value':
                            _ntype = self._get_type(node)
                            if _ntype == 'NoneType':
                                _ntype = 'None'

                            if not self._is_builtin(_ntype):
                                _path = _ntype.split('.')
                                _module = __import__(".".join(_path[0:-1]), fromlist=[_path[-1:]])
                                value = getattr(_module, _path[-1:][0])
                            else:
                                value = eval(_ntype)

                            value = self._recursive_unmarshal(value, node)
                    obj.setdefault(key)
                    obj[key] = value
                return obj

        elif not self._is_builtin(_type):
            _children = root.getchildren()
            if not self._is_builtin(_type):
                _path = _type.split('.')
                _module = __import__(".".join(_path[0:-1]), fromlist=[_path[-1:]])
                elem = getattr(_module, _path[-1:][0])
            else:
                elem = eval(_type)

            for child in _children:
                _ctype = self._get_type(child)
                if _ctype == 'NoneType':
                    _ctype = 'None'
                elif self._is_callable(_ctype):
                    elem = None
                    _code = stdm.loads(eval(child.text))
                    elem = types.FunctionType(_code, globals())

                elif not self._is_builtin(_ctype):
                    _path = _ctype.split('.')
                    _module = __import__(".".join(_path[0:-1]), fromlist=[_path[-1:]])
                    elem = getattr(_module, _path[-1:][0])
                else:
                    elem = eval(_ctype)
                if not self._is_callable(_ctype):
                    elem = self._recursive_unmarshal(elem, child)
                _name = self._get_name(child)
                setattr(obj, _name, elem)
            return obj

        else:
            print ("Undefined type")
            raise RuntimeError()

    def _get_type(self, obj):
        """Returns type of object"""
        return obj.attrib['type']

    def _get_name(self, obj):
        """Returns name of object"""
        return obj.attrib['name']

    def _get_class(self, obj):
        """Returns class of the object"""
        return str(type(obj)).split("'")[1]



    def _separate_attributes(self, obj):
        """Separate types from methods"""
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

    def _is_callable(self, obj):
        """Returns True if obj is method or function"""
        if obj in self._callable:
            return True
        else:
            return False

    def _is_builtin(self, obj):
        """Check objects type(default or not)"""
        if obj in self._builtin:
            return True
        else:
            return False

    def _is_sequence(self, obj):
        """Check objects type(sequence-like or not)"""
        if obj in self._sequence_types:
            return True
        else:
            return False

    def _is_primitive(self, obj):
        """Check objects type(simple or not)"""
        if obj in self._primitive_types:
            return True
        else:
            return False
