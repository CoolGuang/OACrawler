from model.base_model import BaseModel
from typing import List
from setting.codeforce_settting import CodeForceProFileSetting
from common.const import DEFAULT_TIME, NO_CONTEST


class CodeForceProFileModel(BaseModel):

    SETTING = CodeForceProFileSetting

    def _column_keys(self) -> List[str]:
        return self.SETTING.TYPE_KEYS

    @property
    def avg_contests_rating(self) -> float:
        """
        :return: latest avg contest rating
        """
        avg = 0
        if len(self.late_contests_ratings) == 0:
            return avg
        for item in self.late_contests_ratings:
            avg += int(item[2])
        return avg / len(self.late_contests_ratings)

    @property
    def latest_contest_time(self) -> str:
        """
        :return: latest 1 contest time
        """
        if len(self.late_contests_time) == 0:
            return DEFAULT_TIME
        return self.late_contests_time[0]

    @property
    def latest_contest_name(self) -> str:
        """
        :return: latest 1 contest name
        """
        if len(self.late_contests_name) == 0:
            return NO_CONTEST
        return self.late_contests_name[0]

    @property
    def latest_contest_change(self) -> int:
        """
        :return: latest 1 rating related
        """
        if len(self.late_contests_ratings) == 0:
            return 0
        return self.late_contests_ratings[0][1]

    @property
    def latest_contests_rank(self) -> int:
        """
            最近1场比赛的rank排名
            return type: str
        """
        if len(self.late_contests_ratings) == 0:
            return -1
        return self.late_contests_ratings[0][0]

    @property
    def late_contests_change(self) -> List[int]:
        """
        :return: latest lt 10 contest ratings change
        """
        if len(self.late_contests_ratings) == 0:
            return []
        result = [item[1] for item in self.late_contests_ratings]
        return result

    @property
    def late_contests_ratings(self) -> List[int]:
        """
        :return: latest lt 10 contest ratings
        """
        if len(self.late_contests_ratings) == 0:
            return []
        result = [item[2] for item in self.late_contests_ratings]
        return result

    @property
    def late_contests_rank(self) -> List[int]:
        """
        :return: latest lt 10 contest rank
        """
        if len(self.late_contests_ratings) == 0:
            return []
        result = [item[0] for item in self.late_contests_ratings]
        return result

