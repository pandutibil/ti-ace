# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.feedback_form_element import FeedbackFormElement  # noqa: F401,E501


class FeedbackForm(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """FeedbackForm - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'FeedbackForm':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FeedbackForm of this FeedbackForm.  # noqa: E501
        :rtype: FeedbackForm
        """
        return util.deserialize_model(dikt, cls)