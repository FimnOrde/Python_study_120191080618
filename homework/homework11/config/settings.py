#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:settings.py.py
# author:jackiex
# datetime:2021/1/26 14:21
# software: PyCharm
'''
   this is function  description
'''
class BaseConfig():
    """通用基础配置"""
    MEDIA_ROOT = "/static/media"

class TestConfig(BaseConfig):
    """测试环境配置"""
    DEBUG = True
    DB = '127.0.0.1'

class DevConfig(BaseConfig):
    """开发环境配置"""
    DEBUG = True
    DB = '192.168.1.1'

class PreProConfig(BaseConfig):
    """预发布环境配置"""
    DEBUG = False
    DB = '47.18.1.10'

class ProConfig(BaseConfig):
    """生产环境配置"""
    DEBUG = False
    DB = '47.18.1.1'
