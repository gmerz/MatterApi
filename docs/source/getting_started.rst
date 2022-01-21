Getting Started
-----------------------

These are the first steps on how to get started with this library

.. seealso :: To get more information on available endpoints take a look at :doc:`/endpoints` or at the `Mattermost API Reference <https://api.mattermost.com/>`_.

For additional options also take a look at :class:`matterapi.driver.base.DriverOptions`.

SyncDriver
^^^^^^^^^^

First, let's look at an example on how to use the :doc:`driver/sync_driver`:

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
    
    # The drivers `user` object will hold information on the current user/bot
    print(sd.user.id)
    
    # Use the driver
    sd.users.get_user("me")
 

AsyncDriver
^^^^^^^^^^^

And this is how you can use the :doc:`driver/async_driver`:


.. code-block:: python

    import asyncio
    from matterapi import AsyncDriver
    
    # set the options for the driver
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
    
    # Create a async driver
    ad = AsyncDriver(options=options)
    
    async def do_something():
      # Call login to:
      # 1. Get a session token if you user user:password based auth
      # 2. Populate the driver with the corresponding user object
      await ad.login()
    
      # Use the driver
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

