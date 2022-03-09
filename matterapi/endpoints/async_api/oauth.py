""" Module to access the Oauth endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from ...models import CreateOAuthAppJsonBody, OAuthApp, StatusOK, UpdateOAuthAppJsonBody
from ..base import ApiBaseClass


class OauthApi(ApiBaseClass):
    """Endpoints for configuring and interacting with Mattermost as an OAuth
    2.0 service provider."""

    async def get_oauth_apps(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[OAuthApp]:
        """Get OAuth apps

        Get a page of OAuth 2.0 client applications registered with Mattermost.

        Permissions:
            With `manage_oauth` permission, the apps registered by the
            logged in user are returned. With `manage_system_wide_oauth`
            permission, all apps regardless of creator are returned.

        Api Reference:
            `GetOAuthApps <https://api.mattermost.com/#operation/GetOAuthApps>`_
        """

        url = "/oauth/apps"
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
                response200_item = OAuthApp.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def create_oauth_app(
        self,
        *,
        json_body: Union[CreateOAuthAppJsonBody, Dict],
    ) -> OAuthApp:
        """Register OAuth app

        Register an OAuth 2.0 client application with Mattermost as the service
        provider.

        Permissions:
            Must have `manage_oauth` permission.

        Api Reference:
            `CreateOAuthApp <https://api.mattermost.com/#operation/CreateOAuthApp>`_
        """

        url = "/oauth/apps"

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
            response201 = OAuthApp.parse_obj(response.json())

            return response201
        return response

    async def get_oauth_app(
        self,
        app_id: str,
    ) -> OAuthApp:
        """Get an OAuth app

        Get an OAuth 2.0 client application registered with Mattermost.

        Permissions:
            If app creator, must have `mange_oauth` permission otherwise
            `manage_system_wide_oauth` permission is required.

        Api Reference:
            `GetOAuthApp <https://api.mattermost.com/#operation/GetOAuthApp>`_
        """

        url = f"/oauth/apps/{app_id}"

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
            response200 = OAuthApp.parse_obj(response.json())

            return response200
        return response

    async def update_oauth_app(
        self,
        app_id: str,
        *,
        json_body: Union[UpdateOAuthAppJsonBody, Dict],
    ) -> OAuthApp:
        """Update an OAuth app

        Update an OAuth 2.0 client application based on OAuth struct.

        Permissions:
            If app creator, must have `mange_oauth` permission otherwise
            `manage_system_wide_oauth` permission is required.

        Api Reference:
            `UpdateOAuthApp <https://api.mattermost.com/#operation/UpdateOAuthApp>`_
        """

        url = f"/oauth/apps/{app_id}"

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
            response200 = OAuthApp.parse_obj(response.json())

            return response200
        return response

    async def delete_oauth_app(
        self,
        app_id: str,
    ) -> StatusOK:
        """Delete an OAuth app

        Delete and unregister an OAuth 2.0 client application

        Permissions:
            If app creator, must have `mange_oauth` permission otherwise
            `manage_system_wide_oauth` permission is required.

        Api Reference:
            `DeleteOAuthApp <https://api.mattermost.com/#operation/DeleteOAuthApp>`_
        """

        url = f"/oauth/apps/{app_id}"

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

    async def regenerate_oauth_app_secret(
        self,
        app_id: str,
    ) -> OAuthApp:
        """Regenerate OAuth app secret

        Regenerate the client secret for an OAuth 2.0 client application
        registered with Mattermost.

        Permissions:
            If app creator, must have `mange_oauth` permission otherwise
            `manage_system_wide_oauth` permission is required.

        Api Reference:
            `RegenerateOAuthAppSecret <https://api.mattermost.com/#operation/RegenerateOAuthAppSecret>`_
        """

        url = f"/oauth/apps/{app_id}/regen_secret"

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
            response200 = OAuthApp.parse_obj(response.json())

            return response200
        return response

    async def get_oauth_app_info(
        self,
        app_id: str,
    ) -> OAuthApp:
        """Get info on an OAuth app

        Get public information about an OAuth 2.0 client application registered
        with Mattermost. The application's client secret will be blanked out.

        Permissions:
            Must be authenticated.

        Api Reference:
            `GetOAuthAppInfo <https://api.mattermost.com/#operation/GetOAuthAppInfo>`_
        """

        url = f"/oauth/apps/{app_id}/info"

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
            response200 = OAuthApp.parse_obj(response.json())

            return response200
        return response

    async def get_authorized_oauth_apps_for_user(
        self,
        user_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[OAuthApp]:
        """Get authorized OAuth apps

        Get a page of OAuth 2.0 client applications authorized to access a
        user's account.

        Permissions:
            Must be authenticated as the user or have `edit_other_users`
            permission.

        Api Reference:
            `GetAuthorizedOAuthAppsForUser <https://api.mattermost.com/#operation/GetAuthorizedOAuthAppsForUser>`_
        """

        url = f"/users/{user_id}/oauth/apps/authorized"
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
                response200_item = OAuthApp.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response
