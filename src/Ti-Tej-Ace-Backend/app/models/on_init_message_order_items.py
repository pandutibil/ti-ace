# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models import ItemQuantitypropertiesselected  # noqa: F401,E501
from models import str  # noqa: F401,E501


class OnInitMessageOrderItems(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, quantity: ItemQuantitypropertiesselected=None):  # noqa: E501
        """OnInitMessageOrderItems - a model defined in Swagger

        :param id: The id of this OnInitMessageOrderItems.  # noqa: E501
        :type id: str
        :param quantity: The quantity of this OnInitMessageOrderItems.  # noqa: E501
        :type quantity: ItemQuantitypropertiesselected
        """
        self.swagger_types = {
            'id': str,
            'quantity': ItemQuantitypropertiesselected
        }

        self.attribute_map = {
            'id': 'id',
            'quantity': 'quantity'
        }
        self._id = id
        self._quantity = quantity

    @classmethod
    def from_dict(cls, dikt) -> 'OnInitMessageOrderItems':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The on_init_message_order_items of this OnInitMessageOrderItems.  # noqa: E501
        :rtype: OnInitMessageOrderItems
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this OnInitMessageOrderItems.


        :return: The id of this OnInitMessageOrderItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this OnInitMessageOrderItems.


        :param id: The id of this OnInitMessageOrderItems.
        :type id: str
        """

        self._id = id

    @property
    def quantity(self) -> ItemQuantitypropertiesselected:
        """Gets the quantity of this OnInitMessageOrderItems.


        :return: The quantity of this OnInitMessageOrderItems.
        :rtype: ItemQuantitypropertiesselected
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: ItemQuantitypropertiesselected):
        """Sets the quantity of this OnInitMessageOrderItems.


        :param quantity: The quantity of this OnInitMessageOrderItems.
        :type quantity: ItemQuantitypropertiesselected
        """

        self._quantity = quantity