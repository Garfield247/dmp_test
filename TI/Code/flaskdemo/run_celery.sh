celery -A manage:celery_app worker  -l info -P gevent -c 10
