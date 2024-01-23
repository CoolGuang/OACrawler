# OACrawer
用于爬取竞赛 &amp; 刷题网站信息

# 安装方法
```python
pip install OACrawler
```

# 使用方法
```python
from OACrawler import get_code_force_profile_info


if __name__ == '__main__':
    for item in get_code_force_profile_info(usernames=["CCoolGuang"], crawler_cfg=MyCrawlerCfg):
        print(item)
```

# 高级用法(可以指定参数配置)

```python
from OACrawler.crawler.base_crawler import CrawlerConfig
from OACrawler import get_code_force_profile_info


class MyCrawlerCfg(CrawlerConfig):
    BATCH_NUM = 5  # 异步批量的块大小


if __name__ == '__main__':
    for item in get_code_force_profile_info(usernames=["CCoolGuang"], crawler_cfg=MyCrawlerCfg):
        print(item)
```

# 函数映射功能 table
| 函数名称 | 功能 | 参数列表 | 返回值 |
| -------- | -------- | -------- | -------- |
| `get_code_force_profile_info`  | 获取 `codeforce` 个人信息（支持批量）  | `usernames`[用户名列表], 爬取配置  | `profileinfo model`的列表

