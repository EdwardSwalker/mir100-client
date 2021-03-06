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


class GetSoundStream(object):
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
        'guid': 'str',
        'length': 'str',
        'name': 'str',
        'url': 'str',
        'volume': 'int'
    }

    attribute_map = {
        'guid': 'guid',
        'length': 'length',
        'name': 'name',
        'url': 'url',
        'volume': 'volume'
    }

    def __init__(self, guid=None, length=None, name=None, url=None, volume=None):  # noqa: E501
        """GetSoundStream - a model defined in Swagger"""  # noqa: E501
        self._guid = None
        self._length = None
        self._name = None
        self._url = None
        self._volume = None
        self.discriminator = None
        if guid is not None:
            self.guid = guid
        if length is not None:
            self.length = length
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if volume is not None:
            self.volume = volume

    @property
    def guid(self):
        """Gets the guid of this GetSoundStream.  # noqa: E501

        The global id unique across robots that identifies this sound  # noqa: E501

        :return: The guid of this GetSoundStream.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetSoundStream.

        The global id unique across robots that identifies this sound  # noqa: E501

        :param guid: The guid of this GetSoundStream.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def length(self):
        """Gets the length of this GetSoundStream.  # noqa: E501

        The length of the sound in the format hh:mm:ss  # noqa: E501

        :return: The length of this GetSoundStream.  # noqa: E501
        :rtype: str
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this GetSoundStream.

        The length of the sound in the format hh:mm:ss  # noqa: E501

        :param length: The length of this GetSoundStream.  # noqa: E501
        :type: str
        """

        self._length = length

    @property
    def name(self):
        """Gets the name of this GetSoundStream.  # noqa: E501

        The name of the sound  # noqa: E501

        :return: The name of this GetSoundStream.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetSoundStream.

        The name of the sound  # noqa: E501

        :param name: The name of this GetSoundStream.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this GetSoundStream.  # noqa: E501

        The URL of the resource  # noqa: E501

        :return: The url of this GetSoundStream.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetSoundStream.

        The URL of the resource  # noqa: E501

        :param url: The url of this GetSoundStream.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def volume(self):
        """Gets the volume of this GetSoundStream.  # noqa: E501

        The volumne of the sound when played  # noqa: E501

        :return: The volume of this GetSoundStream.  # noqa: E501
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this GetSoundStream.

        The volumne of the sound when played  # noqa: E501

        :param volume: The volume of this GetSoundStream.  # noqa: E501
        :type: int
        """

        self._volume = volume

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
        if issubclass(GetSoundStream, dict):
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
        if not isinstance(other, GetSoundStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
