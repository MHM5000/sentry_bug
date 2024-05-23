# Sentry Bug


## Steps to reproduce the issue

1. you need redis and sqlite installed on your machine. a usual dev's environment has those!
2. clone this repo.
3. create a new env and install the requirements. i used pipenv and python 3.11 .
4. run `cp .env.example .env` and add a DSN.
5. `./manage.py runserver` .
6. you'll see the error:

```sh
(test_sentry_bug) ➜  test_sentry_bug git:(main) ./manage.py runserver
job <Job something: example_app.tasks.something()>
job <Job something: example_app.tasks.something()>
Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "/Users/mojtahedi/.pyenv/versions/3.11.7/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/sentry_sdk/integrations/threading.py", line 99, in run
    return _run_old_run_func()
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/sentry_sdk/integrations/threading.py", line 94, in _run_old_run_func
    reraise(*_capture_exception())
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/sentry_sdk/utils.py", line 1640, in reraise
    raise value
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/sentry_sdk/integrations/threading.py", line 92, in _run_old_run_func
    return old_run_func(self, *a, **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mojtahedi/.pyenv/versions/3.11.7/lib/python3.11/threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/django/core/management/commands/runserver.py", line 125, in inner_run
    autoreload.raise_last_exception()
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/django/utils/autoreload.py", line 87, in raise_last_exception
    raise _exception[1]
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/django/core/management/__init__.py", line 394, in execute
    autoreload.check_errors(django.setup)()
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/django/apps/registry.py", line 124, in populate
    app_config.ready()
  File "/Users/mojtahedi/sandbox/test_sentry_bug/example_app/apps.py", line 29, in ready
    job.delete()
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/rq/job.py", line 1251, in delete
    connection.delete(self.key, self.dependents_key, self.dependencies_key)
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/redis/commands/core.py", line 1713, in delete
    return self.execute_command("DEL", *names)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/sentry_sdk/integrations/redis/_sync_common.py", line 72, in sentry_patched_execute_command
    cache_properties = _compile_cache_span_properties(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/sentry_sdk/integrations/redis/modules/caches.py", line 32, in _compile_cache_span_properties
    key = _get_safe_key(redis_command, args, kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mojtahedi/.local/share/virtualenvs/test_sentry_bug-gPib43ih/lib/python3.11/site-packages/sentry_sdk/integrations/redis/utils.py", line 56, in _get_safe_key
    key = ", ".join(args)
          ^^^^^^^^^^^^^^^
TypeError: sequence item 0: expected str instance, bytes found
```