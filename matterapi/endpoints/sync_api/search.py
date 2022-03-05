""" Module to access the Search endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from ...models import FileInfoList, SearchFilesMultipartData
from ..base import ApiBaseClass


class SearchApi(ApiBaseClass):
    """ """

    def search_files(
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
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = FileInfoList.parse_obj(response.json())

            return response200
        return response
