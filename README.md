# Thumbor Indexed File Result Storage

This Thumbor result storage plugin indexes the creation time of result storage files
using a Redis ZSET. We use this ZSET to delete files older than a certain time frame,
because `find` performance was too slow for our scale.

The ZSET key is `result_storage_creation_time:HOSTNAME` where HOSTNAME is the result of `hostname` on the Thumbor app server

No additional Thumbor Configuration values are used, as it piggy backs off the Redis settings for `Storage`
