# Thumbor Indexed File Result Storage

This Thumbor result storage plugin indexes the creation time of result storage files
using a Redis ZSET. We use this ZSET to delete files older than a certain time frame,
because `find` performance was too slow for our scale.

Thumbor Configuration values used:

```
```
