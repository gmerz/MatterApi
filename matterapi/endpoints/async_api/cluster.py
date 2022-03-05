""" Module to access the Cluster endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from typing import List

from ...models import ClusterInfo
from ..base import ApiBaseClass


class ClusterApi(ApiBaseClass):
    """Endpoints for configuring and interacting with high availability
    clusters."""

    async def get_cluster_status(
        self,
    ) -> List[ClusterInfo]:
        """Get cluster status

        Get a set of information for each node in the cluster, useful for
        checking the status and health of each node.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `GetClusterStatus <https://api.mattermost.com/#operation/GetClusterStatus>`_
        """

        url = "/cluster/status"

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
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = ClusterInfo.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response
