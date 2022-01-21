from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ...models import CreateOAuthAppJsonBody, OAuthApp, StatusOK, UpdateOAuthAppJsonBody
from ..base import ApiBaseClass


class OauthApi(ApiBaseClass):
    """Endpoints for configuring and interacting with Mattermost as an OAuth 2.0 service provider."""

    async def get_oauth_apps(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[OAuthApp]:
        """Get OAuth apps

        Get a page of OAuth 2.0 client applications registered with Mattermost.

        Permissions:
            With `manage_oauth` permission, the apps registered by the logged in user are returned. With `manage_system_wide_oauth` permission, all apps regardless of creator are returned.
        """

        url = "{}/oauth/apps".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()
        params: Dict[str, Any] = {
            "page": page,
            "per_page": per_page,
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
                response_200_item = OAuthApp.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response

    async def create_oauth_app(
        self,
        *,
        json_body: CreateOAuthAppJsonBody,
    ) -> OAuthApp:
        """Register OAuth app

        Register an OAuth 2.0 client application with Mattermost as the service provider.

        Permissions:
            Must have `manage_oauth` permission.
        """

        url = "{}/oauth/apps".format(self.client.base_url)
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
            response_201 = OAuthApp.parse_obj(response.json())

            return response_201
        return response

    async def get_oauth_app(
        self,
        app_id: str,
    ) -> OAuthApp:
        """Get an OAuth app

        Get an OAuth 2.0 client application registered with Mattermost.

        Permissions:
            If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission is required.
        """

        url = "{}/oauth/apps/{app_id}".format(self.client.base_url, app_id=app_id)
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
            response_200 = OAuthApp.parse_obj(response.json())

            return response_200
        return response

    async def update_oauth_app(
        self,
        app_id: str,
        *,
        json_body: UpdateOAuthAppJsonBody,
    ) -> OAuthApp:
        """Update an OAuth app

        Update an OAuth 2.0 client application based on OAuth struct.

        Permissions:
            If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission is required.
        """

        url = "{}/oauth/apps/{app_id}".format(self.client.base_url, app_id=app_id)
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
            response_200 = OAuthApp.parse_obj(response.json())

            return response_200
        return response

    async def delete_oauth_app(
        self,
        app_id: str,
    ) -> StatusOK:
        """Delete an OAuth app

        Delete and unregister an OAuth 2.0 client application

        Permissions:
            If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission is required.
        """

        url = "{}/oauth/apps/{app_id}".format(self.client.base_url, app_id=app_id)
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

    async def regenerate_oauth_app_secret(
        self,
        app_id: str,
    ) -> OAuthApp:
        """Regenerate OAuth app secret

        Regenerate the client secret for an OAuth 2.0 client application registered with Mattermost.

        Permissions:
            If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission is required.
        """

        url = "{}/oauth/apps/{app_id}/regen_secret".format(
            self.client.base_url, app_id=app_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = OAuthApp.parse_obj(response.json())

            return response_200
        return response

    async def get_oauth_app_info(
        self,
        app_id: str,
    ) -> OAuthApp:
        """Get info on an OAuth app

        Get public information about an OAuth 2.0 client application registered with Mattermost. The application's client secret will be blanked out.

        Permissions:
            Must be authenticated.
        """

        url = "{}/oauth/apps/{app_id}/info".format(self.client.base_url, app_id=app_id)
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
            response_200 = OAuthApp.parse_obj(response.json())

            return response_200
        return response

    async def get_authorized_oauth_apps_for_user(
        self,
        user_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[OAuthApp]:
        """Get authorized OAuth apps

        Get a page of OAuth 2.0 client applications authorized to access a user's account.

        Permissions:
            Must be authenticated as the user or have `edit_other_users` permission.
        """

        url = "{}/users/{user_id}/oauth/apps/authorized".format(
            self.client.base_url, user_id=user_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()
        params: Dict[str, Any] = {
            "page": page,
            "per_page": per_page,
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
                response_200_item = OAuthApp.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response
