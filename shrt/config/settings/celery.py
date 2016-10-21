BROKER URL = 'ampq://guest@localhost//'

CELERY_TIMEZONE = 'Europe/Moscow'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_ROUTES = {
    'shrt.send_email_task': {'queue': 'shrt'}
}