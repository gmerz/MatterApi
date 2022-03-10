[![Readthedocs](https://readthedocs.org/projects/matterapi/badge/?version=latest)](https://matterapi.readthedocs.io/en/latest/)
[![PyPI version](https://img.shields.io/pypi/v/matterapi)](https://pypi.org/project/matterapi/)

# MatterApi

A python client library for the Mattermost API with sync/async support.


## Features
+ Endpoints generated from the [API documentation](https://api.mattermost.com/)
  - However: if the description is wrong, this library will be wrong
+ Based on [httpx](https://www.python-httpx.org/) and supports sync and async operation
+ Response parsing into models with [pydantic](https://pydantic-docs.helpmanual.io/)
+ Typing support
+ Websocket handling to connect to the Mattermost event stream.

## Getting Started

The client has synch and async support. Depending on your workflow you will want to choose between
the `SyncClient` and `AsyncClient`.


### SyncClient

First, let's look at an example on how to use the SyncClient:

```python
from matterapi import SyncClient
from matterapi.client.exceptions import ApiError, InvalidOrMissingParameters
from matterapi.models import (
    CreateChannelJsonBody,
    CreatePostJsonBody,
    CreateTeamJsonBody,
    CreateUserJsonBody,
)

# set the options for the client
options = { 'url' : 'http://localhost:8095',
    'auth' : { 
      'token' : '<yourtokenhere>' 
      }
}

# Create a sync client
sd = SyncClient(options=options)

# Use the client
""" You can use the client directly. This will create a new httpx.Client for each
request (an potentially run the login flow again, if you use username/password authentication).
"""

## Get your own user object
sd.users.get_user("me")

## Get channels
channels = sd.channels.get_all_channels(per_page=20)
print(channels[0])

## Get posts for channel
post_list = sd.posts.get_posts_for_channel("<channel_id>")
for post in post_list.posts:
  print(post, post_list.posts[post].id)


""" Or you can open a session, which will reuse a single httpx client instance
for the requests, thereby reusing connections ( the login flow is then only run once).
The returned object can be used exactly the same as the SyncClient.
Most often you will want to use this as it requires fewer connections to the server
"""

with sd.session() as api_session:
    # Get the current user
    user = api_session.users.get_user("me")
    print("User id:", user.id)

    # Get a list of plugins
    plugins_avail = api_session.plugins.get_plugins()
    print("Number of active plugins:", len(plugins_avail.active))
    print("Name of first active plugin:", plugins_avail.active[0].name)

    # Create a new Team or get existing
    new_team = CreateTeamJsonBody(name="rebels", display_name="Rebels", type="I")
    try:
        team = api_session.teams.create_team(json_body=new_team)
        print("New Team created with id:", team.id)
    except InvalidOrMissingParameters as e:
        print("> Exception:", e)
        team = api_session.teams.get_team_by_name(name=new_team.name)
        print("Got existing Team with id:", team.id)

    # Create a channel or get existing
    new_channel = CreateChannelJsonBody(
        team_id=team.id, name="newchannelname", display_name="New Channel", type="O"
    )
    try:
        channel = api_session.channels.create_channel(json_body=new_channel)
        print(f"New Channel with id:", channel.id)
    except InvalidOrMissingParameters as e:
        print("> Exception:", e)
        channel = api_session.channels.get_channel_by_name(
            team_id=team.id, channel_name=new_channel.name
        )
        print(f"Got existing Channel with id:", channel.id)

    # Upload files to be used in a channel
    file_info = api_session.files.upload_file(
        channel_id=channel.id,
        multipart_data={
            "files": {
                "upload1.png": open("testfile1.png", "rb"),
                "upload2.png": open("testfile2.png", "rb"),
            },
        },
    )
    print("File id for second file:", file_info.file_infos[1].id)
    
    # Create a post including the uploaded files
    new_post = CreatePostJsonBody(
        channel_id=channel.id,
        message="A wild message appears",
        file_ids=[info.id for info in file_info.file_infos],
    )
    post = api_session.posts.create_post(json_body=new_post)
    print("Creation time for new post:", post.create_at)
```

### AsyncClient

And this is how you can use the AsyncClient

```python

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
    # httpx_client_options are passed to the underlying httpx.Client
    'httpx_client_options' : {
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
```

The AsyncClient supports sessions as well, same as the SyncClient.

## Websocket connection

You can also listen for event data from Mattermost

```python

def handler(message):
  print(message)

# either use the sync version
sd.start_ws_sync(handler)

# or the async version with 
async def wrapper():
  await ad.start_ws(handler)

```


Contributing
------------

The actual endpoints in Matterapi are autogenerated with a fork of [openapi-python-client](https://github.com/gmerz/openapi-python-client). If anything there needs changing, please refer to the generator project.

Some endpoints might return wrong results or miss parameters. Currently, I can image the following reasons:

1. The generator is broken and/or does not support the required feature set.
    - Create an issue in the [matterapi-generator](https://github.com/gmerz/matterapi-generator) repository
    - If you know how to fix it, consider to do a pull request

2. The [mattermost api documentation](https://github.com/mattermost/mattermost-api-reference), which this client is generated from, is not correct
    - Sometimes entries in the documentation might not be completely correct
    - Consider fixing the API documentation/do a pull request/post an issue there
    - This will help everybody who is using the documentation

3. The API documentation changed or included new endpoints, but the library was not updated.
    - Currently creation of the api client is not automated, so you have two options:
        1. Help with the automation so that this proejct is automatically updated with changes
        2. Create a new issue here that the client is out of sync
        3. Clone the generator repo, update the mattermost api with the generator and do a pull request here. (This is currently the only save way to get changes into the matterapi folder)


Credits
-------

Credits where credits are due:

+ This library is autogenerated from the Mattermost API documentation using a fork of [openapi-python-client](https://github.com/triaxtec/openapi-python-client). 
+ It's heavily inspired by (but not a 1:1 drop-in replacement for) [mattermostdriver](https://github.com/Vaelor/python-mattermost-driver), which I used for several years already. This is still your go-to if you look for something stable that has been in use for years by lot's of people.

