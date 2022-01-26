Getting Started
-----------------------

These are the first steps on how to get started with this library

.. seealso :: To get more information on available endpoints take a look at :doc:`/endpoints` or at the `Mattermost API Reference <https://api.mattermost.com/>`_.

For additional options also take a look at :class:`matterapi.client.base.ClientOptions`.

SyncClient
^^^^^^^^^^

First, let's look at an example on how to use the :doc:`client/sync_client`:

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
    
    # Use the client
    sd.users.get_user("me")
 

AsyncClient
^^^^^^^^^^^

And this is how you can use the :doc:`client/async_client`:


.. code-block:: python

    import asyncio
    from matterapi import AsyncClient
    
    # set the options for the client
    options = { 'url' : 'https://localhost:8095',
        # User username and password authentication
        'auth' : { 
          'login_id' : 'hansolo', 
          'password' : 'lea1234' 
          },
        # Disable TLS verification for the client
        'client_options' : {
          'verify' : False
        }
    }
    
    # Create a async client
    ad = AsyncClient(options=options)
    
    async def do_something():
      
      # Use the client
      users = await ad.users.get_users()
      print(users)
    
      # To upload files, you could for example use the following request
      data = {
              "files": {
                  "test1.png": open("testfile1.png", "rb"),
                  "test2.png": open("testfile2.png", "rb"),
              }
          }
    
      file_infos = await ad.files.upload_file(
          channel_id="7bzsijaqopfczygxm1qc3r63do",
          multipart_data=data)
    
      print(file_info)
    
    asyncio.run(do_something())

