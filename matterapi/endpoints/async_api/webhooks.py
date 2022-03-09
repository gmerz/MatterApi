""" Module to access the Webhooks endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from ...models import (
    CreateIncomingWebhookJsonBody,
    CreateOutgoingWebhookJsonBody,
    IncomingWebhook,
    OutgoingWebhook,
    StatusOK,
    UpdateIncomingWebhookJsonBody,
    UpdateOutgoingWebhookJsonBody,
)
from ..base import ApiBaseClass


class WebhooksApi(ApiBaseClass):
    """Endpoints for creating, getting and updating webhooks."""

    async def get_incoming_webhooks(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
        team_id: Optional[str] = None,
    ) -> List[IncomingWebhook]:
        """List incoming webhooks

        Get a page of a list of incoming webhooks. Optionally filter for a
        specific team using query parameters.

        Permissions:
            `manage_webhooks` for the system or `manage_webhooks` for
            the specific team.

        Api Reference:
            `GetIncomingWebhooks <https://api.mattermost.com/#operation/GetIncomingWebhooks>`_
        """

        url = "/hooks/incoming"
        params: Dict[str, Any] = {
            "page": page,
            "per_page": per_page,
            "team_id": team_id,
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
                response200_item = IncomingWebhook.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def create_incoming_webhook(
        self,
        *,
        json_body: Union[CreateIncomingWebhookJsonBody, Dict],
    ) -> IncomingWebhook:
        """Create an incoming webhook

        Create an incoming webhook for a channel.

        `manage_others_incoming_webhooks` for the team the webhook is in if the
        user is different than the requester.

        Permissions:
            `manage_webhooks` for the team the webhook is in.

        Api Reference:
            `CreateIncomingWebhook <https://api.mattermost.com/#operation/CreateIncomingWebhook>`_
        """

        url = "/hooks/incoming"

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
            response201 = IncomingWebhook.parse_obj(response.json())

            return response201
        return response

    async def get_incoming_webhook(
        self,
        hook_id: str,
    ) -> IncomingWebhook:
        """Get an incoming webhook

        Get an incoming webhook given the hook id.

        Permissions:
            `manage_webhooks` for system or `manage_webhooks` for the
            specific team or `manage_webhooks` for the channel.

        Api Reference:
            `GetIncomingWebhook <https://api.mattermost.com/#operation/GetIncomingWebhook>`_
        """

        url = f"/hooks/incoming/{hook_id}"

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
            response200 = IncomingWebhook.parse_obj(response.json())

            return response200
        return response

    async def update_incoming_webhook(
        self,
        hook_id: str,
        *,
        json_body: Union[UpdateIncomingWebhookJsonBody, Dict],
    ) -> IncomingWebhook:
        """Update an incoming webhook

        Update an incoming webhook given the hook id.

        Permissions:
            `manage_webhooks` for system or `manage_webhooks` for the
            specific team or `manage_webhooks` for the channel.

        Api Reference:
            `UpdateIncomingWebhook <https://api.mattermost.com/#operation/UpdateIncomingWebhook>`_
        """

        url = f"/hooks/incoming/{hook_id}"

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
            response200 = IncomingWebhook.parse_obj(response.json())

            return response200
        return response

    async def delete_incoming_webhook(
        self,
        hook_id: str,
    ) -> StatusOK:
        """Delete an incoming webhook

        Delete an incoming webhook given the hook id.

        Permissions:
            `manage_webhooks` for system or `manage_webhooks` for the
            specific team or `manage_webhooks` for the channel.

        Api Reference:
            `DeleteIncomingWebhook <https://api.mattermost.com/#operation/DeleteIncomingWebhook>`_
        """

        url = f"/hooks/incoming/{hook_id}"

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

    async def get_outgoing_webhooks(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
        team_id: Optional[str] = None,
        channel_id: Optional[str] = None,
    ) -> List[OutgoingWebhook]:
        """List outgoing webhooks

        Get a page of a list of outgoing webhooks. Optionally filter for a
        specific team or channel using query parameters.

        Permissions:
            `manage_webhooks` for the system or `manage_webhooks` for
            the specific team/channel.

        Api Reference:
            `GetOutgoingWebhooks <https://api.mattermost.com/#operation/GetOutgoingWebhooks>`_
        """

        url = "/hooks/outgoing"
        params: Dict[str, Any] = {
            "page": page,
            "per_page": per_page,
            "team_id": team_id,
            "channel_id": channel_id,
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
                response200_item = OutgoingWebhook.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def create_outgoing_webhook(
        self,
        *,
        json_body: Union[CreateOutgoingWebhookJsonBody, Dict],
    ) -> OutgoingWebhook:
        """Create an outgoing webhook

        Create an outgoing webhook for a team.

        `manage_others_outgoing_webhooks` for the team the webhook is in if the
        user is different than the requester.

        Permissions:
            `manage_webhooks` for the team the webhook is in.

        Api Reference:
            `CreateOutgoingWebhook <https://api.mattermost.com/#operation/CreateOutgoingWebhook>`_
        """

        url = "/hooks/outgoing"

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
            response201 = OutgoingWebhook.parse_obj(response.json())

            return response201
        return response

    async def get_outgoing_webhook(
        self,
        hook_id: str,
    ) -> OutgoingWebhook:
        """Get an outgoing webhook

        Get an outgoing webhook given the hook id.

        Permissions:
            `manage_webhooks` for system or `manage_webhooks` for the
            specific team or `manage_webhooks` for the channel.

        Api Reference:
            `GetOutgoingWebhook <https://api.mattermost.com/#operation/GetOutgoingWebhook>`_
        """

        url = f"/hooks/outgoing/{hook_id}"

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
            response200 = OutgoingWebhook.parse_obj(response.json())

            return response200
        return response

    async def update_outgoing_webhook(
        self,
        hook_id: str,
        *,
        json_body: Union[UpdateOutgoingWebhookJsonBody, Dict],
    ) -> OutgoingWebhook:
        """Update an outgoing webhook

        Update an outgoing webhook given the hook id.

        Permissions:
            `manage_webhooks` for system or `manage_webhooks` for the
            specific team or `manage_webhooks` for the channel.

        Api Reference:
            `UpdateOutgoingWebhook <https://api.mattermost.com/#operation/UpdateOutgoingWebhook>`_
        """

        url = f"/hooks/outgoing/{hook_id}"

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
            response200 = OutgoingWebhook.parse_obj(response.json())

            return response200
        return response

    async def delete_outgoing_webhook(
        self,
        hook_id: str,
    ) -> StatusOK:
        """Delete an outgoing webhook

        Delete an outgoing webhook given the hook id.

        Permissions:
            `manage_webhooks` for system or `manage_webhooks` for the
            specific team or `manage_webhooks` for the channel.

        Api Reference:
            `DeleteOutgoingWebhook <https://api.mattermost.com/#operation/DeleteOutgoingWebhook>`_
        """

        url = f"/hooks/outgoing/{hook_id}"

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

    async def regen_outgoing_hook_token(
        self,
        hook_id: str,
    ) -> StatusOK:
        """Regenerate the token for the outgoing webhook.

        Regenerate the token for the outgoing webhook.

        Permissions:
            `manage_webhooks` for system or `manage_webhooks` for the
            specific team or `manage_webhooks` for the channel.

        Api Reference:
            `RegenOutgoingHookToken <https://api.mattermost.com/#operation/RegenOutgoingHookToken>`_
        """

        url = f"/hooks/outgoing/{hook_id}/regen_token"

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
