# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model


class Ack(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, status: str=None):  # noqa: E501
        """Ack - a model defined in Swagger

        :param status: The status of this Ack.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'status': str
        }

        self.attribute_map = {
            'status': 'status'
        }
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Ack':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ack of this Ack.  # noqa: E501
        :rtype: Ack
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> str:
        """Gets the status of this Ack.

        Describe the status of the ACK response. If the message passes the acknowledgement criteria, then the receiver shouls set this value equal to ACK else it should be set to NACK  # noqa: E501

        :return: The status of this Ack.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Ack.

        Describe the status of the ACK response. If the message passes the acknowledgement criteria, then the receiver shouls set this value equal to ACK else it should be set to NACK  # noqa: E501

        :param status: The status of this Ack.
        :type status: str
        """
        allowed_values = ["ACK", "NACK"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
