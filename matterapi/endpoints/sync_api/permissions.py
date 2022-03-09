""" Module to access the Permissions endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Any, Dict, List, Optional, cast

from ..base import ApiBaseClass


class PermissionsApi(ApiBaseClass):
    """ """

    def get_ancillary_permissions(
        self,
        *,
        subsection_permissions: Optional[str] = None,
    ) -> List[str]:
        """Return all system console subsection ancillary permissions

        Returns all the ancillary permissions for the corresponding system
        console subsection permissions appended to the requested permission
        subsections.

        Minimum Server Version:
            5.35

        Api Reference:
            `GetAncillaryPermissions <https://api.mattermost.com/#operation/GetAncillaryPermissions>`_
        """

        url = "/permissions/ancillary"
        params: Dict[str, Any] = {
            "subsection_permissions": subsection_permissions,
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
            response200 = cast(List[str], response.json())

            return response200
        return response
