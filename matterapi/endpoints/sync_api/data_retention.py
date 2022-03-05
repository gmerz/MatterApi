""" Module to access the DataRetention endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ...models import (
    ChannelListWithTeamData,
    DataRetentionPolicyCreate,
    DataRetentionPolicyWithTeamAndChannelCounts,
    DataRetentionPolicyWithTeamAndChannelIds,
    GetDataRetentionPoliciesCountResponse200,
    GlobalDataRetentionPolicy,
    RetentionPolicyForChannelList,
    RetentionPolicyForTeamList,
    SearchChannelsForRetentionPolicyJsonBody,
    SearchTeamsForRetentionPolicyJsonBody,
    StatusOK,
    Team,
)
from ..base import ApiBaseClass


class DataRetentionApi(ApiBaseClass):
    """Endpoint for getting data retention policy settings."""

    def get_team_policies_for_user(
        self,
        user_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> RetentionPolicyForTeamList:
        """Get the policies which are applied to a user's teams

        Gets the policies which are applied to the all of the teams to which a
        user belongs.

        ##### License
        Requires an E20 license.

        Permissions:
            Must be logged in as the user or have the `manage_system`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `GetTeamPoliciesForUser <https://api.mattermost.com/#operation/GetTeamPoliciesForUser>`_
        """

        url = f"/users/{user_id}/data_retention/team_policies"
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
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = RetentionPolicyForTeamList.parse_obj(response.json())

            return response200
        return response

    def get_channel_policies_for_user(
        self,
        user_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> RetentionPolicyForChannelList:
        """Get the policies which are applied to a user's channels

        Gets the policies which are applied to the all of the channels to which
        a user belongs.

        ##### License
        Requires an E20 license.

        Permissions:
            Must be logged in as the user or have the `manage_system`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `GetChannelPoliciesForUser <https://api.mattermost.com/#operation/GetChannelPoliciesForUser>`_
        """

        url = f"/users/{user_id}/data_retention/channel_policies"
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
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = RetentionPolicyForChannelList.parse_obj(response.json())

            return response200
        return response

    def get_data_retention_policy(
        self,
    ) -> GlobalDataRetentionPolicy:
        """Get the global data retention policy

        Gets the current global data retention policy details from the server,
        including what data should be purged and the cutoff times for each data
        type that should be purged.

        ##### License
        Requires an E20 license.

        Permissions:
            Requires an active session but no other permissions.
        Minimum Server Version:
            4.3

        Api Reference:
            `GetDataRetentionPolicy <https://api.mattermost.com/#operation/GetDataRetentionPolicy>`_
        """

        url = "/data_retention/policy"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = GlobalDataRetentionPolicy.parse_obj(response.json())

            return response200
        return response

    def get_data_retention_policies_count(
        self,
    ) -> GetDataRetentionPoliciesCountResponse200:
        """Get the number of granular data retention policies

        Gets the number of granular (i.e. team or channel-specific) data
        retention
        policies from the server.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_read_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `GetDataRetentionPoliciesCount <https://api.mattermost.com/#operation/GetDataRetentionPoliciesCount>`_
        """

        url = "/data_retention/policies_count"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = GetDataRetentionPoliciesCountResponse200.parse_obj(
                response.json()
            )

            return response200
        return response

    def get_data_retention_policies(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[DataRetentionPolicyWithTeamAndChannelCounts]:
        """Get the granular data retention policies

        Gets details about the granular (i.e. team or channel-specific) data
        retention
        policies from the server.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_read_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `GetDataRetentionPolicies <https://api.mattermost.com/#operation/GetDataRetentionPolicies>`_
        """

        url = "/data_retention/policies"
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
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = (
                    DataRetentionPolicyWithTeamAndChannelCounts.parse_obj(
                        response200_item_data
                    )
                )

                response200.append(response200_item)

            return response200
        return response

    def create_data_retention_policy(
        self,
        *,
        json_body: DataRetentionPolicyCreate,
    ) -> DataRetentionPolicyWithTeamAndChannelCounts:
        """Create a new granular data retention policy

        Creates a new granular data retention policy with the specified display
        name and post duration.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_write_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `CreateDataRetentionPolicy <https://api.mattermost.com/#operation/CreateDataRetentionPolicy>`_
        """

        url = "/data_retention/policies"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 201:
            response201 = DataRetentionPolicyWithTeamAndChannelCounts.parse_obj(
                response.json()
            )

            return response201
        return response

    def get_data_retention_policy_by_id(
        self,
        policy_id: str,
    ) -> DataRetentionPolicyWithTeamAndChannelCounts:
        """Get a granular data retention policy

        Gets details about a granular data retention policies by ID.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_read_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `GetDataRetentionPolicyByID <https://api.mattermost.com/#operation/GetDataRetentionPolicyByID>`_
        """

        url = f"/data_retention/policies/{policy_id}"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = DataRetentionPolicyWithTeamAndChannelCounts.parse_obj(
                response.json()
            )

            return response200
        return response

    def delete_data_retention_policy(
        self,
        policy_id: str,
    ) -> StatusOK:
        """Delete a granular data retention policy

        Deletes a granular data retention policy.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_write_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `DeleteDataRetentionPolicy <https://api.mattermost.com/#operation/DeleteDataRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.delete(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def patch_data_retention_policy(
        self,
        policy_id: str,
        *,
        json_body: DataRetentionPolicyWithTeamAndChannelIds,
    ) -> DataRetentionPolicyWithTeamAndChannelCounts:
        """Patch a granular data retention policy

        Patches (i.e. replaces the fields of) a granular data retention policy.
        If any fields are omitted, they will not be changed.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_write_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `PatchDataRetentionPolicy <https://api.mattermost.com/#operation/PatchDataRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.patch(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = DataRetentionPolicyWithTeamAndChannelCounts.parse_obj(
                response.json()
            )

            return response200
        return response

    def get_teams_for_retention_policy(
        self,
        policy_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Team]:
        """Get the teams for a granular data retention policy

        Gets the teams to which a granular data retention policy is applied.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_read_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `GetTeamsForRetentionPolicy <https://api.mattermost.com/#operation/GetTeamsForRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}/teams"
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
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = Team.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def add_teams_to_retention_policy(
        self,
        policy_id: str,
        *,
        json_body: List[str],
    ) -> StatusOK:
        """Add teams to a granular data retention policy

        Adds teams to a granular data retention policy.



        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_write_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `AddTeamsToRetentionPolicy <https://api.mattermost.com/#operation/AddTeamsToRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}/teams"
        json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def remove_teams_from_retention_policy(
        self,
        policy_id: str,
        *,
        json_body: List[str],
    ) -> StatusOK:
        """Delete teams from a granular data retention policy

        Delete teams from a granular data retention policy.



        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_write_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `RemoveTeamsFromRetentionPolicy <https://api.mattermost.com/#operation/RemoveTeamsFromRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}/teams"
        json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.delete(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def search_teams_for_retention_policy(
        self,
        policy_id: str,
        *,
        json_body: SearchTeamsForRetentionPolicyJsonBody,
    ) -> List[Team]:
        """Search for the teams in a granular data retention policy

        Searches for the teams to which a granular data retention policy is
        applied.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_read_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `SearchTeamsForRetentionPolicy <https://api.mattermost.com/#operation/SearchTeamsForRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}/teams/search"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = Team.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def get_channels_for_retention_policy(
        self,
        policy_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> ChannelListWithTeamData:
        """Get the channels for a granular data retention policy

        Gets the channels to which a granular data retention policy is applied.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_read_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `GetChannelsForRetentionPolicy <https://api.mattermost.com/#operation/GetChannelsForRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}/channels"
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
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = ChannelListWithTeamData.parse_obj(response.json())

            return response200
        return response

    def add_channels_to_retention_policy(
        self,
        policy_id: str,
        *,
        json_body: List[str],
    ) -> StatusOK:
        """Add channels to a granular data retention policy

        Adds channels to a granular data retention policy.



        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_write_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `AddChannelsToRetentionPolicy <https://api.mattermost.com/#operation/AddChannelsToRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}/channels"
        json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def remove_channels_from_retention_policy(
        self,
        policy_id: str,
        *,
        json_body: List[str],
    ) -> StatusOK:
        """Delete channels from a granular data retention policy

        Delete channels from a granular data retention policy.



        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_write_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `RemoveChannelsFromRetentionPolicy <https://api.mattermost.com/#operation/RemoveChannelsFromRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}/channels"
        json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.delete(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def search_channels_for_retention_policy(
        self,
        policy_id: str,
        *,
        json_body: SearchChannelsForRetentionPolicyJsonBody,
    ) -> ChannelListWithTeamData:
        """Search for the channels in a granular data retention policy

        Searches for the channels to which a granular data retention policy is
        applied.

        ##### License
        Requires an E20 license.

        Permissions:
            Must have the `sysconsole_read_compliance_data_retention`
            permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `SearchChannelsForRetentionPolicy <https://api.mattermost.com/#operation/SearchChannelsForRetentionPolicy>`_
        """

        url = f"/data_retention/policies/{policy_id}/channels/search"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = ChannelListWithTeamData.parse_obj(response.json())

            return response200
        return response
