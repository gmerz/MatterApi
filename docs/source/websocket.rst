Websocket Handler
^^^^^^^^^^^^^^^^^^

Additionally to accessing the API, this library also includes a websocket listener
to react to events in Mattermost. 

The websocket handling is part of :doc:`client/base_client`. The functionality is the same, no matter if you use
the sync or the async client.


.. code-block:: python

    from matterapi import SyncClient
    
    # set the options for the client
    options = { 'url' : 'http://localhost:8095',
        'auth' : { 
          'token' : '<yourtokenhere>' 
          }
    }
    
    # Create a sync client
    sd = SyncClient(options=options)
    # You can use either a function or a coroutine here. Both are supported equally
    async def handler(message):
        print(message)
    # Start handling messages and block
    sd.start_ws_sync(handler)


.. code-block:: python

    import asyncio
    from matterapi import AsyncClient
    
    # set the options for the client
    options = { 'url' : 'https://localhost:8095',
        # User username and password authentication
        'auth' : { 
          'login_id' : 'hansolo', 
          'password' : 'lea1234' 
          }
    }
    
    # Create a async client
    ad = AsyncClient(options=options)
    
    # You can use either a function or a coroutine here. Both are supported equally
    def handler(message):
        print(message)

    async def do_something():
        # Call login to:
        # 1. Get a session token if you user user:password based auth
        # 2. Populate the client with the corresponding user object
        await ad.users.get_user("me")
    
        # Handle messages, Call login() again on websocket failures
        await ad.start_ws(handler, relogin=True)

    asyncio.run(do_something())


As can be seen in the example above, the websocket handler can work with functions and coroutines. You can also call ``start_ws_sync`` from the ``AsyncClient`` and vice versa.
