from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from ...models import CreateJobJsonBody, Job, StatusOK
from ..base import ApiBaseClass


class JobsApi(ApiBaseClass):
    """Endpoints related to various background jobs that can be run by the server or separately by job servers."""

    async def get_jobs(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Job]:
        """Get the jobs.

        Get a page of jobs. Use the query parameters to modify the behaviour of this endpoint.

        Permissions:
            Must have `manage_jobs` permission.
        Minimum Server Version:
            4.1
        """

        url = "{}/jobs".format(self.client.base_url)
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
                response_200_item = Job.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
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
        """

        url = "{}/jobs".format(self.client.base_url)
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
            response_201 = Job.parse_obj(response.json())

            return response_201
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
        """

        url = "{}/jobs/{job_id}".format(self.client.base_url, job_id=job_id)
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
            response_200 = Job.parse_obj(response.json())

            return response_200
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
        """

        url = "{}/jobs/{job_id}/download".format(self.client.base_url, job_id=job_id)
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
        """

        url = "{}/jobs/{job_id}/cancel".format(self.client.base_url, job_id=job_id)
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
            response_200 = StatusOK.parse_obj(response.json())

            return response_200
        return response

    async def get_jobs_by_type(
        self,
        type: str,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Job]:
        """Get the jobs of the given type.

        Get a page of jobs of the given type. Use the query parameters to modify the behaviour of this endpoint.

        Permissions:
            Must have `manage_jobs` permission.
        Minimum Server Version:
            4.1
        """

        url = "{}/jobs/type/{type}".format(self.client.base_url, type=type)
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
                response_200_item = Job.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response
