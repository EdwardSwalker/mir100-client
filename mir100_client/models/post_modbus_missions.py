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


class PostModbusMissions(object):
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
        'coil_id': 'int',
        'created_by_id': 'str',
        'guid': 'str',
        'mission_id': 'str',
        'name': 'str',
        'parameters': 'list[object]'
    }

    attribute_map = {
        'coil_id': 'coil_id',
        'created_by_id': 'created_by_id',
        'guid': 'guid',
        'mission_id': 'mission_id',
        'name': 'name',
        'parameters': 'parameters'
    }

    def __init__(self, coil_id=None, created_by_id=None, guid=None, mission_id=None, name=None, parameters=None):  # noqa: E501
        """PostModbusMissions - a model defined in Swagger"""  # noqa: E501
        self._coil_id = None
        self._created_by_id = None
        self._guid = None
        self._mission_id = None
        self._name = None
        self._parameters = None
        self.discriminator = None
        self.coil_id = coil_id
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if guid is not None:
            self.guid = guid
        self.mission_id = mission_id
        self.name = name
        if parameters is not None:
            self.parameters = parameters

    @property
    def coil_id(self):
        """Gets the coil_id of this PostModbusMissions.  # noqa: E501


        :return: The coil_id of this PostModbusMissions.  # noqa: E501
        :rtype: int
        """
        return self._coil_id

    @coil_id.setter
    def coil_id(self, coil_id):
        """Sets the coil_id of this PostModbusMissions.


        :param coil_id: The coil_id of this PostModbusMissions.  # noqa: E501
        :type: int
        """
        if coil_id is None:
            raise ValueError("Invalid value for `coil_id`, must not be `None`")  # noqa: E501

        self._coil_id = coil_id

    @property
    def created_by_id(self):
        """Gets the created_by_id of this PostModbusMissions.  # noqa: E501


        :return: The created_by_id of this PostModbusMissions.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this PostModbusMissions.


        :param created_by_id: The created_by_id of this PostModbusMissions.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def guid(self):
        """Gets the guid of this PostModbusMissions.  # noqa: E501


        :return: The guid of this PostModbusMissions.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PostModbusMissions.


        :param guid: The guid of this PostModbusMissions.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def mission_id(self):
        """Gets the mission_id of this PostModbusMissions.  # noqa: E501


        :return: The mission_id of this PostModbusMissions.  # noqa: E501
        :rtype: str
        """
        return self._mission_id

    @mission_id.setter
    def mission_id(self, mission_id):
        """Sets the mission_id of this PostModbusMissions.


        :param mission_id: The mission_id of this PostModbusMissions.  # noqa: E501
        :type: str
        """
        if mission_id is None:
            raise ValueError("Invalid value for `mission_id`, must not be `None`")  # noqa: E501

        self._mission_id = mission_id

    @property
    def name(self):
        """Gets the name of this PostModbusMissions.  # noqa: E501

        Min length: 1, Max length: 200  # noqa: E501

        :return: The name of this PostModbusMissions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostModbusMissions.

        Min length: 1, Max length: 200  # noqa: E501

        :param name: The name of this PostModbusMissions.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this PostModbusMissions.  # noqa: E501


        :return: The parameters of this PostModbusMissions.  # noqa: E501
        :rtype: list[object]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this PostModbusMissions.


        :param parameters: The parameters of this PostModbusMissions.  # noqa: E501
        :type: list[object]
        """

        self._parameters = parameters

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
        if issubclass(PostModbusMissions, dict):
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
        if not isinstance(other, PostModbusMissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other