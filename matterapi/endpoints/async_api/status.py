""" Module to access the Status endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Dict, List, Union

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

        Api Reference:
            `GetUserStatus <https://api.mattermost.com/#operation/GetUserStatus>`_
        """

        url = f"/users/{user_id}/status"

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
            response200 = Status.parse_obj(response.json())

            return response200
        return response

    async def update_user_status(
        self,
        user_id: str,
        *,
        json_body: Union[UpdateUserStatusJsonBody, Dict],
    ) -> Status:
        """Update user status

        Manually set a user's status. When setting a user's status, the status
        will remain that value until set \"online\" again, which will return the
        status to being automatically updated based on user activity.

        Permissions:
            Must have `edit_other_users` permission for the team.

        Api Reference:
            `UpdateUserStatus <https://api.mattermost.com/#operation/UpdateUserStatus>`_
        """

        url = f"/users/{user_id}/status"

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
            response = await httpx_client.put(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = Status.parse_obj(response.json())

            return response200
        return response

    async def get_users_statuses_by_ids(
        self,
        *,
        json_body: Union[List[str], Dict],
    ) -> List[Status]:
        """Get user statuses by id

        Get a list of user statuses by id from the server.

        Permissions:
            Must be authenticated.

        Api Reference:
            `GetUsersStatusesByIds <https://api.mattermost.com/#operation/GetUsersStatusesByIds>`_
        """

        url = "/users/status/ids"
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
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = Status.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    async def update_user_custom_status(
        self,
        user_id: str,
        *,
        json_body: Union[UpdateUserCustomStatusJsonBody, Dict],
    ) -> None:
        """Update user custom status

        Updates a user's custom status by setting the value in the user's props
        and updates the user. Also save the given custom status to the recent
        custom statuses in the user's props

        Permissions:
            Must be logged in as the user whose custom status is being
            updated.

        Api Reference:
            `UpdateUserCustomStatus <https://api.mattermost.com/#operation/UpdateUserCustomStatus>`_
        """

        url = f"/users/{user_id}/status/custom"

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
            response = await httpx_client.put(
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
            Must be logged in as the user whose custom status is being
            removed.

        Api Reference:
            `UnsetUserCustomStatus <https://api.mattermost.com/#operation/UnsetUserCustomStatus>`_
        """

        url = f"/users/{user_id}/status/custom"

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

        return response

    async def remove_recent_custom_status(
        self,
        user_id: str,
        *,
        json_body: Union[RemoveRecentCustomStatusJsonBody, Dict],
    ) -> None:
        """Delete user's recent custom status

        Deletes a user's recent custom status by removing the specific status
        from the recentCustomStatuses in the user's props and updates the user.

        Permissions:
            Must be logged in as the user whose recent custom status is
            being deleted.

        Api Reference:
            `RemoveRecentCustomStatus <https://api.mattermost.com/#operation/RemoveRecentCustomStatus>`_
        """

        url = f"/users/{user_id}/status/custom/recent"

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
            response = await httpx_client.delete(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        return response

    async def post_user_recent_custom_status_delete(
        self,
        user_id: str,
        *,
        json_body: Union[PostUserRecentCustomStatusDeleteJsonBody, Dict],
    ) -> None:
        """Delete user's recent custom status

        Deletes a user's recent custom status by removing the specific status
        from the recentCustomStatuses in the user's props and updates the user.

        Permissions:
            Must be logged in as the user whose recent custom status is
            being deleted.

        Api Reference:
            `PostUserRecentCustomStatusDelete <https://api.mattermost.com/#operation/PostUserRecentCustomStatusDelete>`_
        """

        url = f"/users/{user_id}/status/custom/recent/delete"

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

        return response
