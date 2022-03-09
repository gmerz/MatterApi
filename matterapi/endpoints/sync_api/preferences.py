""" Module to access the Preferences endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Dict, List, Union

from pydantic import BaseModel

from ...models import Preference, StatusOK
from ..base import ApiBaseClass


class PreferencesApi(ApiBaseClass):
    """Endpoints for saving and modifying user preferences."""

    def get_preferences(
        self,
        user_id: str,
    ) -> List[Preference]:
        """Get the user's preferences

        Get a list of the user's preferences.

        Permissions:
            Must be logged in as the user being updated or have the
            `edit_other_users` permission.

        Api Reference:
            `GetPreferences <https://api.mattermost.com/#operation/GetPreferences>`_
        """

        url = f"/users/{user_id}/preferences"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = Preference.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def update_preferences(
        self,
        user_id: str,
        *,
        json_body: Union[List[Preference], Dict],
    ) -> StatusOK:
        """Save the user's preferences

        Save a list of the user's preferences.

        Permissions:
            Must be logged in as the user being updated or have the
            `edit_other_users` permission.

        Api Reference:
            `UpdatePreferences <https://api.mattermost.com/#operation/UpdatePreferences>`_
        """

        url = f"/users/{user_id}/preferences"
        json_json_body = []
        for json_body_item_data in json_body:

            if isinstance(json_body_item_data, BaseModel):
                json_body_item = json_body_item_data.dict(exclude_unset=True)
            else:
                json_body_item = json_body_item_data

            json_json_body.append(json_body_item)

        request_kwargs = {
            "url": url,
            "json": json_json_body,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.put(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def delete_preferences(
        self,
        user_id: str,
        *,
        json_body: Union[List[Preference], Dict],
    ) -> StatusOK:
        """Delete user's preferences

        Delete a list of the user's preferences.

        Permissions:
            Must be logged in as the user being updated or have the
            `edit_other_users` permission.

        Api Reference:
            `DeletePreferences <https://api.mattermost.com/#operation/DeletePreferences>`_
        """

        url = f"/users/{user_id}/preferences/delete"
        json_json_body = []
        for json_body_item_data in json_body:

            if isinstance(json_body_item_data, BaseModel):
                json_body_item = json_body_item_data.dict(exclude_unset=True)
            else:
                json_body_item = json_body_item_data

            json_json_body.append(json_body_item)

        request_kwargs = {
            "url": url,
            "json": json_json_body,
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

    def get_preferences_by_category(
        self,
        user_id: str,
        category: str,
    ) -> List[Preference]:
        """List a user's preferences by category

        Lists the current user's stored preferences in the given category.

        Permissions:
            Must be logged in as the user being updated or have the
            `edit_other_users` permission.

        Api Reference:
            `GetPreferencesByCategory <https://api.mattermost.com/#operation/GetPreferencesByCategory>`_
        """

        url = f"/users/{user_id}/preferences/{category}"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = Preference.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def get_preferences_by_category_by_name(
        self,
        user_id: str,
        category: str,
        preference_name: str,
    ) -> Preference:
        """Get a specific user preference

        Gets a single preference for the current user with the given category
        and name.

        Permissions:
            Must be logged in as the user being updated or have the
            `edit_other_users` permission.

        Api Reference:
            `GetPreferencesByCategoryByName <https://api.mattermost.com/#operation/GetPreferencesByCategoryByName>`_
        """

        url = f"/users/{user_id}/preferences/{category}/name/{preference_name}"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = Preference.parse_obj(response.json())

            return response200
        return response
