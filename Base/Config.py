# /usr/bin/env python
# -*- encoding: utf-8 -*-
import random

class Config:
    # apk包名
    package_name = "com.huawei.hwireader"
    # 默认设备列表
    device_dict = {}
    # 网络
    net = "wifi"
    # monkey seed值，随机产生
    monkey_seed = str(random.randrange(1000, 9999))
    # monkey 参数
    monkey_parameters = "--throttle 200 --ignore-crashes --ignore-timeouts --pct-touch 80 --pct-trackball 5 --pct-appswitch 5 --pct-syskeys 5 --pct-motion 5 -v -v 10000"
    # log保存地址
    log_location = "D:\\log\\monkey_log\\log\\"
    #性能数据存储目录
    info_path = "D:\\git\\monkeyTest-master\\info\\"

# "adb shell monkey -p com.quvideo.xiaoying --throttle 300 --ignore-crashes --ignore-timeouts --pct-touch 80 --pct-trackball 5 --pct-appswitch 5 --pct-syskeys 5 --pct-motion 5 -v -v 30000"

