""" Module to access the Commands endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from ...models import (
    AutocompleteSuggestion,
    Command,
    CommandResponse,
    CreateCommandJsonBody,
    ExecuteCommandJsonBody,
    MoveCommandJsonBody,
    RegenCommandTokenResponse200,
    StatusOK,
)
from ..base import ApiBaseClass


class CommandsApi(ApiBaseClass):
    """Endpoints for creating, getting and updating slash commands."""

    async def list_commands(
        self,
        *,
        team_id: Optional[str] = None,
        custom_only: Optional[bool] = False,
    ) -> List[Command]:
        """List commands for a team

        List commands for a team.

        Permissions:
            `manage_slash_commands` if need list custom commands.

        Api Reference:
            `ListCommands <https://api.mattermost.com/#operation/ListCommands>`_
        """

        url = "/commands"
        params: Dict[str, Any] = {
            "team_id": team_id,
            "custom_only": custom_only,
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
                response200_item = Command.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def create_command(
        self,
        *,
        json_body: Union[CreateCommandJsonBody, Dict],
    ) -> Command:
        """Create a command

        Create a command for a team.

        Permissions:
            `manage_slash_commands` for the team the command is in.

        Api Reference:
            `CreateCommand <https://api.mattermost.com/#operation/CreateCommand>`_
        """

        url = "/commands"

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
            response201 = Command.parse_obj(response.json())

            return response201
        return response

    async def list_autocomplete_commands(
        self,
        team_id: str,
    ) -> List[Command]:
        """List autocomplete commands

        List autocomplete commands in the team.

        Permissions:
            `view_team` for the team.

        Api Reference:
            `ListAutocompleteCommands <https://api.mattermost.com/#operation/ListAutocompleteCommands>`_
        """

        url = f"/teams/{team_id}/commands/autocomplete"

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
                response200_item = Command.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def list_command_autocomplete_suggestions(
        self,
        team_id: str,
        *,
        user_input: str,
    ) -> List[AutocompleteSuggestion]:
        """List commands' autocomplete data

        List commands' autocomplete data for the team.

        Permissions:
            `view_team` for the team.
        Minimum Server Version:
            5.24

        Api Reference:
            `ListCommandAutocompleteSuggestions <https://api.mattermost.com/#operation/ListCommandAutocompleteSuggestions>`_
        """

        url = f"/teams/{team_id}/commands/autocomplete_suggestions"
        params: Dict[str, Any] = {
            "user_input": user_input,
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
                response200_item = AutocompleteSuggestion.parse_obj(
                    response200_item_data
                )

                response200.append(response200_item)

            return response200
        return response

    async def get_command_by_id(
        self,
        command_id: str,
    ) -> Command:
        """Get a command

        Get a command definition based on command id string.

        Permissions:
            Must have `manage_slash_commands` permission for the team
            the command is in.
        Minimum Server Version:
            5.22

        Api Reference:
            `GetCommandById <https://api.mattermost.com/#operation/GetCommandById>`_
        """

        url = f"/commands/{command_id}"

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
            response200 = Command.parse_obj(response.json())

            return response200
        return response

    async def update_command(
        self,
        command_id: str,
        *,
        json_body: Union[Command, Dict],
    ) -> Command:
        """Update a command

        Update a single command based on command id string and Command struct.

        Permissions:
            Must have `manage_slash_commands` permission for the team
            the command is in.

        Api Reference:
            `UpdateCommand <https://api.mattermost.com/#operation/UpdateCommand>`_
        """

        url = f"/commands/{command_id}"

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
            response200 = Command.parse_obj(response.json())

            return response200
        return response

    async def delete_command(
        self,
        command_id: str,
    ) -> StatusOK:
        """Delete a command

        Delete a command based on command id string.

        Permissions:
            Must have `manage_slash_commands` permission for the team
            the command is in.

        Api Reference:
            `DeleteCommand <https://api.mattermost.com/#operation/DeleteCommand>`_
        """

        url = f"/commands/{command_id}"

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

    async def move_command(
        self,
        command_id: str,
        *,
        json_body: Union[MoveCommandJsonBody, Dict],
    ) -> StatusOK:
        """Move a command

        Move a command to a different team based on command id string.

        Permissions:
            Must have `manage_slash_commands` permission for the team
            the command is currently in and the destination team.
        Minimum Server Version:
            5.22

        Api Reference:
            `MoveCommand <https://api.mattermost.com/#operation/MoveCommand>`_
        """

        url = f"/commands/{command_id}/move"

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

    async def regen_command_token(
        self,
        command_id: str,
    ) -> RegenCommandTokenResponse200:
        """Generate a new token

        Generate a new token for the command based on command id string.

        Permissions:
            Must have `manage_slash_commands` permission for the team
            the command is in.

        Api Reference:
            `RegenCommandToken <https://api.mattermost.com/#operation/RegenCommandToken>`_
        """

        url = f"/commands/{command_id}/regen_token"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.put(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = RegenCommandTokenResponse200.parse_obj(response.json())

            return response200
        return response

    async def execute_command(
        self,
        *,
        json_body: Union[ExecuteCommandJsonBody, Dict],
    ) -> CommandResponse:
        """Execute a command

        Execute a command on a team.

        Permissions:
            Must have `use_slash_commands` permission for the team the
            command is in.

        Api Reference:
            `ExecuteCommand <https://api.mattermost.com/#operation/ExecuteCommand>`_
        """

        url = "/commands/execute"

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
            response200 = CommandResponse.parse_obj(response.json())

            return response200
        return response
