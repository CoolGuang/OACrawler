from setting.base_setting import BaseSettingProtocol, BaseSetting


class CodeForceProFileSetting(BaseSetting):
    """
        return a codeforce crawler profile setting
    """
    URL = {
        "profile": "https://codeforces.com/profile/",
        "contest": "https://codeforces.com/contests/with/"
    }

    TYPE_KEYS = [
        "username",  # username
        "max_rating",  # max rating
        "current_rating",  # cur rating
        "solve_problems",  # problems solved total
        "last_month_solutions"  # problems solved in last month
        "last_contest_time",  # contest-time in latest 10 contests
        "latest_contests_ratings",  # contest change in latest 10 contests format: (rank, change, new_rating)
        "last_contests_name"  # contest-name in latest 10 contests
    ]

    MAP_FRE_KEY = {
        "user_name": "用户名",
        "max_rating": "最高Rating",
        "current_rating": "当前Rating",
        "solve_problems": "解决题目数量",
        "last_month_solutions": "上个月解决题目数量",
        "last_contest_time": "最近十场比赛时间",
        "latest_contests_ratings": "最近10场rating变化",
        "last_contests_name": "最近十场比赛名称",
    }
