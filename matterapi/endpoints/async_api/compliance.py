""" Module to access the Compliance endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Any, Dict, List, Optional

from ...models import Compliance
from ..base import ApiBaseClass


class ComplianceApi(ApiBaseClass):
    """Endpoints for creating, getting and downloading compliance reports."""

    async def get_compliance_reports(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Compliance]:
        """Get reports

        Get a list of compliance reports previously created by page, selected
        with `page` and `per_page` query parameters.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `GetComplianceReports <https://api.mattermost.com/#operation/GetComplianceReports>`_
        """

        url = "/compliance/reports"
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
                response200_item = Compliance.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def create_compliance_report(
        self,
    ) -> Compliance:
        """Create report

        Create and save a compliance report.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `CreateComplianceReport <https://api.mattermost.com/#operation/CreateComplianceReport>`_
        """

        url = "/compliance/reports"

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

        if response.status_code == 201:
            response201 = Compliance.parse_obj(response.json())

            return response201
        return response

    async def get_compliance_report(
        self,
        report_id: str,
    ) -> Compliance:
        """Get a report

        Get a compliance reports previously created.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `GetComplianceReport <https://api.mattermost.com/#operation/GetComplianceReport>`_
        """

        url = f"/compliance/reports/{report_id}"

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
            response200 = Compliance.parse_obj(response.json())

            return response200
        return response

    async def download_compliance_report(
        self,
        report_id: str,
    ) -> None:
        """Download a report

        Download the full contents of a report as a file.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `DownloadComplianceReport <https://api.mattermost.com/#operation/DownloadComplianceReport>`_
        """

        url = f"/compliance/reports/{report_id}/download"

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
