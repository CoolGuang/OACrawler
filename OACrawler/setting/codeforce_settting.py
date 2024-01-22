from setting.base_setting import BaseSetting


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
        "late_month_solutions",  # problems solved in last month
        "late_contests_time",  # contest-time in latest 10 contests
        "late_contests_ratings",  # contest change in latest 10 contests format: (rank, change, new_rating)
        "late_contests_name"  # contest-name in latest 10 contests
    ]

    MAP_FRE_KEY = {
        "username": "用户名",
        "max_rating": "最高Rating",
        "current_rating": "当前Rating",
        "solve_problems": "解决题目数量",
        "late_month_solutions": "上个月解决题目数量",
        "late_contests_time": "最近十场比赛时间",
        "late_contests_ratings": "最近10场rating变化",
        "late_contests_name": "最近十场比赛名称",
    }
