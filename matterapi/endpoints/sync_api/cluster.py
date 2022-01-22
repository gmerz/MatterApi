from typing import Any, Dict, List

from ...models import ClusterInfo
from ..base import ApiBaseClass


class ClusterApi(ApiBaseClass):
    """Endpoints for configuring and interacting with high availability
    clusters."""

    def get_cluster_status(
        self,
    ) -> List[ClusterInfo]:
        """Get cluster status

        Get a set of information for each node in the cluster, useful for
        checking the status and health of each node.

        Permissions:
            Must have `manage_system` permission.
        """

        url = "{}/cluster/status".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = ClusterInfo.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response
