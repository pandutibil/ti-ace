# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.all_of_provider_locations_items import AllOfProviderLocationsItems  # noqa: F401,E501
from models.base_model_ import Model
from models.category import Category  # noqa: F401,E501
from models.descriptor import Descriptor  # noqa: F401,E501
from models.fulfillment import Fulfillment  # noqa: F401,E501
from models.item import Item  # noqa: F401,E501
from models.offer import Offer  # noqa: F401,E501
from models.payment import Payment  # noqa: F401,E501
from models.rateable import Rateable  # noqa: F401,E501
from models.tags import Tags  # noqa: F401,E501
from models.time import Time  # noqa: F401,E501


class Provider(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, descriptor: Descriptor=None, category_id: str=None, rating: str=None, time: Time=None, categories: List[Category]=None, fulfillments: List[Fulfillment]=None, payments: List[Payment]=None, locations: List[AllOfProviderLocationsItems]=None, offers: List[Offer]=None, items: List[Item]=None, exp: datetime=None, rateable: Rateable=None, tags: Tags=None):  # noqa: E501
        """Provider - a model defined in Swagger

        :param id: The id of this Provider.  # noqa: E501
        :type id: str
        :param descriptor: The descriptor of this Provider.  # noqa: E501
        :type descriptor: Descriptor
        :param category_id: The category_id of this Provider.  # noqa: E501
        :type category_id: str
        :param rating: The rating of this Provider.  # noqa: E501
        :type rating: str
        :param time: The time of this Provider.  # noqa: E501
        :type time: Time
        :param categories: The categories of this Provider.  # noqa: E501
        :type categories: List[Category]
        :param fulfillments: The fulfillments of this Provider.  # noqa: E501
        :type fulfillments: List[Fulfillment]
        :param payments: The payments of this Provider.  # noqa: E501
        :type payments: List[Payment]
        :param locations: The locations of this Provider.  # noqa: E501
        :type locations: List[AllOfProviderLocationsItems]
        :param offers: The offers of this Provider.  # noqa: E501
        :type offers: List[Offer]
        :param items: The items of this Provider.  # noqa: E501
        :type items: List[Item]
        :param exp: The exp of this Provider.  # noqa: E501
        :type exp: datetime
        :param rateable: The rateable of this Provider.  # noqa: E501
        :type rateable: Rateable
        :param tags: The tags of this Provider.  # noqa: E501
        :type tags: Tags
        """
        self.swagger_types = {
            'id': str,
            'descriptor': Descriptor,
            'category_id': str,
            'rating': str,
            'time': Time,
            'categories': List[Category],
            'fulfillments': List[Fulfillment],
            'payments': List[Payment],
            'locations': List[AllOfProviderLocationsItems],
            'offers': List[Offer],
            'items': List[Item],
            'exp': datetime,
            'rateable': Rateable,
            'tags': Tags
        }

        self.attribute_map = {
            'id': 'id',
            'descriptor': 'descriptor',
            'category_id': 'category_id',
            'rating': 'rating',
            'time': 'time',
            'categories': 'categories',
            'fulfillments': 'fulfillments',
            'payments': 'payments',
            'locations': 'locations',
            'offers': 'offers',
            'items': 'items',
            'exp': 'exp',
            'rateable': 'rateable',
            'tags': 'tags'
        }
        self._id = id
        self._descriptor = descriptor
        self._category_id = category_id
        self._rating = rating
        self._time = time
        self._categories = categories
        self._fulfillments = fulfillments
        self._payments = payments
        self._locations = locations
        self._offers = offers
        self._items = items
        self._exp = exp
        self._rateable = rateable
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> 'Provider':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Provider of this Provider.  # noqa: E501
        :rtype: Provider
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Provider.

        Id of the provider  # noqa: E501

        :return: The id of this Provider.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Provider.

        Id of the provider  # noqa: E501

        :param id: The id of this Provider.
        :type id: str
        """

        self._id = id

    @property
    def descriptor(self) -> Descriptor:
        """Gets the descriptor of this Provider.


        :return: The descriptor of this Provider.
        :rtype: Descriptor
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor: Descriptor):
        """Sets the descriptor of this Provider.


        :param descriptor: The descriptor of this Provider.
        :type descriptor: Descriptor
        """

        self._descriptor = descriptor

    @property
    def category_id(self) -> str:
        """Gets the category_id of this Provider.

        Category Id of the provider  # noqa: E501

        :return: The category_id of this Provider.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id: str):
        """Sets the category_id of this Provider.

        Category Id of the provider  # noqa: E501

        :param category_id: The category_id of this Provider.
        :type category_id: str
        """

        self._category_id = category_id

    @property
    def rating(self) -> str:
        """Gets the rating of this Provider.


        :return: The rating of this Provider.
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating: str):
        """Sets the rating of this Provider.


        :param rating: The rating of this Provider.
        :type rating: str
        """

        self._rating = rating

    @property
    def time(self) -> Time:
        """Gets the time of this Provider.


        :return: The time of this Provider.
        :rtype: Time
        """
        return self._time

    @time.setter
    def time(self, time: Time):
        """Sets the time of this Provider.


        :param time: The time of this Provider.
        :type time: Time
        """

        self._time = time

    @property
    def categories(self) -> List[Category]:
        """Gets the categories of this Provider.


        :return: The categories of this Provider.
        :rtype: List[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List[Category]):
        """Sets the categories of this Provider.


        :param categories: The categories of this Provider.
        :type categories: List[Category]
        """

        self._categories = categories

    @property
    def fulfillments(self) -> List[Fulfillment]:
        """Gets the fulfillments of this Provider.


        :return: The fulfillments of this Provider.
        :rtype: List[Fulfillment]
        """
        return self._fulfillments

    @fulfillments.setter
    def fulfillments(self, fulfillments: List[Fulfillment]):
        """Sets the fulfillments of this Provider.


        :param fulfillments: The fulfillments of this Provider.
        :type fulfillments: List[Fulfillment]
        """

        self._fulfillments = fulfillments

    @property
    def payments(self) -> List[Payment]:
        """Gets the payments of this Provider.


        :return: The payments of this Provider.
        :rtype: List[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments: List[Payment]):
        """Sets the payments of this Provider.


        :param payments: The payments of this Provider.
        :type payments: List[Payment]
        """

        self._payments = payments

    @property
    def locations(self) -> List[AllOfProviderLocationsItems]:
        """Gets the locations of this Provider.


        :return: The locations of this Provider.
        :rtype: List[AllOfProviderLocationsItems]
        """
        return self._locations

    @locations.setter
    def locations(self, locations: List[AllOfProviderLocationsItems]):
        """Sets the locations of this Provider.


        :param locations: The locations of this Provider.
        :type locations: List[AllOfProviderLocationsItems]
        """

        self._locations = locations

    @property
    def offers(self) -> List[Offer]:
        """Gets the offers of this Provider.


        :return: The offers of this Provider.
        :rtype: List[Offer]
        """
        return self._offers

    @offers.setter
    def offers(self, offers: List[Offer]):
        """Sets the offers of this Provider.


        :param offers: The offers of this Provider.
        :type offers: List[Offer]
        """

        self._offers = offers

    @property
    def items(self) -> List[Item]:
        """Gets the items of this Provider.


        :return: The items of this Provider.
        :rtype: List[Item]
        """
        return self._items

    @items.setter
    def items(self, items: List[Item]):
        """Sets the items of this Provider.


        :param items: The items of this Provider.
        :type items: List[Item]
        """

        self._items = items

    @property
    def exp(self) -> datetime:
        """Gets the exp of this Provider.

        Time after which catalog has to be refreshed  # noqa: E501

        :return: The exp of this Provider.
        :rtype: datetime
        """
        return self._exp

    @exp.setter
    def exp(self, exp: datetime):
        """Sets the exp of this Provider.

        Time after which catalog has to be refreshed  # noqa: E501

        :param exp: The exp of this Provider.
        :type exp: datetime
        """

        self._exp = exp

    @property
    def rateable(self) -> Rateable:
        """Gets the rateable of this Provider.


        :return: The rateable of this Provider.
        :rtype: Rateable
        """
        return self._rateable

    @rateable.setter
    def rateable(self, rateable: Rateable):
        """Sets the rateable of this Provider.


        :param rateable: The rateable of this Provider.
        :type rateable: Rateable
        """

        self._rateable = rateable

    @property
    def tags(self) -> Tags:
        """Gets the tags of this Provider.


        :return: The tags of this Provider.
        :rtype: Tags
        """
        return self._tags

    @tags.setter
    def tags(self, tags: Tags):
        """Sets the tags of this Provider.


        :param tags: The tags of this Provider.
        :type tags: Tags
        """

        self._tags = tags
