""" Module to access the Files endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from typing import Any, Dict, Optional

from ...models import (
    FileInfo,
    FileInfoList,
    GetFileLinkResponse200,
    SearchFilesMultipartData,
    UploadFileMultipartData,
    UploadFileResponse201,
)
from ..base import ApiBaseClass


class FilesApi(ApiBaseClass):
    """Endpoints for uploading and interacting with files."""

    async def upload_file(
        self,
        *,
        multipart_data: UploadFileMultipartData,
        channel_id: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> UploadFileResponse201:
        """Upload a file

        Uploads a file that can later be attached to a post.

        This request can either be a multipart/form-data request with a
        channel_id, files and optional
        client_ids defined in the FormData, or it can be a request with the
        channel_id and filename
        defined as query parameters with the contents of a single file in the
        body of the request.

        Only multipart/form-data requests are supported by server versions up to
        and including 4.7.
        Server versions 4.8 and higher support both types of requests.

        Permissions:
            Must have `upload_file` permission.

        Api Reference:
            `UploadFile <https://api.mattermost.com/#operation/UploadFile>`_
        """

        url = "/files"
        params: Dict[str, Any] = {
            "channel_id": channel_id,
            "filename": filename,
        }
        params = {k: v for k, v in params.items() if v is not None}

        multipart_body_data = UploadFileMultipartData.parse_obj(multipart_data)

        request_kwargs = {
            "url": url,
            "data": multipart_body_data.get_data(),
            "files": multipart_body_data.get_files(),
            "params": params,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 201:
            response201 = UploadFileResponse201.parse_obj(response.json())

            return response201
        return response

    async def get_file(
        self,
        file_id: str,
    ) -> None:
        """Get a file

        Gets a file that has been uploaded previously.

        Permissions:
            Must have `read_channel` permission or be uploader of the
            file.

        Api Reference:
            `GetFile <https://api.mattermost.com/#operation/GetFile>`_
        """

        url = f"/files/{file_id}"

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

    async def get_file_thumbnail(
        self,
        file_id: str,
    ) -> None:
        """Get a file's thumbnail

        Gets a file's thumbnail.

        Permissions:
            Must have `read_channel` permission or be uploader of the
            file.

        Api Reference:
            `GetFileThumbnail <https://api.mattermost.com/#operation/GetFileThumbnail>`_
        """

        url = f"/files/{file_id}/thumbnail"

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

    async def get_file_preview(
        self,
        file_id: str,
    ) -> None:
        """Get a file's preview

        Gets a file's preview.

        Permissions:
            Must have `read_channel` permission or be uploader of the
            file.

        Api Reference:
            `GetFilePreview <https://api.mattermost.com/#operation/GetFilePreview>`_
        """

        url = f"/files/{file_id}/preview"

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

    async def get_file_link(
        self,
        file_id: str,
    ) -> GetFileLinkResponse200:
        """Get a public file link

        Gets a public link for a file that can be accessed without logging into
        Mattermost.

        Permissions:
            Must have `read_channel` permission or be uploader of the
            file.

        Api Reference:
            `GetFileLink <https://api.mattermost.com/#operation/GetFileLink>`_
        """

        url = f"/files/{file_id}/link"

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
            response200 = GetFileLinkResponse200.parse_obj(response.json())

            return response200
        return response

    async def get_file_info(
        self,
        file_id: str,
    ) -> FileInfo:
        """Get metadata for a file

        Gets a file's info.

        Permissions:
            Must have `read_channel` permission or be uploader of the
            file.

        Api Reference:
            `GetFileInfo <https://api.mattermost.com/#operation/GetFileInfo>`_
        """

        url = f"/files/{file_id}/info"

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
            response200 = FileInfo.parse_obj(response.json())

            return response200
        return response

    async def get_file_public(
        self,
        file_id: str,
        *,
        h: str,
    ) -> None:
        """Get a public file



        Permissions:
            No permissions required.

        Api Reference:
            `GetFilePublic <https://api.mattermost.com/#operation/GetFilePublic>`_
        """

        url = f"/files/{file_id}/public"
        params: Dict[str, Any] = {
            "h": h,
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

        return response

    async def search_files(
        self,
        team_id: str,
        *,
        multipart_data: SearchFilesMultipartData,
    ) -> FileInfoList:
        """Search files in a team

        Search for files in a team based on file name, extention and file
        content (if file content extraction is enabled and supported for the
        files).

        Permissions:
            Must be authenticated and have the `view_team` permission.
        Minimum Server Version:
            5.34

        Api Reference:
            `SearchFiles <https://api.mattermost.com/#operation/SearchFiles>`_
        """

        url = f"/teams/{team_id}/files/search"

        multipart_body_data = SearchFilesMultipartData.parse_obj(multipart_data)

        request_kwargs = {
            "url": url,
            "data": multipart_body_data.get_data(),
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = FileInfoList.parse_obj(response.json())

            return response200
        return response
