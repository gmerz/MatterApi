""" Module to access the Posts endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from ...models import (
    ChannelUnreadAt,
    CreatePostEphemeralJsonBody,
    CreatePostJsonBody,
    FileInfo,
    PatchPostJsonBody,
    Post,
    PostList,
    PostListWithSearchMatches,
    SearchPostsJsonBody,
    StatusOK,
    UpdatePostJsonBody,
)
from ..base import ApiBaseClass


class PostsApi(ApiBaseClass):
    """Endpoints for creating, getting and interacting with posts."""

    async def create_post(
        self,
        *,
        json_body: Union[CreatePostJsonBody, Dict],
        set_online: Optional[bool] = None,
    ) -> Post:
        """Create a post

        Create a new post in a channel. To create the post as a comment on
        another post, provide `root_id`.

        Permissions:
            Must have `create_post` permission for the channel the post
            is being created in.

        Api Reference:
            `CreatePost <https://api.mattermost.com/#operation/CreatePost>`_
        """

        url = "/posts"
        params: Dict[str, Any] = {
            "set_online": set_online,
        }
        params = {k: v for k, v in params.items() if v is not None}

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
            "params": params,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 201:
            response201 = Post.parse_obj(response.json())

            return response201
        return response

    async def create_post_ephemeral(
        self,
        *,
        json_body: Union[CreatePostEphemeralJsonBody, Dict],
    ) -> Post:
        """Create a ephemeral post

        Create a new ephemeral post in a channel.

        Permissions:
            Must have `create_post_ephemeral` permission (currently only
            given to system admin)

        Api Reference:
            `CreatePostEphemeral <https://api.mattermost.com/#operation/CreatePostEphemeral>`_
        """

        url = "/posts/ephemeral"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 201:
            response201 = Post.parse_obj(response.json())

            return response201
        return response

    async def get_post(
        self,
        post_id: str,
    ) -> Post:
        """Get a post

        Get a single post.

        Permissions:
            Must have `read_channel` permission for the channel the post
            is in or if the channel is public, have the
            `read_public_channels` permission for the team.

        Api Reference:
            `GetPost <https://api.mattermost.com/#operation/GetPost>`_
        """

        url = f"/posts/{post_id}"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = Post.parse_obj(response.json())

            return response200
        return response

    async def update_post(
        self,
        post_id: str,
        *,
        json_body: Union[UpdatePostJsonBody, Dict],
    ) -> Post:
        """Update a post

        Update a post. Only the fields listed below are updatable, omitted
        fields will be treated as blank.

        Permissions:
            Must have `edit_post` permission for the channel the post is
            in.

        Api Reference:
            `UpdatePost <https://api.mattermost.com/#operation/UpdatePost>`_
        """

        url = f"/posts/{post_id}"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.put(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = Post.parse_obj(response.json())

            return response200
        return response

    async def delete_post(
        self,
        post_id: str,
    ) -> StatusOK:
        """Delete a post

        Soft deletes a post, by marking the post as deleted in the database.
        Soft deleted posts will not be returned in post queries.

        Permissions:
            Must be logged in as the user or have `delete_others_posts`
            permission.

        Api Reference:
            `DeletePost <https://api.mattermost.com/#operation/DeletePost>`_
        """

        url = f"/posts/{post_id}"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.delete(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    async def set_post_unread(
        self,
        user_id: str,
        post_id: str,
    ) -> ChannelUnreadAt:
        """Mark as unread from a post.

        Mark a channel as being unread from a given post.
        Must have `edit_other_users` permission if the user is not the one
        marking the post for himself.

        Permissions:
            Must have `read_channel` permission for the channel the post
            is in or if the channel is public, have the
            `read_public_channels` permission for the team.
        Minimum Server Version:
            5.18

        Api Reference:
            `SetPostUnread <https://api.mattermost.com/#operation/SetPostUnread>`_
        """

        url = f"/users/{user_id}/posts/{post_id}/set_unread"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = ChannelUnreadAt.parse_obj(response.json())

            return response200
        return response

    async def patch_post(
        self,
        post_id: str,
        *,
        json_body: Union[PatchPostJsonBody, Dict],
    ) -> Post:
        """Patch a post

        Partially update a post by providing only the fields you want to update.
        Omitted fields will not be updated. The fields that can be updated are
        defined in the request body, all other provided fields will be ignored.

        Permissions:
            Must have the `edit_post` permission.

        Api Reference:
            `PatchPost <https://api.mattermost.com/#operation/PatchPost>`_
        """

        url = f"/posts/{post_id}/patch"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.put(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = Post.parse_obj(response.json())

            return response200
        return response

    async def get_post_thread(
        self,
        post_id: str,
    ) -> PostList:
        """Get a thread

        Get a post and the rest of the posts in the same thread.

        Permissions:
            Must have `read_channel` permission for the channel the post
            is in or if the channel is public, have the
            `read_public_channels` permission for the team.

        Api Reference:
            `GetPostThread <https://api.mattermost.com/#operation/GetPostThread>`_
        """

        url = f"/posts/{post_id}/thread"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = PostList.parse_obj(response.json())

            return response200
        return response

    async def get_flagged_posts_for_user(
        self,
        user_id: str,
        *,
        team_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[PostList]:
        """Get a list of flagged posts

        Get a page of flagged posts of a user provided user id string. Selects
        from a channel, team, or all flagged posts by a user. Will only return
        posts from channels in which the user is member.

        Permissions:
            Must be user or have `manage_system` permission.

        Api Reference:
            `GetFlaggedPostsForUser <https://api.mattermost.com/#operation/GetFlaggedPostsForUser>`_
        """

        url = f"/users/{user_id}/posts/flagged"
        params: Dict[str, Any] = {
            "team_id": team_id,
            "channel_id": channel_id,
            "page": page,
            "per_page": per_page,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = PostList.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_file_infos_for_post(
        self,
        post_id: str,
    ) -> List[FileInfo]:
        """Get file info for post

        Gets a list of file information objects for the files attached to a
        post.

        Permissions:
            Must have `read_channel` permission for the channel the post
            is in.

        Api Reference:
            `GetFileInfosForPost <https://api.mattermost.com/#operation/GetFileInfosForPost>`_
        """

        url = f"/posts/{post_id}/files/info"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = FileInfo.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_posts_for_channel(
        self,
        channel_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
        since: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
    ) -> PostList:
        """Get posts for a channel

        Get a page of posts in a channel. Use the query parameters to modify the
        behaviour of this endpoint. The parameter `since` must not be used with
        any of `before`, `after`, `page`, and `per_page` parameters.
        If `since` is used, it will always return all posts modified since that
        time, ordered by their create time limited till 1000. A caveat with this
        parameter is that there is no guarantee that the returned posts will be
        consecutive. It is left to the clients to maintain state and fill any
        missing holes in the post order.

        Permissions:
            Must have `read_channel` permission for the channel.

        Api Reference:
            `GetPostsForChannel <https://api.mattermost.com/#operation/GetPostsForChannel>`_
        """

        url = f"/channels/{channel_id}/posts"
        params: Dict[str, Any] = {
            "page": page,
            "per_page": per_page,
            "since": since,
            "before": before,
            "after": after,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = PostList.parse_obj(response.json())

            return response200
        return response

    async def get_posts_around_last_unread(
        self,
        user_id: str,
        channel_id: str,
        *,
        limit_before: Optional[int] = 60,
        limit_after: Optional[int] = 60,
        skipFetchThreads: Optional[bool] = False,
        collapsedThreads: Optional[bool] = False,
        collapsedThreadsExtended: Optional[bool] = False,
    ) -> PostList:
        """Get posts around oldest unread

        Get the oldest unread post in the channel for the given user as well as
        the posts around it. The returned list is sorted in descending order
        (most recent post first).

        Permissions:
            Must be logged in as the user or have `edit_other_users`
            permission, and must have `read_channel` permission for the
            channel.
        Minimum Server Version:
            5.14

        Api Reference:
            `GetPostsAroundLastUnread <https://api.mattermost.com/#operation/GetPostsAroundLastUnread>`_
        """

        url = f"/users/{user_id}/channels/{channel_id}/posts/unread"
        params: Dict[str, Any] = {
            "limit_before": limit_before,
            "limit_after": limit_after,
            "skipFetchThreads": skipFetchThreads,
            "collapsedThreads": collapsedThreads,
            "collapsedThreadsExtended": collapsedThreadsExtended,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = PostList.parse_obj(response.json())

            return response200
        return response

    async def search_posts(
        self,
        team_id: str,
        *,
        json_body: Union[SearchPostsJsonBody, Dict],
    ) -> PostListWithSearchMatches:
        """Search for team posts

        Search posts in the team and from the provided terms string.

        Permissions:
            Must be authenticated and have the `view_team` permission.

        Api Reference:
            `SearchPosts <https://api.mattermost.com/#operation/SearchPosts>`_
        """

        url = f"/teams/{team_id}/posts/search"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = PostListWithSearchMatches.parse_obj(response.json())

            return response200
        return response

    async def pin_post(
        self,
        post_id: str,
    ) -> StatusOK:
        """Pin a post to the channel

        Pin a post to a channel it is in based from the provided post id string.

        Permissions:
            Must be authenticated and have the `read_channel` permission
            to the channel the post is in.

        Api Reference:
            `PinPost <https://api.mattermost.com/#operation/PinPost>`_
        """

        url = f"/posts/{post_id}/pin"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    async def unpin_post(
        self,
        post_id: str,
    ) -> StatusOK:
        """Unpin a post to the channel

        Unpin a post to a channel it is in based from the provided post id
        string.

        Permissions:
            Must be authenticated and have the `read_channel` permission
            to the channel the post is in.

        Api Reference:
            `UnpinPost <https://api.mattermost.com/#operation/UnpinPost>`_
        """

        url = f"/posts/{post_id}/unpin"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    async def do_post_action(
        self,
        post_id: str,
        action_id: str,
    ) -> StatusOK:
        """Perform a post action

        Perform a post action, which allows users to interact with integrations
        through posts.

        Permissions:
            Must be authenticated and have the `read_channel` permission
            to the channel the post is in.

        Api Reference:
            `DoPostAction <https://api.mattermost.com/#operation/DoPostAction>`_
        """

        url = f"/posts/{post_id}/actions/{action_id}"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    async def get_posts_by_ids(
        self,
        *,
        json_body: Union[List[str], Dict],
    ) -> List[Post]:
        """Get posts by a list of ids

        Fetch a list of posts based on the provided postIDs

        Permissions:
            Must have `read_channel` permission for the channel the post
            is in or if the channel is public, have the
            `read_public_channels` permission for the team.

        Api Reference:
            `GetPostsByIds <https://api.mattermost.com/#operation/GetPostsByIds>`_
        """

        url = "/posts/ids"
        json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = Post.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response
