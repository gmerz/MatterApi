""" Module to access the Roles endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from typing import List

from pydantic import BaseModel

from ...models import PatchRoleJsonBody, Role
from ..base import ApiBaseClass


class RolesApi(ApiBaseClass):
    """Endpoints for creating, getting and updating roles."""

    def get_all_roles(
        self,
    ) -> List[Role]:
        """Get a list of all the roles



        Permissions:
            `manage_system` permission is required.
        Minimum Server Version:
            5.33

        Api Reference:
            `GetAllRoles <https://api.mattermost.com/#operation/GetAllRoles>`_
        """

        url = "/roles"

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
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = Role.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def get_role(
        self,
        role_id: str,
    ) -> Role:
        """Get a role

        Get a role from the provided role id.

        Permissions:
            Requires an active session but no other permissions.
        Minimum Server Version:
            4.9

        Api Reference:
            `GetRole <https://api.mattermost.com/#operation/GetRole>`_
        """

        url = f"/roles/{role_id}"

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
            response200 = Role.parse_obj(response.json())

            return response200
        return response

    def get_role_by_name(
        self,
        role_name: str,
    ) -> Role:
        """Get a role

        Get a role from the provided role name.

        Permissions:
            Requires an active session but no other permissions.
        Minimum Server Version:
            4.9

        Api Reference:
            `GetRoleByName <https://api.mattermost.com/#operation/GetRoleByName>`_
        """

        url = f"/roles/name/{role_name}"

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
            response200 = Role.parse_obj(response.json())

            return response200
        return response

    def patch_role(
        self,
        role_id: str,
        *,
        json_body: PatchRoleJsonBody,
    ) -> Role:
        """Patch a role

        Partially update a role by providing only the fields you want to update.
        Omitted fields will not be updated. The fields that can be updated are
        defined in the request body, all other provided fields will be ignored.

        Permissions:
            `manage_system` permission is required.
        Minimum Server Version:
            4.9

        Api Reference:
            `PatchRole <https://api.mattermost.com/#operation/PatchRole>`_
        """

        url = f"/roles/{role_id}/patch"

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
            response = httpx_client.put(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = Role.parse_obj(response.json())

            return response200
        return response

    def get_roles_by_names(
        self,
        *,
        json_body: List[str],
    ) -> List[Role]:
        """Get a list of roles by name

        Get a list of roles from their names.

        Permissions:
            Requires an active session but no other permissions.
        Minimum Server Version:
            4.9

        Api Reference:
            `GetRolesByNames <https://api.mattermost.com/#operation/GetRolesByNames>`_
        """

        url = "/roles/names"
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
                response200_item = Role.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response
