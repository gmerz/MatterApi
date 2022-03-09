""" Module to access the OpenGraph endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Dict, Union

from pydantic import BaseModel

from ...models import OpenGraph, OpenGraphJsonBody
from ..base import ApiBaseClass


class OpenGraphApi(ApiBaseClass):
    """Endpoint for getting Open Graph metadata."""

    async def open_graph(
        self,
        *,
        json_body: Union[OpenGraphJsonBody, Dict],
    ) -> OpenGraph:
        """Get open graph metadata for url

        Get Open Graph Metadata for a specif URL. Use the Open Graph protocol to
        get some generic metadata about a URL. Used for creating link previews.

        Permissions:
            No permission required but must be logged in.
        Minimum Server Version:
            3.10

        Api Reference:
            `OpenGraph <https://api.mattermost.com/#operation/OpenGraph>`_
        """

        url = "/opengraph"

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

        if response.status_code == 200:
            response200 = OpenGraph.parse_obj(response.json())

            return response200
        return response
