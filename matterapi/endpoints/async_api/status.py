from typing import Any, Dict, List

from pydantic import BaseModel

from ...models import (
    PostUserRecentCustomStatusDeleteJsonBody,
    RemoveRecentCustomStatusJsonBody,
    Status,
    UpdateUserCustomStatusJsonBody,
    UpdateUserStatusJsonBody,
)
from ..base import ApiBaseClass


class StatusApi(ApiBaseClass):
    """Endpoints for getting and updating user statuses."""

    async def get_user_status(
        self,
        user_id: str,
    ) -> Status:
        """Get user status

        Get user status by id from the server.

        Permissions:
            Must be authenticated.
        """

        url = "{}/users/{user_id}/status".format(self.client.base_url, user_id=user_id)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = Status.parse_obj(response.json())

            return response_200
        return response

    async def update_user_status(
        self,
        user_id: str,
        *,
        json_body: UpdateUserStatusJsonBody,
    ) -> Status:
        """Update user status

        Manually set a user's status. When setting a user's status, the status
        will remain that value until set \"online\" again, which will return the
        status to being automatically updated based on user activity.

        Permissions:
            Must have `edit_other_users` permission for the team.
        """

        url = "{}/users/{user_id}/status".format(self.client.base_url, user_id=user_id)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "json": json_json_body,
        }

        response = await self.client.put(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = Status.parse_obj(response.json())

            return response_200
        return response

    async def get_users_statuses_by_ids(
        self,
        *,
        json_body: List[str],
    ) -> List[Status]:
        """Get user statuses by id

        Get a list of user statuses by id from the server.

        Permissions:
            Must be authenticated.
        """

        url = "{}/users/status/ids".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()
        json_json_body = json_body

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "json": json_json_body,
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = Status.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response

    async def update_user_custom_status(
        self,
        user_id: str,
        *,
        json_body: UpdateUserCustomStatusJsonBody,
    ) -> None:
        """Update user custom status

        Updates a user's custom status by setting the value in the user's props
        and updates the user. Also save the given custom status to the recent
        custom statuses in the user's props

        Permissions:
            Must be logged in as the user whose custom status is being updated.
        """

        url = "{}/users/{user_id}/status/custom".format(
            self.client.base_url, user_id=user_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "json": json_json_body,
        }

        response = await self.client.put(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        return response

    async def unset_user_custom_status(
        self,
        user_id: str,
    ) -> None:
        """Unsets user custom status

        Unsets a user's custom status by updating the user's props and updates
        the user

        Permissions:
            Must be logged in as the user whose custom status is being removed.
        """

        url = "{}/users/{user_id}/status/custom".format(
            self.client.base_url, user_id=user_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.delete(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        return response

    async def remove_recent_custom_status(
        self,
        user_id: str,
        *,
        json_body: RemoveRecentCustomStatusJsonBody,
    ) -> None:
        """Delete user's recent custom status

        Deletes a user's recent custom status by removing the specific status
        from the recentCustomStatuses in the user's props and updates the user.

        Permissions:
            Must be logged in as the user whose recent custom status is being
        deleted.
        """

        url = "{}/users/{user_id}/status/custom/recent".format(
            self.client.base_url, user_id=user_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "json": json_json_body,
        }

        response = await self.client.delete(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        return response

    async def post_user_recent_custom_status_delete(
        self,
        user_id: str,
        *,
        json_body: PostUserRecentCustomStatusDeleteJsonBody,
    ) -> None:
        """Delete user's recent custom status

        Deletes a user's recent custom status by removing the specific status
        from the recentCustomStatuses in the user's props and updates the user.

        Permissions:
            Must be logged in as the user whose recent custom status is being
        deleted.
        """

        url = "{}/users/{user_id}/status/custom/recent/delete".format(
            self.client.base_url, user_id=user_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "json": json_json_body,
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        return response
