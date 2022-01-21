from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ...models import (
    AutocompleteSuggestion,
    Command,
    CommandResponse,
    CreateCommandJsonBody,
    ExecuteCommandJsonBody,
    MoveCommandJsonBody,
    RegenCommandTokenResponse_200,
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
        """

        url = "{}/commands".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()
        params: Dict[str, Any] = {
            "team_id": team_id,
            "custom_only": custom_only,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "params": params,
        }

        response = await self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = Command.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response

    async def create_command(
        self,
        *,
        json_body: CreateCommandJsonBody,
    ) -> Command:
        """Create a command

        Create a command for a team.

        Permissions:
            `manage_slash_commands` for the team the command is in.
        """

        url = "{}/commands".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "json": json_json_body,
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 201:
            response_201 = Command.parse_obj(response.json())

            return response_201
        return response

    async def list_autocomplete_commands(
        self,
        team_id: str,
    ) -> List[Command]:
        """List autocomplete commands

        List autocomplete commands in the team.

        Permissions:
            `view_team` for the team.
        """

        url = "{}/teams/{team_id}/commands/autocomplete".format(
            self.client.base_url, team_id=team_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = Command.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
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
        """

        url = "{}/teams/{team_id}/commands/autocomplete_suggestions".format(
            self.client.base_url, team_id=team_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()
        params: Dict[str, Any] = {
            "user_input": user_input,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "params": params,
        }

        response = await self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = AutocompleteSuggestion.parse_obj(
                    response_200_item_data
                )

                response_200.append(response_200_item)

            return response_200
        return response

    async def get_command_by_id(
        self,
        command_id: str,
    ) -> Command:
        """Get a command

        Get a command definition based on command id string.

        Permissions:
            Must have `manage_slash_commands` permission for the team the command is in.
        Minimum Server Version:
            5.22
        """

        url = "{}/commands/{command_id}".format(
            self.client.base_url, command_id=command_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = Command.parse_obj(response.json())

            return response_200
        return response

    async def update_command(
        self,
        command_id: str,
        *,
        json_body: Command,
    ) -> Command:
        """Update a command

        Update a single command based on command id string and Command struct.

        Permissions:
            Must have `manage_slash_commands` permission for the team the command is in.
        """

        url = "{}/commands/{command_id}".format(
            self.client.base_url, command_id=command_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "json": json_json_body,
        }

        response = await self.client.put(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = Command.parse_obj(response.json())

            return response_200
        return response

    async def delete_command(
        self,
        command_id: str,
    ) -> StatusOK:
        """Delete a command

        Delete a command based on command id string.

        Permissions:
            Must have `manage_slash_commands` permission for the team the command is in.
        """

        url = "{}/commands/{command_id}".format(
            self.client.base_url, command_id=command_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.delete(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = StatusOK.parse_obj(response.json())

            return response_200
        return response

    async def move_command(
        self,
        command_id: str,
        *,
        json_body: MoveCommandJsonBody,
    ) -> StatusOK:
        """Move a command

        Move a command to a different team based on command id string.

        Permissions:
            Must have `manage_slash_commands` permission for the team the command is currently in and the destination team.
        Minimum Server Version:
            5.22
        """

        url = "{}/commands/{command_id}/move".format(
            self.client.base_url, command_id=command_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "json": json_json_body,
        }

        response = await self.client.put(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = StatusOK.parse_obj(response.json())

            return response_200
        return response

    async def regen_command_token(
        self,
        command_id: str,
    ) -> RegenCommandTokenResponse_200:
        """Generate a new token

        Generate a new token for the command based on command id string.

        Permissions:
            Must have `manage_slash_commands` permission for the team the command is in.
        """

        url = "{}/commands/{command_id}/regen_token".format(
            self.client.base_url, command_id=command_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.put(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = RegenCommandTokenResponse_200.parse_obj(response.json())

            return response_200
        return response

    async def execute_command(
        self,
        *,
        json_body: ExecuteCommandJsonBody,
    ) -> CommandResponse:
        """Execute a command

        Execute a command on a team.

        Permissions:
            Must have `use_slash_commands` permission for the team the command is in.
        """

        url = "{}/commands/execute".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "json": json_json_body,
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = CommandResponse.parse_obj(response.json())

            return response_200
        return response
