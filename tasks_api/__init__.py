from fastapi import FastAPI
from tasks_api.sub_task import views as sub_task_views
from tasks_api.task import views as task_views
from tasks_api.task_list import views as task_list_views
from tasks_api.users import views as user_views


def create_app():
    """
      Construct the core application.
      The whole function can be divided in 3 steps below
          >> Create a fast api app object, which derives configuration values
          (either from a Python class, a config file, or environment variables).
          >> Import the logic which makes up our app (such as routes).
          >> Register routers   .
    """
    # callback to get your configuration
    app = FastAPI(title="Google_tasks", version=" 0.79.0")

    # registering routers
    app.include_router(user_views.router)
    app.include_router(task_list_views.router)
    app.include_router(task_views.router)
    app.include_router(sub_task_views.router)

    # run celery task.
    # from tasks_api.celery_config import celery_app
    # __all__ = (celery_app,)

    return app
