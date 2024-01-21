import asyncio
import os
os.path.join("../*")
from typing import List, Union
from crawler.codeforce_crawler import CodeForceProFileCrawler
from crawler.base_crawler import CrawlerConfig
from model.base_model import BaseModel
from model.codeforce_model import CodeForceProFileModel


async def _get_code_force_profile_info(
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
                c.execute_tasks(username, crawler_cfg=crawler_cfg) for username in _usernames
            ]
        )

        _result = await gather_fortune

        result = []
        for kwargs in _result:
            result.append(CodeForceProFileModel(**kwargs))

        if r_flag:
            yield result
        else:
            yield result[0]


def get_code_force_profile_info(
        usernames: List[str],
        crawler_cfg: CrawlerConfig = CrawlerConfig
) -> Union[BaseModel, List[BaseModel]]:

    yield asyncio.run(_get_code_force_profile_info(usernames))


if __name__ == '__main__':

    for item in get_code_force_profile_info(["CCoolGuang", "CCoolGuang", "CCoolGuang"]):
        async for t in item:
            print(t)




