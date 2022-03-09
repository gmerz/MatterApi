""" Module to access the Channels endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Any, Dict, List, Optional, Union, cast

from pydantic import BaseModel

from ...models import (
    AddChannelMemberJsonBody,
    Channel,
    ChannelListWithTeamData,
    ChannelMember,
    ChannelModeration,
    ChannelModerationPatch,
    ChannelNotifyProps,
    ChannelStats,
    ChannelUnread,
    CreateChannelJsonBody,
    MoveChannelJsonBody,
    OrderedSidebarCategories,
    PatchChannelJsonBody,
    PostList,
    SearchAllChannelsJsonBody,
    SearchAllChannelsResponse200,
    SearchArchivedChannelsJsonBody,
    SearchChannelsJsonBody,
    SearchGroupChannelsJsonBody,
    SidebarCategory,
    StatusOK,
    UpdateChannelJsonBody,
    UpdateChannelMemberSchemeRolesJsonBody,
    UpdateChannelPrivacyJsonBody,
    UpdateChannelRolesJsonBody,
    UpdateChannelSchemeJsonBody,
    ViewChannelJsonBody,
    ViewChannelResponse200,
)
from ..base import ApiBaseClass


class ChannelsApi(ApiBaseClass):
    """Endpoints for creating, getting and interacting with channels."""

    async def get_all_channels(
        self,
        *,
        not_associated_to_group: Optional[str] = None,
        page: Optional[int] = 0,
        per_page: Optional[int] = 0,
        exclude_default_channels: Optional[bool] = False,
        include_deleted: Optional[bool] = False,
        include_total_count: Optional[bool] = False,
        exclude_policy_constrained: Optional[bool] = False,
    ) -> ChannelListWithTeamData:
        """Get a list of all channels



        Permissions:
            `manage_system`

        Api Reference:
            `GetAllChannels <https://api.mattermost.com/#operation/GetAllChannels>`_
        """

        url = "/channels"
        params: Dict[str, Any] = {
            "not_associated_to_group": not_associated_to_group,
            "page": page,
            "per_page": per_page,
            "exclude_default_channels": exclude_default_channels,
            "include_deleted": include_deleted,
            "include_total_count": include_total_count,
            "exclude_policy_constrained": exclude_policy_constrained,
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
            response200 = ChannelListWithTeamData.parse_obj(response.json())

            return response200
        return response

    async def create_channel(
        self,
        *,
        json_body: Union[CreateChannelJsonBody, Dict],
    ) -> Channel:
        """Create a channel

        Create a new channel.

        Permissions:
            If creating a public channel, `create_public_channel`
            permission is required. If creating a private channel,
            `create_private_channel` permission is required.

        Api Reference:
            `CreateChannel <https://api.mattermost.com/#operation/CreateChannel>`_
        """

        url = "/channels"

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
            response201 = Channel.parse_obj(response.json())

            return response201
        return response

    async def create_direct_channel(
        self,
        *,
        json_body: Union[List[str], Dict],
    ) -> Channel:
        """Create a direct message channel

        Create a new direct message channel between two users.

        Permissions:
            Must be one of the two users and have
            `create_direct_channel` permission. Having the
            `manage_system` permission voids the previous requirements.

        Api Reference:
            `CreateDirectChannel <https://api.mattermost.com/#operation/CreateDirectChannel>`_
        """

        url = "/channels/direct"
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
            response201 = Channel.parse_obj(response.json())

            return response201
        return response

    async def create_group_channel(
        self,
        *,
        json_body: Union[List[str], Dict],
    ) -> Channel:
        """Create a group message channel

        Create a new group message channel to group of users. If the logged in
        user's id is not included in the list, it will be appended to the end.

        Permissions:
            Must have `create_group_channel` permission.

        Api Reference:
            `CreateGroupChannel <https://api.mattermost.com/#operation/CreateGroupChannel>`_
        """

        url = "/channels/group"
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
            response201 = Channel.parse_obj(response.json())

            return response201
        return response

    async def search_all_channels(
        self,
        *,
        json_body: Union[SearchAllChannelsJsonBody, Dict],
        system_console: Optional[bool] = True,
    ) -> SearchAllChannelsResponse200:
        """Search all private and open type channels across all teams

        Returns all private and open type channels where 'term' matches on the
        name, display name, or purpose of
        the channel.

        Configured 'default' channels (ex Town Square and Off-Topic) can be
        excluded from the results
        with the `exclude_default_channels` boolean parameter.

        Channels that are associated (via GroupChannel records) to a given group
        can be excluded from the results
        with the `not_associated_to_group` parameter and a group id string.

        Api Reference:
            `SearchAllChannels <https://api.mattermost.com/#operation/SearchAllChannels>`_
        """

        url = "/channels/search"
        params: Dict[str, Any] = {
            "system_console": system_console,
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

        if response.status_code == 200:
            response200 = SearchAllChannelsResponse200.parse_obj(response.json())

            return response200
        return response

    async def search_group_channels(
        self,
        *,
        json_body: Union[SearchGroupChannelsJsonBody, Dict],
    ) -> List[Channel]:
        """Search Group Channels

        Get a list of group channels for a user which members' usernames match
        the search term.

        Minimum Server Version:
            5.14

        Api Reference:
            `SearchGroupChannels <https://api.mattermost.com/#operation/SearchGroupChannels>`_
        """

        url = "/channels/group/search"

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
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = Channel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_public_channels_by_ids_for_team(
        self,
        team_id: str,
        *,
        json_body: Union[List[str], Dict],
    ) -> List[Channel]:
        """Get a list of channels by ids

        Get a list of public channels on a team by id.

        Permissions:
            `view_team` for the team the channels are on.

        Api Reference:
            `GetPublicChannelsByIdsForTeam <https://api.mattermost.com/#operation/GetPublicChannelsByIdsForTeam>`_
        """

        url = f"/teams/{team_id}/channels/ids"
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
                response200_item = Channel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_channel_members_timezones(
        self,
        channel_id: str,
    ) -> List[str]:
        """Get timezones in a channel

        Get a list of timezones for the users who are in this channel.

        Permissions:
            Must have the `read_channel` permission.
        Minimum Server Version:
            5.6

        Api Reference:
            `GetChannelMembersTimezones <https://api.mattermost.com/#operation/GetChannelMembersTimezones>`_
        """

        url = f"/channels/{channel_id}/timezones"

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
            response200 = cast(List[str], response.json())

            return response200
        return response

    async def get_channel(
        self,
        channel_id: str,
    ) -> Channel:
        """Get a channel

        Get channel from the provided channel id string.

        Permissions:
            `read_channel` permission for the channel.

        Api Reference:
            `GetChannel <https://api.mattermost.com/#operation/GetChannel>`_
        """

        url = f"/channels/{channel_id}"

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
            response200 = Channel.parse_obj(response.json())

            return response200
        return response

    async def update_channel(
        self,
        channel_id: str,
        *,
        json_body: Union[UpdateChannelJsonBody, Dict],
    ) -> Channel:
        """Update a channel

        Update a channel. The fields that can be updated are listed as
        parameters. Omitted fields will be treated as blanks.

        Permissions:
            If updating a public channel,
            `manage_public_channel_members` permission is required. If
            updating a private channel, `manage_private_channel_members`
            permission is required.

        Api Reference:
            `UpdateChannel <https://api.mattermost.com/#operation/UpdateChannel>`_
        """

        url = f"/channels/{channel_id}"

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
            response200 = Channel.parse_obj(response.json())

            return response200
        return response

    async def delete_channel(
        self,
        channel_id: str,
    ) -> StatusOK:
        """Delete a channel

        Archives a channel. This will set the `deleteAt` to the current
        timestamp in the database. Soft deleted channels may not be accessible
        in the user interface. They can be viewed and unarchived in the **System
        Console > User Management > Channels** based on your license. Direct and
        group message channels cannot be deleted.

        As of server version 5.28, optionally use the `permanent=true` query
        parameter to permanently delete the channel for compliance reasons. To
        use this feature `ServiceSettings.EnableAPIChannelDeletion` must be set
        to `true` in the server's configuration.  If you permanently delete a
        channel this action is not recoverable outside of a database backup.

        `delete_private_channel` permission if the channel is private,
        or have `manage_system` permission.

        Permissions:
            `delete_public_channel` permission if the channel is public,

        Api Reference:
            `DeleteChannel <https://api.mattermost.com/#operation/DeleteChannel>`_
        """

        url = f"/channels/{channel_id}"

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

    async def patch_channel(
        self,
        channel_id: str,
        *,
        json_body: Union[PatchChannelJsonBody, Dict],
    ) -> Channel:
        """Patch a channel

        Partially update a channel by providing only the fields you want to
        update. Omitted fields will not be updated. The fields that can be
        updated are defined in the request body, all other provided fields will
        be ignored.

        Permissions:
            If updating a public channel,
            `manage_public_channel_members` permission is required. If
            updating a private channel, `manage_private_channel_members`
            permission is required.

        Api Reference:
            `PatchChannel <https://api.mattermost.com/#operation/PatchChannel>`_
        """

        url = f"/channels/{channel_id}/patch"

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
            response200 = Channel.parse_obj(response.json())

            return response200
        return response

    async def update_channel_privacy(
        self,
        channel_id: str,
        *,
        json_body: Union[UpdateChannelPrivacyJsonBody, Dict],
    ) -> Channel:
        """Update channel's privacy

        Updates channel's privacy allowing changing a channel from Public to
        Private and back.

        Permissions:
            `manage_team` permission for the channels team on version <
            5.28. `convert_public_channel_to_private` permission for the
            channel if updating privacy to 'P' on version >= 5.28.
            `convert_private_channel_to_public` permission for the
            channel if updating privacy to 'O' on version >= 5.28.
        Minimum Server Version:
            5.16

        Api Reference:
            `UpdateChannelPrivacy <https://api.mattermost.com/#operation/UpdateChannelPrivacy>`_
        """

        url = f"/channels/{channel_id}/privacy"

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
            response200 = Channel.parse_obj(response.json())

            return response200
        return response

    async def restore_channel(
        self,
        channel_id: str,
    ) -> Channel:
        """Restore a channel

        Restore channel from the provided channel id string.

        Permissions:
            `manage_team` permission for the team of the channel.
        Minimum Server Version:
            3.10

        Api Reference:
            `RestoreChannel <https://api.mattermost.com/#operation/RestoreChannel>`_
        """

        url = f"/channels/{channel_id}/restore"

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
            response200 = Channel.parse_obj(response.json())

            return response200
        return response

    async def move_channel(
        self,
        channel_id: str,
        *,
        json_body: Union[MoveChannelJsonBody, Dict],
    ) -> Channel:
        """Move a channel

        Move a channel to another team.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `MoveChannel <https://api.mattermost.com/#operation/MoveChannel>`_
        """

        url = f"/channels/{channel_id}/move"

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
            response200 = Channel.parse_obj(response.json())

            return response200
        return response

    async def get_channel_stats(
        self,
        channel_id: str,
    ) -> ChannelStats:
        """Get channel statistics

        Get statistics for a channel.

        Permissions:
            Must have the `read_channel` permission.

        Api Reference:
            `GetChannelStats <https://api.mattermost.com/#operation/GetChannelStats>`_
        """

        url = f"/channels/{channel_id}/stats"

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
            response200 = ChannelStats.parse_obj(response.json())

            return response200
        return response

    async def get_pinned_posts(
        self,
        channel_id: str,
    ) -> PostList:
        """Get a channel's pinned posts

        Get a list of pinned posts for channel.

        Api Reference:
            `GetPinnedPosts <https://api.mattermost.com/#operation/GetPinnedPosts>`_
        """

        url = f"/channels/{channel_id}/pinned"

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

    async def get_public_channels_for_team(
        self,
        team_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Channel]:
        """Get public channels

        Get a page of public channels on a team based on query string parameters
        - page and per_page.

        Permissions:
            Must be authenticated and have the `list_team_channels`
            permission.

        Api Reference:
            `GetPublicChannelsForTeam <https://api.mattermost.com/#operation/GetPublicChannelsForTeam>`_
        """

        url = f"/teams/{team_id}/channels"
        params: Dict[str, Any] = {
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
                response200_item = Channel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_private_channels_for_team(
        self,
        team_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Channel]:
        """Get private channels

        Get a page of private channels on a team based on query string
        parameters - team_id, page and per_page.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `GetPrivateChannelsForTeam <https://api.mattermost.com/#operation/GetPrivateChannelsForTeam>`_
        """

        url = f"/teams/{team_id}/channels/private"
        params: Dict[str, Any] = {
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
                response200_item = Channel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_deleted_channels_for_team(
        self,
        team_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Channel]:
        """Get deleted channels

        Get a page of deleted channels on a team based on query string
        parameters - team_id, page and per_page.

        Minimum Server Version:
            3.10

        Api Reference:
            `GetDeletedChannelsForTeam <https://api.mattermost.com/#operation/GetDeletedChannelsForTeam>`_
        """

        url = f"/teams/{team_id}/channels/deleted"
        params: Dict[str, Any] = {
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
                response200_item = Channel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def autocomplete_channels_for_team(
        self,
        team_id: str,
        *,
        name: str,
    ) -> List[Channel]:
        """Autocomplete channels

        Autocomplete public channels on a team based on the search term provided
        in the request URL.

        Permissions:
            Must have the `list_team_channels` permission.
        Minimum Server Version:
            4.7

        Api Reference:
            `AutocompleteChannelsForTeam <https://api.mattermost.com/#operation/AutocompleteChannelsForTeam>`_
        """

        url = f"/teams/{team_id}/channels/autocomplete"
        params: Dict[str, Any] = {
            "name": name,
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
                response200_item = Channel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def autocomplete_channels_for_team_for_search(
        self,
        team_id: str,
        *,
        name: str,
    ) -> List[Channel]:
        """Autocomplete channels for search

        Autocomplete your channels on a team based on the search term provided
        in the request URL.

        Permissions:
            Must have the `list_team_channels` permission.
        Minimum Server Version:
            5.4

        Api Reference:
            `AutocompleteChannelsForTeamForSearch <https://api.mattermost.com/#operation/AutocompleteChannelsForTeamForSearch>`_
        """

        url = f"/teams/{team_id}/channels/search_autocomplete"
        params: Dict[str, Any] = {
            "name": name,
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
                response200_item = Channel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def search_channels(
        self,
        team_id: str,
        *,
        json_body: Union[SearchChannelsJsonBody, Dict],
    ) -> List[Channel]:
        """Search channels

        Search public channels on a team based on the search term provided in
        the request body.

        In server version 5.16 and later, a user without the
        `list_team_channels` permission will be able to use this endpoint, with
        the search results limited to the channels that the user is a member of.

        Permissions:
            Must have the `list_team_channels` permission.

        Api Reference:
            `SearchChannels <https://api.mattermost.com/#operation/SearchChannels>`_
        """

        url = f"/teams/{team_id}/channels/search"

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
            response201 = []
            _response201 = response.json()
            for response201_item_data in _response201:
                response201_item = Channel.parse_obj(response201_item_data)

                response201.append(response201_item)

            return response201
        return response

    async def search_archived_channels(
        self,
        team_id: str,
        *,
        json_body: Union[SearchArchivedChannelsJsonBody, Dict],
    ) -> List[Channel]:
        """Search archived channels

        Search archived channels on a team based on the search term provided in
        the request body.

        In server version 5.18 and later, a user without the
        `list_team_channels` permission will be able to use this endpoint, with
        the search results limited to the channels that the user is a member of.

        Permissions:
            Must have the `list_team_channels` permission.
        Minimum Server Version:
            5.18

        Api Reference:
            `SearchArchivedChannels <https://api.mattermost.com/#operation/SearchArchivedChannels>`_
        """

        url = f"/teams/{team_id}/channels/search_archived"

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
            response201 = []
            _response201 = response.json()
            for response201_item_data in _response201:
                response201_item = Channel.parse_obj(response201_item_data)

                response201.append(response201_item)

            return response201
        return response

    async def get_channel_by_name(
        self,
        team_id: str,
        channel_name: str,
        *,
        include_deleted: Optional[bool] = False,
    ) -> Channel:
        """Get a channel by name

        Gets channel from the provided team id and channel name strings.

        Permissions:
            `read_channel` permission for the channel.

        Api Reference:
            `GetChannelByName <https://api.mattermost.com/#operation/GetChannelByName>`_
        """

        url = f"/teams/{team_id}/channels/name/{channel_name}"
        params: Dict[str, Any] = {
            "include_deleted": include_deleted,
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
            response200 = Channel.parse_obj(response.json())

            return response200
        return response

    async def get_channel_by_name_for_team_name(
        self,
        team_name: str,
        channel_name: str,
        *,
        include_deleted: Optional[bool] = False,
    ) -> Channel:
        """Get a channel by name and team name

        Gets a channel from the provided team name and channel name strings.

        Permissions:
            `read_channel` permission for the channel.

        Api Reference:
            `GetChannelByNameForTeamName <https://api.mattermost.com/#operation/GetChannelByNameForTeamName>`_
        """

        url = f"/teams/name/{team_name}/channels/name/{channel_name}"
        params: Dict[str, Any] = {
            "include_deleted": include_deleted,
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
            response200 = Channel.parse_obj(response.json())

            return response200
        return response

    async def get_channel_members(
        self,
        channel_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[ChannelMember]:
        """Get channel members

        Get a page of members for a channel.

        Permissions:
            `read_channel` permission for the channel.

        Api Reference:
            `GetChannelMembers <https://api.mattermost.com/#operation/GetChannelMembers>`_
        """

        url = f"/channels/{channel_id}/members"
        params: Dict[str, Any] = {
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
                response200_item = ChannelMember.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def add_channel_member(
        self,
        channel_id: str,
        *,
        json_body: Union[AddChannelMemberJsonBody, Dict],
    ) -> ChannelMember:
        """Add user to channel

        Add a user to a channel by creating a channel member object.

        Api Reference:
            `AddChannelMember <https://api.mattermost.com/#operation/AddChannelMember>`_
        """

        url = f"/channels/{channel_id}/members"

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
            response201 = ChannelMember.parse_obj(response.json())

            return response201
        return response

    async def get_channel_members_by_ids(
        self,
        channel_id: str,
        *,
        json_body: Union[List[str], Dict],
    ) -> List[ChannelMember]:
        """Get channel members by ids

        Get a list of channel members based on the provided user ids.

        Permissions:
            Must have the `read_channel` permission.

        Api Reference:
            `GetChannelMembersByIds <https://api.mattermost.com/#operation/GetChannelMembersByIds>`_
        """

        url = f"/channels/{channel_id}/members/ids"
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
                response200_item = ChannelMember.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_channel_member(
        self,
        channel_id: str,
        user_id: str,
    ) -> ChannelMember:
        """Get channel member

        Get a channel member.

        Permissions:
            `read_channel` permission for the channel.

        Api Reference:
            `GetChannelMember <https://api.mattermost.com/#operation/GetChannelMember>`_
        """

        url = f"/channels/{channel_id}/members/{user_id}"

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
            response200 = ChannelMember.parse_obj(response.json())

            return response200
        return response

    async def remove_user_from_channel(
        self,
        channel_id: str,
        user_id: str,
    ) -> StatusOK:
        """Remove user from channel

        Delete a channel member, effectively removing them from a channel.

        In server version 5.3 and later, channel members can only be deleted
        from public or private channels.
        `manage_private_channel_members` permission if the channel is private.

        Permissions:
            `manage_public_channel_members` permission if the channel is
            public.

        Api Reference:
            `RemoveUserFromChannel <https://api.mattermost.com/#operation/RemoveUserFromChannel>`_
        """

        url = f"/channels/{channel_id}/members/{user_id}"

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

    async def update_channel_roles(
        self,
        channel_id: str,
        user_id: str,
        *,
        json_body: Union[UpdateChannelRolesJsonBody, Dict],
    ) -> StatusOK:
        """Update channel roles

        Update a user's roles for a channel.

        Permissions:
            Must have `manage_channel_roles` permission for the channel.

        Api Reference:
            `UpdateChannelRoles <https://api.mattermost.com/#operation/UpdateChannelRoles>`_
        """

        url = f"/channels/{channel_id}/members/{user_id}/roles"

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
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    async def update_channel_member_scheme_roles(
        self,
        channel_id: str,
        user_id: str,
        *,
        json_body: Union[UpdateChannelMemberSchemeRolesJsonBody, Dict],
    ) -> StatusOK:
        """Update the scheme-derived roles of a channel member.

        Update a channel member's scheme_admin/scheme_user properties. Typically
        this should either be `scheme_admin=false, scheme_user=true` for
        ordinary channel member, or `scheme_admin=true, scheme_user=true` for a
        channel admin.

        Permissions:
            Must be authenticated and have the `manage_channel_roles`
            permission.
        Minimum Server Version:
            5.0

        Api Reference:
            `UpdateChannelMemberSchemeRoles <https://api.mattermost.com/#operation/UpdateChannelMemberSchemeRoles>`_
        """

        url = f"/channels/{channel_id}/members/{user_id}/schemeRoles"

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
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    async def update_channel_notify_props(
        self,
        channel_id: str,
        user_id: str,
        *,
        json_body: Union[ChannelNotifyProps, Dict],
    ) -> StatusOK:
        """Update channel notifications

        Update a user's notification properties for a channel. Only the provided
        fields are updated.

        Permissions:
            Must be logged in as the user or have `edit_other_users`
            permission.

        Api Reference:
            `UpdateChannelNotifyProps <https://api.mattermost.com/#operation/UpdateChannelNotifyProps>`_
        """

        url = f"/channels/{channel_id}/members/{user_id}/notify_props"

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
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    async def view_channel(
        self,
        user_id: str,
        *,
        json_body: Union[ViewChannelJsonBody, Dict],
    ) -> ViewChannelResponse200:
        """View channel

        Perform all the actions involved in viewing a channel. This includes
        marking channels as read, clearing push notifications, and updating the
        active channel.

        __Response only includes `last_viewed_at_times` in Mattermost server 4.3
        and newer.__

        Permissions:
            Must be logged in as user or have `edit_other_users`
            permission.

        Api Reference:
            `ViewChannel <https://api.mattermost.com/#operation/ViewChannel>`_
        """

        url = f"/channels/members/{user_id}/view"

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
            response200 = ViewChannelResponse200.parse_obj(response.json())

            return response200
        return response

    async def get_channel_members_for_user(
        self,
        user_id: str,
        team_id: str,
    ) -> List[ChannelMember]:
        """Get channel memberships and roles for a user

        Get all channel memberships and associated membership roles (i.e.
        `channel_user`, `channel_admin`) for a user on a specific team.

        Permissions:
            Logged in as the user and `view_team` permission for the
            team. Having `manage_system` permission voids the previous
            requirements.

        Api Reference:
            `GetChannelMembersForUser <https://api.mattermost.com/#operation/GetChannelMembersForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels/members"

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
                response200_item = ChannelMember.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_channels_for_team_for_user(
        self,
        user_id: str,
        team_id: str,
        *,
        include_deleted: Optional[bool] = False,
        last_delete_at: Optional[int] = 0,
    ) -> List[Channel]:
        """Get channels for user

        Get all the channels on a team for a user.

        Permissions:
            Logged in as the user, or have `edit_other_users`
            permission, and `view_team` permission for the team.

        Api Reference:
            `GetChannelsForTeamForUser <https://api.mattermost.com/#operation/GetChannelsForTeamForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels"
        params: Dict[str, Any] = {
            "include_deleted": include_deleted,
            "last_delete_at": last_delete_at,
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
                response200_item = Channel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_channels_for_user(
        self,
        user_id: str,
        *,
        last_delete_at: Optional[int] = 0,
        include_deleted: Optional[bool] = False,
    ) -> List[Channel]:
        """Get all channels from all teams

        Get all channels from all teams that a user is a member of.

        Permissions:
            Logged in as the user, or have `edit_other_users`
            permission.
        Minimum Server Version:
            6.1

        Api Reference:
            `GetChannelsForUser <https://api.mattermost.com/#operation/GetChannelsForUser>`_
        """

        url = f"/users/{user_id}/channels"
        params: Dict[str, Any] = {
            "last_delete_at": last_delete_at,
            "include_deleted": include_deleted,
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
                response200_item = Channel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_channel_unread(
        self,
        user_id: str,
        channel_id: str,
    ) -> ChannelUnread:
        """Get unread messages

        Get the total unread messages and mentions for a channel for a user.

        Permissions:
            Must be logged in as user and have the `read_channel`
            permission, or have `edit_other_usrs` permission.

        Api Reference:
            `GetChannelUnread <https://api.mattermost.com/#operation/GetChannelUnread>`_
        """

        url = f"/users/{user_id}/channels/{channel_id}/unread"

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
            response200 = ChannelUnread.parse_obj(response.json())

            return response200
        return response

    async def update_channel_scheme(
        self,
        channel_id: str,
        *,
        json_body: Union[UpdateChannelSchemeJsonBody, Dict],
    ) -> StatusOK:
        """Set a channel's scheme

        Set a channel's scheme, more specifically sets the scheme_id value of a
        channel record.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            4.10

        Api Reference:
            `UpdateChannelScheme <https://api.mattermost.com/#operation/UpdateChannelScheme>`_
        """

        url = f"/channels/{channel_id}/scheme"

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
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    async def channel_members_minus_group_members(
        self,
        channel_id: str,
        *,
        group_ids: str = "",
        page: Optional[int] = 0,
        per_page: Optional[int] = 0,
    ) -> None:
        """Channel members minus group members.

        Get the set of users who are members of the channel minus the set of
        users who are members of the given groups.
        Each user object contains an array of group objects representing the
        group memberships for that user.
        Each user object contains the boolean fields `scheme_guest`,
        `scheme_user`, and `scheme_admin` representing the roles that user has
        for the given channel.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.14

        Api Reference:
            `ChannelMembersMinusGroupMembers <https://api.mattermost.com/#operation/ChannelMembersMinusGroupMembers>`_
        """

        url = f"/channels/{channel_id}/members_minus_group_members"
        params: Dict[str, Any] = {
            "group_ids": group_ids,
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

        return response

    async def get_channel_member_counts_by_group(
        self,
        channel_id: str,
        *,
        include_timezones: Optional[bool] = False,
    ) -> None:
        """Channel members counts for each group that has atleast one member in the
        channel

        Returns a set of ChannelMemberCountByGroup objects which contain a
        `group_id`, `channel_member_count` and a
        `channel_member_timezones_count`.

        Permissions:
            Must have `read_channel` permission for the given channel.
        Minimum Server Version:
            5.24

        Api Reference:
            `GetChannelMemberCountsByGroup <https://api.mattermost.com/#operation/GetChannelMemberCountsByGroup>`_
        """

        url = f"/channels/{channel_id}/member_counts_by_group"
        params: Dict[str, Any] = {
            "include_timezones": include_timezones,
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

        return response

    async def get_channel_moderations(
        self,
        channel_id: str,
    ) -> List[ChannelModeration]:
        """Get information about channel's moderation.



        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.22

        Api Reference:
            `GetChannelModerations <https://api.mattermost.com/#operation/GetChannelModerations>`_
        """

        url = f"/channels/{channel_id}/moderations"

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
                response200_item = ChannelModeration.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def patch_channel_moderations(
        self,
        channel_id: str,
        *,
        json_body: Union[ChannelModerationPatch, Dict],
    ) -> List[ChannelModeration]:
        """Update a channel's moderation settings.



        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.22

        Api Reference:
            `PatchChannelModerations <https://api.mattermost.com/#operation/PatchChannelModerations>`_
        """

        url = f"/channels/{channel_id}/moderations/patch"

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
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = ChannelModeration.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_sidebar_categories_for_team_for_user(
        self,
        team_id: str,
        user_id: str,
    ) -> List[OrderedSidebarCategories]:
        """Get user's sidebar categories

        Get a list of sidebar categories that will appear in the user's sidebar
        on the given team, including a list of channel IDs in each category.

        Permissions:
            Must be authenticated and have the `list_team_channels`
            permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `GetSidebarCategoriesForTeamForUser <https://api.mattermost.com/#operation/GetSidebarCategoriesForTeamForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels/categories"

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
                response200_item = OrderedSidebarCategories.parse_obj(
                    response200_item_data
                )

                response200.append(response200_item)

            return response200
        return response

    async def update_sidebar_categories_for_team_for_user(
        self,
        team_id: str,
        user_id: str,
        *,
        json_body: Union[List[SidebarCategory], Dict],
    ) -> SidebarCategory:
        """Update user's sidebar categories

        Update any number of sidebar categories for the user on the given team.
        This can be used to reorder the channels in these categories.

        Permissions:
            Must be authenticated and have the `list_team_channels`
            permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `UpdateSidebarCategoriesForTeamForUser <https://api.mattermost.com/#operation/UpdateSidebarCategoriesForTeamForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels/categories"
        json_json_body = []
        for json_body_item_data in json_body:

            if isinstance(json_body_item_data, BaseModel):
                json_body_item = json_body_item_data.dict(exclude_unset=True)
            else:
                json_body_item = json_body_item_data

            json_json_body.append(json_body_item)

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
            response200 = SidebarCategory.parse_obj(response.json())

            return response200
        return response

    async def create_sidebar_category_for_team_for_user(
        self,
        team_id: str,
        user_id: str,
        *,
        json_body: Union[SidebarCategory, Dict],
    ) -> SidebarCategory:
        """Create user's sidebar category

        Create a custom sidebar category for the user on the given team.

        Permissions:
            Must be authenticated and have the `list_team_channels`
            permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `CreateSidebarCategoryForTeamForUser <https://api.mattermost.com/#operation/CreateSidebarCategoryForTeamForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels/categories"

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
            response200 = SidebarCategory.parse_obj(response.json())

            return response200
        return response

    async def get_sidebar_category_order_for_team_for_user(
        self,
        team_id: str,
        user_id: str,
    ) -> List[str]:
        """Get user's sidebar category order

        Returns the order of the sidebar categories for a user on the given team
        as an array of IDs.

        Permissions:
            Must be authenticated and have the `list_team_channels`
            permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `GetSidebarCategoryOrderForTeamForUser <https://api.mattermost.com/#operation/GetSidebarCategoryOrderForTeamForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels/categories/order"

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
            response200 = cast(List[str], response.json())

            return response200
        return response

    async def update_sidebar_category_order_for_team_for_user(
        self,
        team_id: str,
        user_id: str,
        *,
        json_body: Union[List[str], Dict],
    ) -> List[str]:
        """Update user's sidebar category order

        Updates the order of the sidebar categories for a user on the given
        team. The provided array must include the IDs of all categories on the
        team.

        Permissions:
            Must be authenticated and have the `list_team_channels`
            permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `UpdateSidebarCategoryOrderForTeamForUser <https://api.mattermost.com/#operation/UpdateSidebarCategoryOrderForTeamForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels/categories/order"
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
            response200 = cast(List[str], response.json())

            return response200
        return response

    async def get_sidebar_category_for_team_for_user(
        self,
        team_id: str,
        user_id: str,
        category_id: str,
    ) -> SidebarCategory:
        """Get sidebar category

        Returns a single sidebar category for the user on the given team.

        Permissions:
            Must be authenticated and have the `list_team_channels`
            permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `GetSidebarCategoryForTeamForUser <https://api.mattermost.com/#operation/GetSidebarCategoryForTeamForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels/categories/{category_id}"

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
            response200 = SidebarCategory.parse_obj(response.json())

            return response200
        return response

    async def update_sidebar_category_for_team_for_user(
        self,
        team_id: str,
        user_id: str,
        category_id: str,
        *,
        json_body: Union[SidebarCategory, Dict],
    ) -> SidebarCategory:
        """Update sidebar category

        Updates a single sidebar category for the user on the given team.

        Permissions:
            Must be authenticated and have the `list_team_channels`
            permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `UpdateSidebarCategoryForTeamForUser <https://api.mattermost.com/#operation/UpdateSidebarCategoryForTeamForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels/categories/{category_id}"

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
            response200 = SidebarCategory.parse_obj(response.json())

            return response200
        return response

    async def remove_sidebar_category_for_team_for_user(
        self,
        team_id: str,
        user_id: str,
        category_id: str,
    ) -> SidebarCategory:
        """Delete sidebar category

        Deletes a single sidebar category for the user on the given team. Only
        custom categories can be deleted.

        Permissions:
            Must be authenticated and have the `list_team_channels`
            permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `RemoveSidebarCategoryForTeamForUser <https://api.mattermost.com/#operation/RemoveSidebarCategoryForTeamForUser>`_
        """

        url = f"/users/{user_id}/teams/{team_id}/channels/categories/{category_id}"

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
            response200 = SidebarCategory.parse_obj(response.json())

            return response200
        return response
