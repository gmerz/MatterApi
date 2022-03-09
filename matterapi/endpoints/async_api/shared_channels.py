""" Module to access the SharedChannels endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Any, Dict, List, Optional

from ...models import RemoteClusterInfo, SharedChannel
from ..base import ApiBaseClass


class SharedChannelsApi(ApiBaseClass):
    """Endpoints for getting information about shared channels."""

    async def get_all_shared_channels(
        self,
        team_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 0,
    ) -> List[SharedChannel]:
        """Get all shared channels for team.

        Get all shared channels for a team.

        Permissions:
            Must be authenticated.
        Minimum Server Version:
            5.50

        Api Reference:
            `GetAllSharedChannels <https://api.mattermost.com/#operation/GetAllSharedChannels>`_
        """

        url = f"/sharedchannels/{team_id}"
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
                response200_item = SharedChannel.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def get_remote_cluster_info(
        self,
        remote_id: str,
    ) -> RemoteClusterInfo:
        """Get remote cluster info by ID for user.

        Get remote cluster info based on remoteId.

        Permissions:
            Must be authenticated and user must belong to at least one
            channel shared with the remote cluster.
        Minimum Server Version:
            5.50

        Api Reference:
            `GetRemoteClusterInfo <https://api.mattermost.com/#operation/GetRemoteClusterInfo>`_
        """

        url = f"/sharedchannels/remote_info/{remote_id}"

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
            response200 = RemoteClusterInfo.parse_obj(response.json())

            return response200
        return response
