Load Test
==============================================================================
This folder include a single machine, 1000+ concurrent request load test, powered by Locust, a high performance Python load test framework.

**Run load test in CLI**:

.. code-block:: bash

    locust -f locustfile_slow.py --headless --users 100 --spawn-rate 10 --stop-timeout 10

Explain:

- ``-f``: the locustfile location
- ``--headless``: no GUI, CLI only
- ``--users``: number of users you want to simulate
- ``--spawn-rate``: spawn n users per sec
- ``--stop-timeout``: when hit Ctrl + C to stop, give those on-the-fly request sometime to finish


Concepts
------------------------------------------------------------------------------
- ``coroutine``: the backbone of high concurrent. single thread, single core, but high concurrent, non-block, async, event driven.
- ``User``: represent a user
- ``task``: user's action
- ``request_meta``: metadata about the request / response
- ``event listener``: main Locust event
- ``client``


Reference
------------------------------------------------------------------------------
- Locust: https://locust.io/