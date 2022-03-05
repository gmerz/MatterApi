""" Module to access the Root endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from ...models import PushNotification
from ..base import ApiBaseClass


class RootApi(ApiBaseClass):
    """ """

    async def acknowledge_notification(
        self,
    ) -> PushNotification:
        """Acknowledge receiving of a notification



        Permissions:
            Must be logged in.
        Minimum Server Version:
            3.10

        Api Reference:
            `AcknowledgeNotification <https://api.mattermost.com/#operation/AcknowledgeNotification>`_
        """

        url = "/notifications/ack"

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
            response200 = PushNotification.parse_obj(response.json())

            return response200
        return response
