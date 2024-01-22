import random

HEADERS = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    },
    {
        "Accept": "text/html",
        "Accept-Language": "en-US,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
        "Connection": "keep-alive",
        "Referer": "http://www.baidu.com/"
    },
    {
        "Accept": "text/html",
        "Accept-Language": "en-US,en;q=0.8",
        "User-Agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Connection": "keep-alive",
        "Referer": "http://www.baidu.com/"
    },
    {
        "Accept": "text/html",
        "Accept-Language": "en-US,en;q=0.8",
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.54",
        "Connection": "keep-alive",
        "Referer": "http://www.baidu.com/"
    }
]


def get_random_headers() -> dict:
    """
        avoid crawler defense
    :return: a header config
    """
    return HEADERS[1]
    # return random.choice(HEADERS)


