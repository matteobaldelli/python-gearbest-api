"""
Gearbest API
https://affiliate.gearbest.com/documents
"""

import time
import requests
from hashlib import md5

_ENDPOINT = "https://affiliate.gearbest.com/api"
_ORDERS = "orders"
_PRODUCTS = "products"
_BANNER = "banner"
_PROMOTIONS = "promotions"
_COUPON = "coupon"


class GearbestApi(object):
    def __init__(self, api_key: int, api_secret: str):
        self._api_key = api_key
        self._api_secret = api_secret

    def get_completed_orders(self, start_date: str, end_date: str, page: int = 1) -> dict:
        """
        Get completed orders
        :param str start_date: The start date of orders
        :param str end_date: The end date of orders
        :param int page: Number page
        :return dict: A collection of list completed orders
        """
        url = "{}/{}/completed-orders".format(_ENDPOINT, _ORDERS)
        payload = {
            'api_key': self._api_key,
            'end_date': end_date,
            'page': page,
            'start_date': start_date,
        }
        return self._make_request(url=url, payload=payload)

    def get_list_promotion_product(self, category: int, keywords: str, lkid: int, country_website: str,
                                   currency: str = 'USD', page: int = 1) -> dict:
        """
        Get list promotion product
        :param int category: Number of category
        :param str keywords: Keywords for product
        :param str lkid: lkid
        :param str country_website: Country website
        :param str currency: currency
        :param int page: Number page
        :return dict: A collection of list promotion product
        """
        url = "{}/{}/list-promotion-products".format(_ENDPOINT, _PRODUCTS)
        payload = {
            'api_key': self._api_key,
            'category': category,
            'country_website': country_website,
            'currency': currency,
            'keywords': keywords,
            'lkid': lkid,
            'page': page,
        }
        return self._make_request(url=url, payload=payload)

    def get_list_event_creative(self, type: int, category: int, language: str, size: str = None, lkid: int = None,
                                page: int = 1) -> dict:
        """
        Get list event creative
        :param int type: Type of event
        :param int category: Number of category
        :param str language: Language
        :param str size: Size of banner
        :param str lkid: lkid
        :param int page: Number page
        :return dict: A collection of list event creative
        """
        url = "{}/{}/list-event-creative".format(_ENDPOINT, _BANNER)
        payload = {
            'api_key': self._api_key,
            'category': category,
            'language': language,
            'lkid': lkid,
            'page': page,
            'size': size,
            'type': type,
        }
        return self._make_request(url=url, payload=payload)

    def get_list_product_creative(self, type: int, category: int, lkid: int = None, page: int = 1) -> dict:
        """
        Get list product creative
        :param int type: Type of event
        :param int category: Number of category
        :param str lkid: lkid
        :param int page: Number page
        :return dict: A collection of list product creative
        """
        url = "{}/{}/list-product-creative".format(_ENDPOINT, _PROMOTIONS)
        payload = {
            'api_key': self._api_key,
            'category': category,
            'lkid': lkid,
            'page': page,
            'type': type,
        }
        return self._make_request(url=url, payload=payload)

    def get_list_coupons(self, category: int, language: str, lkid: int = None, page: int = 1) -> dict:
        """
        Get list coupons
        :param int category: Number of category
        :param str language: Language
        :param str lkid: lkid
        :param int page: Number page
        :return dict: A collection of list coupons
        """
        url = "{}/{}/list-coupons".format(_ENDPOINT, _COUPON)
        payload = {
            'api_key': self._api_key,
            'category': category,
            'language': language,
            'lkid': lkid,
            'page': page,
        }
        return self._make_request(url=url, payload=payload)

    # def get_promotion_links(self, associate_id: int, link_names: str, urls: list) -> dict:
    #     url = "{}/{}/get-promotion-links".format(_ENDPOINT, _PROMOTIONS)
    #     payload = {
    #         'api_key': self._api_key,
    #         'associate_id': associate_id,
    #         'link_names': link_names,
    #         'urls': urls,
    #     }
    #     return self._make_request(url=url, payload=payload)

    def get_app_exclusive_price_product(self, page: int = 1) -> dict:
        """
        Get app exclusive price product
        :param int page: Number page
        :return dict: A collection of list app exclusive price product
        """
        url = "{}/{}/get-app-exclusive-price-product".format(_ENDPOINT, _PRODUCTS)
        payload = {
            'api_key': self._api_key,
            'page': page,
        }
        return self._make_request(url=url, payload=payload)

    def _make_request(self, url: str, payload: dict) -> dict:
        """
        Make a request
        :param str url: Url to call
        :param dict payload: Payload to call
        :return dict: Response as dict
        """
        payload['time'] = int(time.time())
        signature = self._make_signature(payload=payload)
        payload['sign'] = signature
        res = requests.get(url, params=payload)

        return res.json()

    def _make_signature(self, payload) -> str:
        """
        Make signature
        :param dict payload: Payload to call
        :return str: signature for call
        """
        signature = ""
        for key in sorted(payload):
            signature = "{}{}{}".format(signature, key, payload[key])

        signature = "{}{}{}".format(self._api_secret, signature, self._api_secret)
        signature = md5(signature.encode('utf-8')).hexdigest()
        signature = signature.upper()

        return signature

