import pytest

from unittest.mock import Mock
from datetime import date, timedelta

from gearbest_api import GearbestApi

API_KEY = 1234567
API_SECRET = "secret"


class TestGearbestApi(object):

    @pytest.fixture()
    def gearbest_api(self):
        gearbest_api = GearbestApi(api_key=API_KEY, api_secret=API_SECRET)
        return gearbest_api

    def test_get_completed_orders(self, gearbest_api):
        start_date = str(date.today() - timedelta(days=2))
        end_date = str(date.today() - timedelta(days=1))
        page = 1
        gearbest_api._make_request = Mock()
        gearbest_api.get_completed_orders(start_date=start_date, end_date=end_date, page=page)
        gearbest_api._make_request.assert_called_with(payload={
            'api_key': API_KEY,
            'end_date': end_date,
            'page': page,
            'start_date': start_date,
        }, url='https://affiliate.gearbest.com/api/orders/completed-orders')

    def test_get_list_promotion_product(self, gearbest_api):
        category = 11239
        country_website = 'IT'
        currency = 'EUR'
        keywords = 'test'
        lkid = 47464241
        page = 1
        gearbest_api._make_request = Mock()
        gearbest_api.get_list_promotion_product(
            category=category, country_website=country_website, currency=currency, keywords=keywords, lkid=lkid,
            page=page)
        gearbest_api._make_request.assert_called_with(payload={
            'api_key': API_KEY,
            'category': category,
            'country_website': country_website,
            'currency': currency,
            'keywords': keywords,
            'lkid': lkid,
            'page': page
        }, url='https://affiliate.gearbest.com/api/products/list-promotion-products')

    def test_get_list_event_creative(self, gearbest_api):
        category = 11239
        type = 1
        language = 'EN'
        size = '10*22'
        lkid = 47464241
        page = 1
        gearbest_api._make_request = Mock()
        gearbest_api.get_list_event_creative(
            type=type, category=category, language=language, size=size, lkid=lkid, page=page)
        gearbest_api._make_request.assert_called_with(payload={
            'api_key': API_KEY,
            'category': category,
            'language': language,
            'lkid': lkid,
            'page': page,
            'size': size,
            'type': type
        }, url='https://affiliate.gearbest.com/api/banner/list-event-creative')

    def test_get_list_product_creative(self, gearbest_api):
        category = 11239
        type = 1
        lkid = 47464241
        page = 1
        gearbest_api._make_request = Mock()
        gearbest_api.get_list_product_creative(
            type=type, category=category, lkid=lkid, page=page)
        gearbest_api._make_request.assert_called_with(payload={
            'api_key': API_KEY,
            'type': type,
            'category': category,
            'lkid': lkid,
            'page': page
        }, url='https://affiliate.gearbest.com/api/promotions/list-product-creative')

    def test_get_list_coupons(self, gearbest_api):
        category = 11239
        language = 'EN'
        lkid = 47464241
        page = 1
        gearbest_api._make_request = Mock()
        gearbest_api.get_list_coupons(category=category, language=language, lkid=lkid, page=page)
        gearbest_api._make_request.assert_called_with(payload={
            'api_key': API_KEY,
            'category': category,
            'language': language,
            'lkid': lkid,
            'page': page
        }, url='https://affiliate.gearbest.com/api/coupon/list-coupons')

    # def test_get_promotion_links(self, gearbest_api):
    #     associate_id = 10109867
    #     link_names = 'tests'
    #     urls = ['www.test.test', 'www.test2.test']
    #     promotion_links = gearbest_api.get_promotion_links(
    #         associate_id=associate_id, link_names=link_names, urls=urls)
    #     assert promotion_links.get('error_no') == 0

    def test_get_app_exclusive_price_product(self, gearbest_api):
        page = 1
        gearbest_api._make_request = Mock()
        gearbest_api.get_app_exclusive_price_product(page=page)
        gearbest_api._make_request.assert_called_with(payload={
            'api_key': API_KEY,
            'page': page
        }, url='https://affiliate.gearbest.com/api/products/get-app-exclusive-price-product')
