import asyncio
from typing import List, Union

from .crawler.codeforce_crawler import CodeForceProFileCrawler
from .crawler.base_crawler import CrawlerConfig
from .model.base_model import BaseModel
from .model.codeforce_model import CodeForceProFileModel


async def __get_code_force_profile_info_async(
        usernames: List[str],
        crawler_cfg: CrawlerConfig = CrawlerConfig
) -> Union[BaseModel, List[BaseModel]]:
    """
    :param usernames: username list
    :param crawler_cfg: crawler cfg
    :return: a generator include CodeForceProFileModel
    """
    # init

    batch_num = crawler_cfg.BATCH_NUM
    r_flag = 1 if ~batch_num else 0
    batch_num = max(batch_num, 1)
    c = CodeForceProFileCrawler()

    while usernames:
        _usernames, usernames = usernames[:batch_num], usernames[batch_num:]

        gather_fortune = asyncio.gather(
            *[
                c.execute_tasks([username], crawler_cfg=crawler_cfg) for username in _usernames
            ]
        )

        _result = await gather_fortune

        result = []
        for item in _result:
            for kwargs in item:
                result.append(CodeForceProFileModel(**kwargs))

        if r_flag:
            yield result
        else:
            yield result[0]


async def _get_code_force_profile_info_async(
        usernames: List[str],
        crawler_cfg: CrawlerConfig = CrawlerConfig
) -> Union[BaseModel, List[BaseModel]]:

    result = []
    async for item in __get_code_force_profile_info_async(usernames, crawler_cfg=crawler_cfg):
        result.append(item)

    return result


def get_code_force_profile_info(
    usernames: List[str],
    crawler_cfg: CrawlerConfig = CrawlerConfig
) -> BaseModel:
    r = asyncio.run(_get_code_force_profile_info_async(usernames, crawler_cfg=crawler_cfg))
    for r_profile in r:
        for r in r_profile:
            yield r


if __name__ == '__main__':
    # for test
    for item in get_code_force_profile_info(["CCoolGuang"]):
        print(item.username)
        print(item.get_columns_name())
        print(item.get_dict_info())
        print(item.parse_to_text())




