# coding: utf-8

"""
    Check Sender API

    Описание взаимодействия с сервисом аренды кассовой техники Check Sender  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeviceStatusResponse(object):
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
        'serial_number': 'str',
        'fiscal_serial_number': 'str'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'fiscal_serial_number': 'fiscal_serial_number'
    }

    def __init__(self, serial_number=None, fiscal_serial_number=None):  # noqa: E501
        """DeviceStatusResponse - a model defined in Swagger"""  # noqa: E501

        self._serial_number = None
        self._fiscal_serial_number = None
        self.discriminator = None

        if serial_number is not None:
            self.serial_number = serial_number
        if fiscal_serial_number is not None:
            self.fiscal_serial_number = fiscal_serial_number

    @property
    def serial_number(self):
        """Gets the serial_number of this DeviceStatusResponse.  # noqa: E501

        Серийный номер ККТ  # noqa: E501

        :return: The serial_number of this DeviceStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this DeviceStatusResponse.

        Серийный номер ККТ  # noqa: E501

        :param serial_number: The serial_number of this DeviceStatusResponse.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def fiscal_serial_number(self):
        """Gets the fiscal_serial_number of this DeviceStatusResponse.  # noqa: E501

        Серийный номер фискального накопителя  # noqa: E501

        :return: The fiscal_serial_number of this DeviceStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._fiscal_serial_number

    @fiscal_serial_number.setter
    def fiscal_serial_number(self, fiscal_serial_number):
        """Sets the fiscal_serial_number of this DeviceStatusResponse.

        Серийный номер фискального накопителя  # noqa: E501

        :param fiscal_serial_number: The fiscal_serial_number of this DeviceStatusResponse.  # noqa: E501
        :type: str
        """

        self._fiscal_serial_number = fiscal_serial_number

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
