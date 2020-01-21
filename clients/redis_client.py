# coding=utf8

import redis

import config as conf

from functools import lru_cache

__all__ = ['get_log_redis_client', 'get_config_redis_client',
           'get_report_redis_client']


@lru_cache(maxsize=24 * 3600)
def get_config_redis_client():
    return redis.StrictRedis(**conf.REDIS_CONFIG)


@lru_cache(maxsize=24 * 3600)
def get_log_redis_client():
    return redis.StrictRedis(**conf.LOG_REDIS_CONFIG)


@lru_cache(maxsize=24 * 3600)
def get_report_redis_client():
    return redis.StrictRedis(**conf.REPORT_REDIS_CONFIG)
