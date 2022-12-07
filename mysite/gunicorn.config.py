### Gunicorn Configuration File ###

timeout = 60
graceful_timeout = 60
limit_request_field_size  = 0
limit_request_line = 0
limit_request_fields = 0
proxy_allow_ips = '*'
workers=3
errorlog='gunicorn-error.log'
accesslog='gunicorn-access.log'
loglevel='debug'
