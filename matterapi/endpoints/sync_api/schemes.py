from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ...models import (
    Channel,
    CreateSchemeJsonBody,
    PatchSchemeJsonBody,
    Scheme,
    StatusOK,
    Team,
)
from ..base import ApiBaseClass


class SchemesApi(ApiBaseClass):
    """Endpoints for creating, getting and updating and deleting schemes."""

    def get_schemes(
        self,
        *,
        scope: Optional[str] = "",
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Scheme]:
        """Get the schemes.

        Get a page of schemes. Use the query parameters to modify the behaviour
        of this endpoint.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.0
        """

        url = "{}/schemes".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()
        params: Dict[str, Any] = {
            "scope": scope,
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

        response = self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = Scheme.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response

    def create_scheme(
        self,
        *,
        json_body: CreateSchemeJsonBody,
    ) -> Scheme:
        """Create a scheme

        Create a new scheme.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.0
        """

        url = "{}/schemes".format(self.client.base_url)
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

        response = self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 201:
            response_201 = Scheme.parse_obj(response.json())

            return response_201
        return response

    def get_scheme(
        self,
        scheme_id: str,
    ) -> Scheme:
        """Get a scheme

        Get a scheme from the provided scheme id.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.0
        """

        url = "{}/schemes/{scheme_id}".format(self.client.base_url, scheme_id=scheme_id)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = Scheme.parse_obj(response.json())

            return response_200
        return response

    def delete_scheme(
        self,
        scheme_id: str,
    ) -> StatusOK:
        """Delete a scheme

        Soft deletes a scheme, by marking the scheme as deleted in the database.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.0
        """

        url = "{}/schemes/{scheme_id}".format(self.client.base_url, scheme_id=scheme_id)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = self.client.delete(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = StatusOK.parse_obj(response.json())

            return response_200
        return response

    def patch_scheme(
        self,
        scheme_id: str,
        *,
        json_body: PatchSchemeJsonBody,
    ) -> Scheme:
        """Patch a scheme

        Partially update a scheme by providing only the fields you want to
        update. Omitted fields will not be updated. The fields that can be
        updated are defined in the request body, all other provided fields will
        be ignored.

        Permissions:
            `manage_system` permission is required.
        Minimum Server Version:
            5.0
        """

        url = "{}/schemes/{scheme_id}/patch".format(
            self.client.base_url, scheme_id=scheme_id
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

        response = self.client.put(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = Scheme.parse_obj(response.json())

            return response_200
        return response

    def get_teams_for_scheme(
        self,
        scheme_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Team]:
        """Get a page of teams which use this scheme.

        Get a page of teams which use this scheme. The provided Scheme ID should
        be for a Team-scoped Scheme.
        Use the query parameters to modify the behaviour of this endpoint.

        Permissions:
            `manage_system` permission is required.
        Minimum Server Version:
            5.0
        """

        url = "{}/schemes/{scheme_id}/teams".format(
            self.client.base_url, scheme_id=scheme_id
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

        response = self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = Team.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response

    def get_channels_for_scheme(
        self,
        scheme_id: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Channel]:
        """Get a page of channels which use this scheme.

        Get a page of channels which use this scheme. The provided Scheme ID
        should be for a Channel-scoped Scheme.
        Use the query parameters to modify the behaviour of this endpoint.

        Permissions:
            `manage_system` permission is required.
        Minimum Server Version:
            5.0
        """

        url = "{}/schemes/{scheme_id}/channels".format(
            self.client.base_url, scheme_id=scheme_id
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

        response = self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = Channel.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response
