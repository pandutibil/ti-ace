# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model


class PaymentParams(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, amount: float=None, currency: str=None, transaction_id: str=None, bank_account_number: str=None, bank_code: str=None, bank_id_type: str=None, virtual_payment_address: str=None):  # noqa: E501
        """PaymentParams - a model defined in Swagger

        :param amount: The amount of this PaymentParams.  # noqa: E501
        :type amount: float
        :param currency: The currency of this PaymentParams.  # noqa: E501
        :type currency: str
        :param transaction_id: The transaction_id of this PaymentParams.  # noqa: E501
        :type transaction_id: str
        :param bank_account_number: The bank_account_number of this PaymentParams.  # noqa: E501
        :type bank_account_number: str
        :param bank_code: The bank_code of this PaymentParams.  # noqa: E501
        :type bank_code: str
        :param bank_id_type: The bank_id_type of this PaymentParams.  # noqa: E501
        :type bank_id_type: str
        :param virtual_payment_address: The virtual_payment_address of this PaymentParams.  # noqa: E501
        :type virtual_payment_address: str
        """
        self.swagger_types = {
            'amount': float,
            'currency': str,
            'transaction_id': str,
            'bank_account_number': str,
            'bank_code': str,
            'bank_id_type': str,
            'virtual_payment_address': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'currency': 'currency',
            'transaction_id': 'transaction_id',
            'bank_account_number': 'bank_account_number',
            'bank_code': 'bank_code',
            'bank_id_type': 'bank_id_type',
            'virtual_payment_address': 'virtual_payment_address'
        }
        self._amount = amount
        self._currency = currency
        self._transaction_id = transaction_id
        self._bank_account_number = bank_account_number
        self._bank_code = bank_code
        self._bank_id_type = bank_id_type
        self._virtual_payment_address = virtual_payment_address

    @classmethod
    def from_dict(cls, dikt) -> 'PaymentParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Payment_params of this PaymentParams.  # noqa: E501
        :rtype: PaymentParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self) -> float:
        """Gets the amount of this PaymentParams.

        The numeric value of the amount that has to be paid for the order  # noqa: E501

        :return: The amount of this PaymentParams.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this PaymentParams.

        The numeric value of the amount that has to be paid for the order  # noqa: E501

        :param amount: The amount of this PaymentParams.
        :type amount: float
        """

        self._amount = amount

    @property
    def currency(self) -> str:
        """Gets the currency of this PaymentParams.


        :return: The currency of this PaymentParams.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this PaymentParams.


        :param currency: The currency of this PaymentParams.
        :type currency: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def transaction_id(self) -> str:
        """Gets the transaction_id of this PaymentParams.

        The transaction reference string that is generated by the payment interface once a transaction is successful. If the payment happened directly on a payment interface of a BPP, then the BPP must return this value to the BAP in the on_confirm API callback. If the payment was collected at the BAP, then this value has to be sent to the BPP when calling the confirm API. When the BAP actually settles the amount with the BPP, it must send this value as reference so that the BPP can mark the payment as settled.  # noqa: E501

        :return: The transaction_id of this PaymentParams.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id: str):
        """Sets the transaction_id of this PaymentParams.

        The transaction reference string that is generated by the payment interface once a transaction is successful. If the payment happened directly on a payment interface of a BPP, then the BPP must return this value to the BAP in the on_confirm API callback. If the payment was collected at the BAP, then this value has to be sent to the BPP when calling the confirm API. When the BAP actually settles the amount with the BPP, it must send this value as reference so that the BPP can mark the payment as settled.  # noqa: E501

        :param transaction_id: The transaction_id of this PaymentParams.
        :type transaction_id: str
        """

        self._transaction_id = transaction_id

    @property
    def bank_account_number(self) -> str:
        """Gets the bank_account_number of this PaymentParams.


        :return: The bank_account_number of this PaymentParams.
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number: str):
        """Sets the bank_account_number of this PaymentParams.


        :param bank_account_number: The bank_account_number of this PaymentParams.
        :type bank_account_number: str
        """

        self._bank_account_number = bank_account_number

    @property
    def bank_code(self) -> str:
        """Gets the bank_code of this PaymentParams.


        :return: The bank_code of this PaymentParams.
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code: str):
        """Sets the bank_code of this PaymentParams.


        :param bank_code: The bank_code of this PaymentParams.
        :type bank_code: str
        """

        self._bank_code = bank_code

    @property
    def bank_id_type(self) -> str:
        """Gets the bank_id_type of this PaymentParams.


        :return: The bank_id_type of this PaymentParams.
        :rtype: str
        """
        return self._bank_id_type

    @bank_id_type.setter
    def bank_id_type(self, bank_id_type: str):
        """Sets the bank_id_type of this PaymentParams.


        :param bank_id_type: The bank_id_type of this PaymentParams.
        :type bank_id_type: str
        """

        self._bank_id_type = bank_id_type

    @property
    def virtual_payment_address(self) -> str:
        """Gets the virtual_payment_address of this PaymentParams.


        :return: The virtual_payment_address of this PaymentParams.
        :rtype: str
        """
        return self._virtual_payment_address

    @virtual_payment_address.setter
    def virtual_payment_address(self, virtual_payment_address: str):
        """Sets the virtual_payment_address of this PaymentParams.


        :param virtual_payment_address: The virtual_payment_address of this PaymentParams.
        :type virtual_payment_address: str
        """

        self._virtual_payment_address = virtual_payment_address