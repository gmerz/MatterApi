""" Module to access the Jobs endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ...models import CreateJobJsonBody, Job, StatusOK
from ..base import ApiBaseClass


class JobsApi(ApiBaseClass):
    """Endpoints related to various background jobs that can be run by the
    server or separately by job servers."""

    async def get_jobs(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Job]:
        """Get the jobs.

        Get a page of jobs. Use the query parameters to modify the behaviour of
        this endpoint.

        Permissions:
            Must have `manage_jobs` permission.
        Minimum Server Version:
            4.1

        Api Reference:
            `GetJobs <https://api.mattermost.com/#operation/GetJobs>`_
        """

        url = "/jobs"
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
                response200_item = Job.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def create_job(
        self,
        *,
        json_body: CreateJobJsonBody,
    ) -> Job:
        """Create a new job.

        Create a new job.

        Permissions:
            Must have `manage_jobs` permission.
        Minimum Server Version:
            4.1

        Api Reference:
            `CreateJob <https://api.mattermost.com/#operation/CreateJob>`_
        """

        url = "/jobs"

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
            response201 = Job.parse_obj(response.json())

            return response201
        return response

    async def get_job(
        self,
        job_id: str,
    ) -> Job:
        """Get a job.

        Gets a single job.

        Permissions:
            Must have `manage_jobs` permission.
        Minimum Server Version:
            4.1

        Api Reference:
            `GetJob <https://api.mattermost.com/#operation/GetJob>`_
        """

        url = f"/jobs/{job_id}"

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
            response200 = Job.parse_obj(response.json())

            return response200
        return response

    async def download_job(
        self,
        job_id: str,
    ) -> None:
        """Download the results of a job.

        Download the result of a single job.

        Permissions:
            Must have `manage_jobs` permission.
        Minimum Server Version:
            5.28

        Api Reference:
            `DownloadJob <https://api.mattermost.com/#operation/DownloadJob>`_
        """

        url = f"/jobs/{job_id}/download"

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

    async def cancel_job(
        self,
        job_id: str,
    ) -> StatusOK:
        """Cancel a job.

        Cancel a job.

        Permissions:
            Must have `manage_jobs` permission.
        Minimum Server Version:
            4.1

        Api Reference:
            `CancelJob <https://api.mattermost.com/#operation/CancelJob>`_
        """

        url = f"/jobs/{job_id}/cancel"

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

    async def get_jobs_by_type(
        self,
        type: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Job]:
        """Get the jobs of the given type.

        Get a page of jobs of the given type. Use the query parameters to modify
        the behaviour of this endpoint.

        Permissions:
            Must have `manage_jobs` permission.
        Minimum Server Version:
            4.1

        Api Reference:
            `GetJobsByType <https://api.mattermost.com/#operation/GetJobsByType>`_
        """

        url = f"/jobs/type/{type}"
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
                response200_item = Job.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response
