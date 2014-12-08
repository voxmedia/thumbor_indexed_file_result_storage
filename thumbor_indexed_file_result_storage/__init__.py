#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2014 voxmedia.com

import time
from redis import Redis, RedisError
from thumbor.result_storages.file_storage import Storage as FileStorage
from subprocess import call

class Storage(FileStorage):

    redis_connection = None
    hostname = None

    def __init__(self, context):
        super(Storage, self).__init__(context)
        self.redis_connection = self.reconnect_redis()
        self.hostname = call(["hostname"])

    def reconnect_redis(self):
      if not Storage.redis_connection:
          Storage.redis_connection = Redis(
              port=self.context.config.REDIS_STORAGE_SERVER_PORT,
              host=self.context.config.REDIS_STORAGE_SERVER_HOST,
              db=self.context.config.REDIS_STORAGE_SERVER_DB,
              password=self.context.config.REDIS_STORAGE_SERVER_PASSWORD
          )
      return Storage.redis_connection

    def put(self, bytes):
        file_abspath = self.normalize_path(self.context.request.url)
        timestamp = float(time.time())
        self.redis_connection.zadd(
            "result_storage_creation_time" + ":" + self.hostname,
            file_abspath,
            timestamp
        )
        super(Storage, self).put(bytes)
