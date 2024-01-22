import asyncio
import datetime
from typing import Dict, List, Union
from crawler.base_crawler import CrawlerBase, CrawlerConfig
from setting.codeforce_settting import CodeForceProFileSetting
from bs4 import BeautifulSoup
from common.const import KEY_PROFILE, KEY_CONTEST


class CodeForceProFileCrawler(CrawlerBase):

    SETTING = CodeForceProFileSetting

    @staticmethod
    async def _parse_profile_info(
        body: str,
    ) -> Dict[str, Union[str, int, float]]:
        """
        :param body: request body
        :return: callback result
        """

        soup = BeautifulSoup(markup=body, features="lxml")

        current_rating = int(soup.select_one("div.info>ul>li>span").string)
        max_rating = int(soup.select("div.info>ul>li>span.smaller>span")[1].string)
        problems_set = soup.select("div._UserActivityFrame_footer>div>div."
                                   "_UserActivityFrame_counter>div._UserActivityFrame_counterValue")
        last_month_solutions = int(problems_set[2].string.split(" ")[0])
        solve_problems = int(problems_set[0].string.split(" ")[0])

        return {
            "max_rating": max_rating,
            "current_rating": current_rating,
            "late_month_solutions": last_month_solutions,
            "solve_problems": solve_problems
        }

    @staticmethod
    async def _parse_contest_info(
        body: str,
    ) -> Dict[str, Union[str, int, float]]:
        """
        :param body: request body
        :return: callback result
        """
        soup = BeautifulSoup(markup=body, features="lxml")
        result_set = soup.select("div.datatable>div>table>tbody>tr")

        last_contests_name = []
        latest_contests_ratings = []
        last_contest_time = []
        if len(result_set) > 10:
            result_set = result_set[:10]

        for item in result_set:
            contests = item.select("td")

            c_t = lambda x: int(x[1:]) if x[0] == '+' else -int(x[1:])
            rating_t = (
                int(contests[3].string),
                c_t(contests[5].select_one("span").string),
                int(contests[6].string.strip('\r\n '))
            )
            latest_contests_ratings.append(rating_t)

            last_contest_time.append(datetime.datetime.strptime(contests[2].text.strip('\r\n '), "%b/%d/%Y %H:%M"))

            last_contests_name.append(contests[1].select_one("a").string.strip('\r\n '))

        return {
            "late_contests_name": last_contests_name,
            "late_contests_ratings": latest_contests_ratings,
            "late_contests_time": last_contest_time
        }

    async def execute_task(
        self,
        username: str,
        crawler_cfg: CrawlerConfig = CrawlerConfig
    ) -> Dict:
        """
        :param crawler_cfg: crawler info config
        :param username: username
        :return: a dict exclude [key, value] document in codeforce_setting.py
        """
        gather_fortune = asyncio.gather(
            *[
                self._get_request_body(url_key=KEY_PROFILE, directions=[username], crawler_config=crawler_cfg),
                self._get_request_body(url_key=KEY_CONTEST, directions=[username], crawler_config=crawler_cfg),
            ]
        )

        body_profile, body_contest = await gather_fortune

        gather_fortune = asyncio.gather(
            *[
                self._parse_contest_info(body=body_contest),
                self._parse_profile_info(body=body_profile)
            ]
        )

        result_list = await gather_fortune

        result = {"username": username}
        for _result in result_list:
            result.update(_result)

        return result

    async def execute_tasks(
        self,
        usernames: List[str],
        crawler_cfg: CrawlerConfig = CrawlerConfig
    ):
        """
        :param usernames: username list
        :param crawler_cfg: crawler cfg
        :return: list of [a dict exclude [key, value] document in codeforce_setting.py]
        """
        gather_fortune = asyncio.gather(
            *[self.execute_task(username, crawler_cfg=crawler_cfg) for username in usernames]
        )
        result_list = await gather_fortune

        return result_list
