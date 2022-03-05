""" Module to access the Bots endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ...models import (
    Bot,
    ConvertBotToUserJsonBody,
    CreateBotJsonBody,
    PatchBotJsonBody,
    SetBotIconImageMultipartData,
    StatusOK,
)
from ..base import ApiBaseClass


class BotsApi(ApiBaseClass):
    """Endpoints for creating, getting and updating bot users."""

    async def convert_user_to_bot(
        self,
        user_id: str,
    ) -> StatusOK:
        """Convert a user into a bot

        Convert a user into a bot.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `ConvertUserToBot <https://api.mattermost.com/#operation/ConvertUserToBot>`_
        """

        url = f"/users/{user_id}/convert_to_bot"

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

    async def get_bots(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
        include_deleted: Optional[bool] = None,
        only_orphaned: Optional[bool] = None,
    ) -> List[Bot]:
        """Get bots

        Get a page of a list of bots.

        Permissions:
            Must have `read_bots` permission for bots you are managing,
            and `read_others_bots` permission for bots others are
            managing.
        Minimum Server Version:
            5.10

        Api Reference:
            `GetBots <https://api.mattermost.com/#operation/GetBots>`_
        """

        url = "/bots"
        params: Dict[str, Any] = {
            "page": page,
            "per_page": per_page,
            "include_deleted": include_deleted,
            "only_orphaned": only_orphaned,
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
                response200_item = Bot.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def create_bot(
        self,
        *,
        json_body: CreateBotJsonBody,
    ) -> Bot:
        """Create a bot

        Create a new bot account on the system. Username is required.

        Permissions:
            Must have `create_bot` permission.
        Minimum Server Version:
            5.10

        Api Reference:
            `CreateBot <https://api.mattermost.com/#operation/CreateBot>`_
        """

        url = "/bots"

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
            response201 = Bot.parse_obj(response.json())

            return response201
        return response

    async def get_bot(
        self,
        bot_user_id: str,
        *,
        include_deleted: Optional[bool] = None,
    ) -> Bot:
        """Get a bot

        Get a bot specified by its bot id.

        Permissions:
            Must have `read_bots` permission for bots you are managing,
            and `read_others_bots` permission for bots others are
            managing.
        Minimum Server Version:
            5.10

        Api Reference:
            `GetBot <https://api.mattermost.com/#operation/GetBot>`_
        """

        url = f"/bots/{bot_user_id}"
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
            response200 = Bot.parse_obj(response.json())

            return response200
        return response

    async def patch_bot(
        self,
        bot_user_id: str,
        *,
        json_body: PatchBotJsonBody,
    ) -> Bot:
        """Patch a bot

        Partially update a bot by providing only the fields you want to update.
        Omitted fields will not be updated. The fields that can be updated are
        defined in the request body, all other provided fields will be ignored.

        Permissions:
            Must have `manage_bots` permission.
        Minimum Server Version:
            5.10

        Api Reference:
            `PatchBot <https://api.mattermost.com/#operation/PatchBot>`_
        """

        url = f"/bots/{bot_user_id}"

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
            response200 = Bot.parse_obj(response.json())

            return response200
        return response

    async def disable_bot(
        self,
        bot_user_id: str,
    ) -> Bot:
        """Disable a bot

        Disable a bot.

        Permissions:
            Must have `manage_bots` permission.
        Minimum Server Version:
            5.10

        Api Reference:
            `DisableBot <https://api.mattermost.com/#operation/DisableBot>`_
        """

        url = f"/bots/{bot_user_id}/disable"

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
            response200 = Bot.parse_obj(response.json())

            return response200
        return response

    async def enable_bot(
        self,
        bot_user_id: str,
    ) -> Bot:
        """Enable a bot

        Enable a bot.

        Permissions:
            Must have `manage_bots` permission.
        Minimum Server Version:
            5.10

        Api Reference:
            `EnableBot <https://api.mattermost.com/#operation/EnableBot>`_
        """

        url = f"/bots/{bot_user_id}/enable"

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
            response200 = Bot.parse_obj(response.json())

            return response200
        return response

    async def assign_bot(
        self,
        bot_user_id: str,
        user_id: str,
    ) -> Bot:
        """Assign a bot to a user

        Assign a bot to a specified user.

        Permissions:
            Must have `manage_bots` permission.
        Minimum Server Version:
            5.10

        Api Reference:
            `AssignBot <https://api.mattermost.com/#operation/AssignBot>`_
        """

        url = f"/bots/{bot_user_id}/assign/{user_id}"

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
            response200 = Bot.parse_obj(response.json())

            return response200
        return response

    async def get_bot_icon_image(
        self,
        bot_user_id: str,
    ) -> None:
        """Get bot's LHS icon

        Get a bot's LHS icon image based on bot_user_id string parameter.

        Permissions:
            Must be logged in.
        Minimum Server Version:
            5.14

        Api Reference:
            `GetBotIconImage <https://api.mattermost.com/#operation/GetBotIconImage>`_
        """

        url = f"/bots/{bot_user_id}/icon"

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

        return response

    async def set_bot_icon_image(
        self,
        bot_user_id: str,
        *,
        multipart_data: SetBotIconImageMultipartData,
    ) -> StatusOK:
        """Set bot's LHS icon image

        Set a bot's LHS icon image based on bot_user_id string parameter. Icon
        image must be SVG format, all other formats are rejected.

        Permissions:
            Must have `manage_bots` permission.
        Minimum Server Version:
            5.14

        Api Reference:
            `SetBotIconImage <https://api.mattermost.com/#operation/SetBotIconImage>`_
        """

        url = f"/bots/{bot_user_id}/icon"

        multipart_body_data = SetBotIconImageMultipartData.parse_obj(multipart_data)

        request_kwargs = {
            "url": url,
            "data": multipart_body_data.get_data(),
            "files": multipart_body_data.get_files(),
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

    async def delete_bot_icon_image(
        self,
        bot_user_id: str,
    ) -> StatusOK:
        """Delete bot's LHS icon image

        Delete bot's LHS icon image based on bot_user_id string parameter.

        Permissions:
            Must have `manage_bots` permission.
        Minimum Server Version:
            5.14

        Api Reference:
            `DeleteBotIconImage <https://api.mattermost.com/#operation/DeleteBotIconImage>`_
        """

        url = f"/bots/{bot_user_id}/icon"

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

    async def convert_bot_to_user(
        self,
        bot_user_id: str,
        *,
        json_body: ConvertBotToUserJsonBody,
        set_system_admin: Optional[bool] = False,
    ) -> StatusOK:
        """Convert a bot into a user

        Convert a bot into a user.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `ConvertBotToUser <https://api.mattermost.com/#operation/ConvertBotToUser>`_
        """

        url = f"/bots/{bot_user_id}/convert_to_user"
        params: Dict[str, Any] = {
            "set_system_admin": set_system_admin,
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
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response
