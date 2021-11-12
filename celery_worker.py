# import os
# from app import create_app, celery
# from celery import Celery, Task
# from flask import g
#
# import config
#
#
# app = create_app()
# app.app_context().push()
#
#
# def make_celery(app):
#
#     celery = Celery(app.import_name, broker=config.CELERY_BROKER_URL, backend=config.RESULT_BACKEND, include=['scripts.scripts'])
#     celery.conf.update(app.config)
#
#     class ContextTask(Task):
#         abstract = True
#
#         def __call__(self, *args, **kwargs):
#             with app.test_request_context():
#                 g.in_celery_task = True
#                 res = self.run(*args, **kwargs)
#                 return res
#
#     celery.Task = ContextTask
#     return celery
#
#
# celery = make_celery(app)

from celery import Celery

import config


celery_app = Celery('flask_project',
                    broker=config.CELERY_BROKER_URL,
                    backend=config.RESULT_BACKEND,
                    include=['scripts.scripts'])


if __name__ == '__main__':
    celery_app.start()
