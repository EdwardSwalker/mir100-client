# coding: utf-8

"""
    MIR100 Rest Interface

    Automatically converted from v270 pdf  # noqa: E501

    OpenAPI spec version: 2.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class GetAreaEvent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'actions': 'str',
        'created_by': 'str',
        'created_by_id': 'str',
        'guid': 'str',
        'map': 'str',
        'map_id': 'str',
        'name': 'str',
        'polygon': 'list[object]',
        'type_id': 'int'
    }

    attribute_map = {
        'actions': 'actions',
        'created_by': 'created_by',
        'created_by_id': 'created_by_id',
        'guid': 'guid',
        'map': 'map',
        'map_id': 'map_id',
        'name': 'name',
        'polygon': 'polygon',
        'type_id': 'type_id'
    }

    def __init__(self, actions=None, created_by=None, created_by_id=None, guid=None, map=None, map_id=None, name=None, polygon=None, type_id=None):  # noqa: E501
        """GetAreaEvent - a model defined in Swagger"""  # noqa: E501
        self._actions = None
        self._created_by = None
        self._created_by_id = None
        self._guid = None
        self._map = None
        self._map_id = None
        self._name = None
        self._polygon = None
        self._type_id = None
        self.discriminator = None
        if actions is not None:
            self.actions = actions
        if created_by is not None:
            self.created_by = created_by
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if guid is not None:
            self.guid = guid
        if map is not None:
            self.map = map
        if map_id is not None:
            self.map_id = map_id
        if name is not None:
            self.name = name
        if polygon is not None:
            self.polygon = polygon
        if type_id is not None:
            self.type_id = type_id

    @property
    def actions(self):
        """Gets the actions of this GetAreaEvent.  # noqa: E501


        :return: The actions of this GetAreaEvent.  # noqa: E501
        :rtype: str
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this GetAreaEvent.


        :param actions: The actions of this GetAreaEvent.  # noqa: E501
        :type: str
        """

        self._actions = actions

    @property
    def created_by(self):
        """Gets the created_by of this GetAreaEvent.  # noqa: E501

        The url to the description of the type of this position  # noqa: E501

        :return: The created_by of this GetAreaEvent.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetAreaEvent.

        The url to the description of the type of this position  # noqa: E501

        :param created_by: The created_by of this GetAreaEvent.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetAreaEvent.  # noqa: E501

        The global id of the user who created this entry  # noqa: E501

        :return: The created_by_id of this GetAreaEvent.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetAreaEvent.

        The global id of the user who created this entry  # noqa: E501

        :param created_by_id: The created_by_id of this GetAreaEvent.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def guid(self):
        """Gets the guid of this GetAreaEvent.  # noqa: E501

        The global id unique across robots that identifies this area  # noqa: E501

        :return: The guid of this GetAreaEvent.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetAreaEvent.

        The global id unique across robots that identifies this area  # noqa: E501

        :param guid: The guid of this GetAreaEvent.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def map(self):
        """Gets the map of this GetAreaEvent.  # noqa: E501

        The url to the map this area belongs to  # noqa: E501

        :return: The map of this GetAreaEvent.  # noqa: E501
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this GetAreaEvent.

        The url to the map this area belongs to  # noqa: E501

        :param map: The map of this GetAreaEvent.  # noqa: E501
        :type: str
        """

        self._map = map

    @property
    def map_id(self):
        """Gets the map_id of this GetAreaEvent.  # noqa: E501

        The id of the map this area belongs to  # noqa: E501

        :return: The map_id of this GetAreaEvent.  # noqa: E501
        :rtype: str
        """
        return self._map_id

    @map_id.setter
    def map_id(self, map_id):
        """Sets the map_id of this GetAreaEvent.

        The id of the map this area belongs to  # noqa: E501

        :param map_id: The map_id of this GetAreaEvent.  # noqa: E501
        :type: str
        """

        self._map_id = map_id

    @property
    def name(self):
        """Gets the name of this GetAreaEvent.  # noqa: E501

        A name associated with this area  # noqa: E501

        :return: The name of this GetAreaEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAreaEvent.

        A name associated with this area  # noqa: E501

        :param name: The name of this GetAreaEvent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def polygon(self):
        """Gets the polygon of this GetAreaEvent.  # noqa: E501

        The list of coordinates in the area polygon  # noqa: E501

        :return: The polygon of this GetAreaEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._polygon

    @polygon.setter
    def polygon(self, polygon):
        """Sets the polygon of this GetAreaEvent.

        The list of coordinates in the area polygon  # noqa: E501

        :param polygon: The polygon of this GetAreaEvent.  # noqa: E501
        :type: list[object]
        """

        self._polygon = polygon

    @property
    def type_id(self):
        """Gets the type_id of this GetAreaEvent.  # noqa: E501

        The type of area  # noqa: E501

        :return: The type_id of this GetAreaEvent.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetAreaEvent.

        The type of area  # noqa: E501

        :param type_id: The type_id of this GetAreaEvent.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetAreaEvent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetAreaEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
