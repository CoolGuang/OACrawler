import asyncio
import random
from typing import Dict, List
import requests

from ..common.headers import get_random_headers
from ..setting.base_setting import BaseSetting
from ..common.exception import CrawlerParamTypeError


class CrawlerConfig():

    MAX_RETRY_TIME = 3
    TIMEOUT = 10
    BATCH_NUM = 5


class CrawlerBase():

    SETTING = BaseSetting

    def __init__(self, *args, **kwargs):
        self.semaphore = asyncio.Semaphore(4)

    async def _get_request_body(
        self,
        url_key: str,
        directions: List[str] = None,
        query_param: Dict[str, str] = None,
        crawler_config: CrawlerConfig = CrawlerConfig,
        need_cookie=False,
    ) -> str:
        """
        :param url: request url
        :param query_param: query param 
        :param directions: url directions
        :param need_cookie: cookie check
        :param crawler_config: crawler config 
        :return: request body to crawler
        """""
        async with self.semaphore:
            # url
            await asyncio.sleep(round(random.randint(100, 200) / 100.0, 2))
            url = self._get_url(url_key, directions, query_param)

            # config
            retry_time = crawler_config.MAX_RETRY_TIME
            timeout = crawler_config.TIMEOUT

            # get body
            try_time = 0
            response = None

            # headers
            headers = get_random_headers()

            while try_time < retry_time and not response:
                try:
                    response = requests.get(url=url, headers=headers, allow_redirects=False, timeout=timeout)
                except requests.RequestException as e:
                    response = None
                    #todo log print("get request err, code=%s" % e.errno)
                finally:
                    try_time += 1
                await asyncio.sleep(3)

            if not response:
                response.raise_for_status()

            return response.content.decode("utf-8")

    def _get_url(
        self,
        url_key: str,
        directions: List[str],
        query_param: Dict[str, str]
    ) -> str:

        if query_param is None:
            query_param = {}

        if directions is None:
            directions = []

        if not isinstance(query_param, dict) or not isinstance(directions, list):
            raise CrawlerParamTypeError("crawler param error, query_param must be dict, directions must be list")

        url = self.SETTING.URL[url_key]

        if directions:
            if url[-1] == '/':
                url = url[:-1]
            for direction in directions:
                url += "/" + direction

        if query_param:
            url += "?"
            for k, v in query_param.items():
                url += k + "=" + v + "&"
            url = url[:-1]

        return url

