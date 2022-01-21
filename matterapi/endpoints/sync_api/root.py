from typing import Any, Dict

from ...models import PushNotification
from ..base import ApiBaseClass


class RootApi(ApiBaseClass):
    """None"""

    def acknowledge_notification(
        self,
    ) -> PushNotification:
        """Acknowledge receiving of a notification



        Permissions:
            Must be logged in.
        Minimum Server Version:
            3.10
        """

        url = "{}/notifications/ack".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = PushNotification.parse_obj(response.json())

            return response_200
        return response
