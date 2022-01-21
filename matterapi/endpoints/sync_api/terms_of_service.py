from typing import Any, Dict, Union

from pydantic import BaseModel

from ...models import (
    AppError,
    RegisterTermsOfServiceActionJsonBody,
    StatusOK,
    TermsOfService,
    UserTermsOfService,
)
from ..base import ApiBaseClass


class TermsOfServiceApi(ApiBaseClass):
    """Endpoints for getting and updating custom terms of service."""

    def get_user_terms_of_service(
        self,
        user_id: str,
    ) -> Union[AppError, UserTermsOfService]:
        """Fetches user's latest terms of service action if the latest action was for acceptance.

        Will be deprecated in v6.0
        Fetches user's latest terms of service action if the latest action was for acceptance.

        Permissions:
            Must be logged in as the user being acted on.
        Minimum Server Version:
            5.6
        """

        url = "{}/users/{user_id}/terms_of_service".format(
            self.client.base_url, user_id=user_id
        )
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

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = UserTermsOfService.parse_obj(response.json())

            return response_200
        if response.status_code == 404:
            response_404 = AppError.parse_obj(response.json())

            return response_404
        return response

    def register_terms_of_service_action(
        self,
        user_id: str,
        *,
        json_body: RegisterTermsOfServiceActionJsonBody,
    ) -> StatusOK:
        """Records user action when they accept or decline custom terms of service

        Records user action when they accept or decline custom terms of service. Records the action in audit table.
        Updates user's last accepted terms of service ID if they accepted it.

        Permissions:
            Must be logged in as the user being acted on.
        Minimum Server Version:
            5.4
        """

        url = "{}/users/{user_id}/terms_of_service".format(
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

        response = self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = StatusOK.parse_obj(response.json())

            return response_200
        return response

    def get_terms_of_service(
        self,
    ) -> TermsOfService:
        """Get latest terms of service

        Get latest terms of service from the server

        Permissions:
            Must be authenticated.
        Minimum Server Version:
            5.4
        """

        url = "{}/terms_of_service".format(self.client.base_url)
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

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = TermsOfService.parse_obj(response.json())

            return response_200
        return response

    def create_terms_of_service(
        self,
    ) -> TermsOfService:
        """Creates a new terms of service

        Creates new terms of service

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.4
        """

        url = "{}/terms_of_service".format(self.client.base_url)
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
            response_200 = TermsOfService.parse_obj(response.json())

            return response_200
        return response
