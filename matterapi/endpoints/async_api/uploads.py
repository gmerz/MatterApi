""" Module to access the Uploads endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Dict, Union

from pydantic import BaseModel

from ...models import CreateUploadJsonBody, FileInfo, UploadDataFormData, UploadSession
from ..base import ApiBaseClass


class UploadsApi(ApiBaseClass):
    """Endpoints for creating and performing file uploads."""

    async def create_upload(
        self,
        *,
        json_body: Union[CreateUploadJsonBody, Dict],
    ) -> UploadSession:
        """Create an upload

        Creates a new upload session.

        Permissions:
            Must have `upload_file` permission.
        Minimum Server Version:
            5.28

        Api Reference:
            `CreateUpload <https://api.mattermost.com/#operation/CreateUpload>`_
        """

        url = "/uploads"

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
            response201 = UploadSession.parse_obj(response.json())

            return response201
        return response

    async def get_upload(
        self,
        upload_id: str,
    ) -> None:
        """Get an upload session

        Gets an upload session that has been previously created.

        Permissions:
            Must be logged in as the user who created the upload
            session.

        Api Reference:
            `GetUpload <https://api.mattermost.com/#operation/GetUpload>`_
        """

        url = f"/uploads/{upload_id}"

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

    async def upload_data(
        self,
        upload_id: str,
        *,
        form_data: UploadDataFormData,
    ) -> Union[FileInfo, None]:
        """Perform a file upload

        Starts or resumes a file upload.
        To resume an existing (incomplete) upload, data should be sent starting
        from the offset specified in the upload session object.

        The request body can be in one of two formats:
        - Binary file content streamed in request's body
        - multipart/form-data

        Permissions:
            Must be logged in as the user who created the upload
            session.

        Api Reference:
            `UploadData <https://api.mattermost.com/#operation/UploadData>`_
        """

        url = f"/uploads/{upload_id}"

        request_kwargs = {
            "url": url,
            "data": form_data,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 201:
            response201 = FileInfo.parse_obj(response.json())

            return response201
        return response
