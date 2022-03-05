""" Module to access the Bleve endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from ...models import StatusOK
from ..base import ApiBaseClass


class BleveApi(ApiBaseClass):
    """ """

    def purge_bleve_indexes(
        self,
    ) -> StatusOK:
        """Purge all Bleve indexes

        Deletes all Bleve indexes and their contents. After calling this
        endpoint, it is
        necessary to schedule a new Bleve indexing job to repopulate the
        indexes.

        Permissions:
            Must have `sysconsole_write_experimental` permission.
        Minimum Server Version:
            5.24

        Api Reference:
            `PurgeBleveIndexes <https://api.mattermost.com/#operation/PurgeBleveIndexes>`_
        """

        url = "/bleve/purge_indexes"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response
