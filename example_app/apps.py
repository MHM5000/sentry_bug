from datetime import datetime

import django_rq
from django.apps import AppConfig
from rq.exceptions import NoSuchJobError
from rq.job import Job

from example_app.defaults import JOB_ID
from example_app.tasks import something


class ExampleAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "example_app"

    def ready(self) -> None:
        scheduler = django_rq.get_scheduler()

        job = scheduler.schedule(
            scheduled_time=datetime.now(),
            func=something,
            id=JOB_ID,
            interval=10 * 60,
        )
        print("job", job)

        connection = django_rq.get_connection()

        job = Job.fetch(JOB_ID, connection=connection)
        job.delete()
