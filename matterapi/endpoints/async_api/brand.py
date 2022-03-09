""" Module to access the Brand endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Dict, Union

from ...models import StatusOK, UploadBrandImageMultipartData
from ..base import ApiBaseClass


class BrandApi(ApiBaseClass):
    """Endpoints related to custom branding and white-labeling. See [our
    branding
    documentation](https://docs.mattermost.com/administration/branding.html)
    for more information."""

    async def get_brand_image(
        self,
    ) -> str:
        """Get brand image

        Get the previously uploaded brand image. Returns 404 if no brand image
        has been uploaded.

        Permissions:
            No permission required.

        Api Reference:
            `GetBrandImage <https://api.mattermost.com/#operation/GetBrandImage>`_
        """

        url = "/brand/image"

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
            response200 = response.json()
            return response200
        return response

    async def upload_brand_image(
        self,
        *,
        multipart_data: Union[UploadBrandImageMultipartData, Dict],
    ) -> StatusOK:
        """Upload brand image

        Uploads a brand image.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `UploadBrandImage <https://api.mattermost.com/#operation/UploadBrandImage>`_
        """

        url = "/brand/image"

        multipart_body_data = UploadBrandImageMultipartData.parse_obj(multipart_data)

        request_kwargs = {
            "url": url,
            "data": multipart_body_data.get_data(),
            "files": multipart_body_data.get_files(),
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 201:
            response201 = StatusOK.parse_obj(response.json())

            return response201
        return response

    async def delete_brand_image(
        self,
    ) -> StatusOK:
        """Delete current brand image

        Deletes the previously uploaded brand image. Returns 404 if no brand
        image has been uploaded.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.6

        Api Reference:
            `DeleteBrandImage <https://api.mattermost.com/#operation/DeleteBrandImage>`_
        """

        url = "/brand/image"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.delete(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response
