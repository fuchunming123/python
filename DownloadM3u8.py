# -*- coding: utf-8 -*-
import random

#IP池管理器
import urllib

from IpProxyUtils import IpProxyUtils


if __name__ == '__main__':
    my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
                "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
                ];

    randdom_header=random.choice(my_headers)
    url = "http://hknm5s6gzvm5a6wju24.exp.bcevod.com/mda-iemdar0hsxkzfxv9/mda-iemdar0hsxkzfxv9.m3u8"
    req = urllib.request.Request(url)
    req.add_header("User-Agent",randdom_header)
    req.add_header("Host","hknm5s6gzvm5a6wju24.exp.bcevod.com")
    req.add_header("Origin","http://1s1k.eduyun.cn")
    req.add_header("Referer","http://1s1k.eduyun.cn/")
    req.add_header("GET",url)
    content=urllib.request.urlopen(req).read()
    print(content);