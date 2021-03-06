#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# author wwqgtxx <wwqgtxx@gmail.com>

if __name__ == "__main__":
    import os
    import sys

    _srcdir = os.path.dirname(os.path.realpath(__file__))
    _filepath = os.path.dirname(sys.argv[0])
    sys.path.insert(0, os.path.join(_filepath, _srcdir))

    print(sys.path)
    del sys
    del os

from common import *
from pyquery.pyquery import PyQuery

if __name__ == "__main__":
    from main import *

    main("http://v.yinyuetai.com/video/2796852", parsers_name=["YinYueTaiParser"])
    # main("http://www.mgtv.com/b/316045/4096972.html", types="collection")
    # main("http://www.mgtv.com/b/316045/4096972.html", parsers_name=["MgTVParser"])
    # main("http://www.mgtv.com/b/316045/4096972.html", label="3@MgTVParser")
    # urlcache.timeout = 10
    # main("http://www.iqiyi.com/v_19rrl8pmn8.html", types="list")
    # main("http://www.iqiyi.com/v_19rrl8pmn8.html", types="list")
    # time.sleep(10)
    # main("http://www.iqiyi.com/v_19rrl8pmn8.html", types="list")
    # main("http://www.iqiyi.com/v_19rrl8pmn8.html", parsers_name=["IQiYiMTsParser"])
    # main("http://www.iqiyi.com/v_19rrl8pmn8.html", label="fullhd@IQiYiParser")
    # main("http://www.iqiyi.com/v_19rrl8pmn8.html", parsers_name=["ykdlparser.YKDLParser"])
    # main("http://www.iqiyi.com/v_19rrl8pmn8.html", label="1_BD_1080p_0@YKDLParser")
    # main("http://www.iqiyi.com/v_19rrl8pmn8.html", parsers_name=["yougetparser.YouGetParser"])
    # main("http://www.iqiyi.com/v_19rrl8pmn8.html", label="4_BD_1080p_0@YouGetParser")
    # main("http://www.le.com/ptv/vplay/25047584.html", parsers_name=["LypPvParser"])
    # main("http://www.le.com/ptv/vplay/25047584.html", label="4.0@LypPvParser")
    # main("http://www.le.com/ptv/vplay/25047584.html", parsers_name=["ykdlparser.YKDLParser"], types="formats")
    # main("http://www.le.com/ptv/vplay/25047584.html", label="0_TD_超清_0@YKDLParser")
    # main("http://www.mgtv.com/b/308710/3917451.html", parsers_name=["YouGetParser"])
    # main("http://www.mgtv.com/b/308710/3917451.html", label="2_hd_超清_982.06 MB@YouGetParser")
    # main("http://www.mgtv.com/b/308710/3917451.html", parsers_name=["YKDLParser"])
    # main("http://www.mgtv.com/b/308710/3917451.html", label="1_TD_超清_0@YKDLParser")
    # main("http://www.bilibili.com/video/av3153352/", parsers_name=["YouGetParser"])
    # main("http://www.bilibili.com/video/av3153352/", label="0_default__2.80 MB@YouGetParser")
    # main("http://www.le.com/ptv/vplay/27416375.html", parsers_name=["YouGetParser"])
    # main("http://www.le.com/ptv/vplay/1981824.html", types="list")
    # main("http://www.le.com/ptv/vplay/27416375.html", parsers_name=["LeParser"])
    # main("http://www.le.com/ptv/vplay/27416375.html", label="1080p@LeParser")
    # main("http://v.youku.com/v_show/id_XMjcxMzkwMjU3Mg==.html", types="list")
    # main("http://v.youku.com/v_show/id_XMTYxODUxOTEyNA==.html?f=27502474", parsers_name=["YouGetParser"])
    # main("http://v.youku.com/v_show/id_XMTYxODUxOTEyNA==.html?f=27502474", parsers_name=["YKDLParser"])
    # main("http://v.youku.com/v_show/id_XMTYxODUxOTEyNA==.html?f=27502474", label="3_BD_1080p_2.00 GB@YKDLParser")
    # main("http://v.youku.com/v_show/id_XMzg1ODY1MTIw.html||123", parsers_name=["YouGetParser"])
    # main("http://list.youku.com/albumlist/show/id_2336634.html", types="collection")
    # main("http://v.youku.com/v_show/id_XMTE4NjQ3MjYw.html?spm=a2h1n.8251843.playList.5!4~1!2~3~A&f=2336634&o=0", types="collection")
    # close()
