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


class PutMissionQueue(object):
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
        'cmd': 'int',
        'description': 'str',
        'mission_id': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'cmd': 'cmd',
        'description': 'description',
        'mission_id': 'mission_id',
        'priority': 'priority'
    }

    def __init__(self, cmd=None, description=None, mission_id=None, priority=None):  # noqa: E501
        """PutMissionQueue - a model defined in Swagger"""  # noqa: E501
        self._cmd = None
        self._description = None
        self._mission_id = None
        self._priority = None
        self.discriminator = None
        if cmd is not None:
            self.cmd = cmd
        if description is not None:
            self.description = description
        if mission_id is not None:
            self.mission_id = mission_id
        if priority is not None:
            self.priority = priority

    @property
    def cmd(self):
        """Gets the cmd of this PutMissionQueue.  # noqa: E501


        :return: The cmd of this PutMissionQueue.  # noqa: E501
        :rtype: int
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        """Sets the cmd of this PutMissionQueue.


        :param cmd: The cmd of this PutMissionQueue.  # noqa: E501
        :type: int
        """

        self._cmd = cmd

    @property
    def description(self):
        """Gets the description of this PutMissionQueue.  # noqa: E501

        Max length: 200  # noqa: E501

        :return: The description of this PutMissionQueue.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutMissionQueue.

        Max length: 200  # noqa: E501

        :param description: The description of this PutMissionQueue.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mission_id(self):
        """Gets the mission_id of this PutMissionQueue.  # noqa: E501


        :return: The mission_id of this PutMissionQueue.  # noqa: E501
        :rtype: str
        """
        return self._mission_id

    @mission_id.setter
    def mission_id(self, mission_id):
        """Sets the mission_id of this PutMissionQueue.


        :param mission_id: The mission_id of this PutMissionQueue.  # noqa: E501
        :type: str
        """

        self._mission_id = mission_id

    @property
    def priority(self):
        """Gets the priority of this PutMissionQueue.  # noqa: E501


        :return: The priority of this PutMissionQueue.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PutMissionQueue.


        :param priority: The priority of this PutMissionQueue.  # noqa: E501
        :type: int
        """

        self._priority = priority

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
        if issubclass(PutMissionQueue, dict):
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
        if not isinstance(other, PutMissionQueue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other