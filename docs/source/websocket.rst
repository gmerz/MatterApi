Websocket Handler
^^^^^^^^^^^^^^^^^^

Additionally to accessing the API, this library also includes a websocket listener
to react to events in Mattermost. 

The websocket stuff is part of :doc:`driver/base_driver`. The functionality is the same, no matter if you use
the sync or the async driver.


.. code-block:: python

    from matterapi import SyncDriver
    
    # set the options for the driver
    options = { 'url' : 'http://localhost:8095',
        'auth' : { 
          'token' : '<yourtokenhere>' 
          }
    }
    
    # Create a sync driver
    sd = SyncDriver(options=options)
    # Call login to:
    # 1. Get a session token if you use user:password based auth
    # 2. Populate the driver with the corresponding user object
    sd.login()
    # You can use either a function or a coroutine here. Both are supported equally
    async def handler(message):
        print(message)
    # Start handling messages and block
    sd.start_ws_sync(handler)


.. code-block:: python

    import asyncio
    from matterapi import AsyncDriver
    
    # set the options for the driver
    options = { 'url' : 'https://localhost:8095',
        # User username and password authentication
        'auth' : { 
          'login_id' : 'hansolo', 
          'password' : 'lea1234' 
          }
    }
    
    # Create a async driver
    ad = AsyncDriver(options=options)
    
    # You can use either a function or a coroutine here. Both are supported equally
    def handler(message):
        print(message)

    async def do_something():
        # Call login to:
        # 1. Get a session token if you user user:password based auth
        # 2. Populate the driver with the corresponding user object
        await ad.login()
    
        # Handle messages, Call login() again on websocket failures
        await ad.start_ws(handler, relogin=True)

    asyncio.run(do_something())


As can be seen in the example above, the websocket handler can work with functions and coroutines. You can also call ``start_ws_sync`` from the ``AsyncDriver`` and vice versa.
