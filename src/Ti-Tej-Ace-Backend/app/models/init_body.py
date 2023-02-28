# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.context import Context  # noqa: F401,E501
from models.select_message import SelectMessage  # noqa: F401,E501


class InitBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, context: Context=None, message: SelectMessage=None):  # noqa: E501
        """InitBody - a model defined in Swagger

        :param context: The context of this InitBody.  # noqa: E501
        :type context: Context
        :param message: The message of this InitBody.  # noqa: E501
        :type message: SelectMessage
        """
        self.swagger_types = {
            'context': Context,
            'message': SelectMessage
        }

        self.attribute_map = {
            'context': 'context',
            'message': 'message'
        }
        self._context = context
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'InitBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The init_body of this InitBody.  # noqa: E501
        :rtype: InitBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context(self) -> Context:
        """Gets the context of this InitBody.


        :return: The context of this InitBody.
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context: Context):
        """Sets the context of this InitBody.


        :param context: The context of this InitBody.
        :type context: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def message(self) -> SelectMessage:
        """Gets the message of this InitBody.


        :return: The message of this InitBody.
        :rtype: SelectMessage
        """
        return self._message

    @message.setter
    def message(self, message: SelectMessage):
        """Sets the message of this InitBody.


        :param message: The message of this InitBody.
        :type message: SelectMessage
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message