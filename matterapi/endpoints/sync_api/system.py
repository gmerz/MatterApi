""" Module to access the System endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Any, Dict, List, Optional, Union, cast

from pydantic import BaseModel

from ...models import (
    Audit,
    Config,
    EnvironmentConfig,
    IntegrityCheckResult,
    LicenseRenewalLink,
    Notice,
    PostLogJsonBody,
    PostLogResponse200,
    PushNotification,
    RequestTrialLicenseJsonBody,
    SendWarnMetricAckJsonBody,
    Server_Busy,
    StatusOK,
    System,
    SystemStatusResponse,
    TestSiteURLJsonBody,
    UpgradeToEnterpriseStatusResponse200,
    UploadLicenseFileMultipartData,
)
from ..base import ApiBaseClass


class SystemApi(ApiBaseClass):
    """General endpoints for interacting with the server, such as configuration
    and logging."""

    def get_supported_timezone(
        self,
    ) -> List[str]:
        """Retrieve a list of supported timezones



        Permissions:
            Must be logged in.
        Minimum Server Version:
            3.10

        Api Reference:
            `GetSupportedTimezone <https://api.mattermost.com/#operation/GetSupportedTimezone>`_
        """

        url = "/system/timezones"

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
            response200 = cast(List[str], response.json())

            return response200
        return response

    def get_ping(
        self,
        *,
        get_server_status: Optional[bool] = None,
        device_id: Optional[str] = None,
    ) -> SystemStatusResponse:
        """Check system health

        Check if the server is up and healthy based on the configuration setting
        `GoRoutineHealthThreshold`. If `GoRoutineHealthThreshold` and the number
        of goroutines on the server exceeds that threshold the server is
        considered unhealthy. If `GoRoutineHealthThreshold` is not set or the
        number of goroutines is below the threshold the server is considered
        healthy.
        If a \"device_id\" is passed in the query, it will test the Push
        Notification Proxy in order to discover whether the device is able to
        receive notifications. The response will have a
        \"CanReceiveNotifications\" property with one of the following values: -
        true: It can receive notifications - false: It cannot receive
        notifications - unknown: There has been an unknown error, and it is not
        certain whether it can
          receive notifications.

        Permissions:
            None.
        Minimum Server Version:
            3.10

        Api Reference:
            `GetPing <https://api.mattermost.com/#operation/GetPing>`_
        """

        url = "/system/ping"
        params: Dict[str, Any] = {
            "get_server_status": get_server_status,
            "device_id": device_id,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = SystemStatusResponse.parse_obj(response.json())

            return response200
        return response

    def get_notices(
        self,
        team_id: str,
        *,
        client_version: str,
        locale: Optional[str] = None,
        client: str,
    ) -> List[Notice]:
        """Get notices for logged in user in specified team

        Will return appropriate product notices for current user in the team
        specified by teamId parameter.

        Permissions:
            Must be logged in.
        Minimum Server Version:
            5.26

        Api Reference:
            `GetNotices <https://api.mattermost.com/#operation/GetNotices>`_
        """

        url = f"/system/notices/{teamId}"
        params: Dict[str, Any] = {
            "clientVersion": client_version,
            "locale": locale,
            "client": client,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
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
                response200_item = Notice.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def mark_notices_viewed(
        self,
        *,
        json_body: Union[List[str], Dict],
    ) -> StatusOK:
        """Update notices as 'viewed'

        Will mark the specified notices as 'viewed' by the logged in user.

        Permissions:
            Must be logged in.
        Minimum Server Version:
            5.26

        Api Reference:
            `MarkNoticesViewed <https://api.mattermost.com/#operation/MarkNoticesViewed>`_
        """

        url = "/system/notices/view"
        json_json_body = json_body

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

    def database_recycle(
        self,
    ) -> StatusOK:
        """Recycle database connections

        Recycle database connections by closing and reconnecting all connections
        to master and read replica databases.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `DatabaseRecycle <https://api.mattermost.com/#operation/DatabaseRecycle>`_
        """

        url = "/database/recycle"

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

    def test_email(
        self,
        *,
        json_body: Union[Config, Dict],
    ) -> StatusOK:
        """Send a test email

        Send a test email to make sure you have your email settings configured
        correctly. Optionally provide a configuration in the request body to
        test. If no valid configuration is present in the request body the
        current server configuration will be tested.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `TestEmail <https://api.mattermost.com/#operation/TestEmail>`_
        """

        url = "/email/test"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

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

    def test_site_url(
        self,
        *,
        json_body: Union[TestSiteURLJsonBody, Dict],
    ) -> StatusOK:
        """Checks the validity of a Site URL

        Sends a Ping request to the mattermost server using the specified Site
        URL.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.16

        Api Reference:
            `TestSiteURL <https://api.mattermost.com/#operation/TestSiteURL>`_
        """

        url = "/site_url/test"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

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

    def test_s3_connection(
        self,
        *,
        json_body: Union[Config, Dict],
    ) -> StatusOK:
        """Test AWS S3 connection

        Send a test to validate if can connect to AWS S3. Optionally provide a
        configuration in the request body to test. If no valid configuration is
        present in the request body the current server configuration will be
        tested.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            4.8

        Api Reference:
            `TestS3Connection <https://api.mattermost.com/#operation/TestS3Connection>`_
        """

        url = "/file/s3_test"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

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

    def get_config(
        self,
    ) -> Config:
        """Get configuration

        Retrieve the current server configuration

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `GetConfig <https://api.mattermost.com/#operation/GetConfig>`_
        """

        url = "/config"

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
            response200 = Config.parse_obj(response.json())

            return response200
        return response

    def update_config(
        self,
        *,
        json_body: Union[Config, Dict],
    ) -> Config:
        """Update configuration

        Submit a new configuration for the server to use. As of server version
        4.8, the `PluginSettings.EnableUploads` setting cannot be modified by
        this endpoint.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `UpdateConfig <https://api.mattermost.com/#operation/UpdateConfig>`_
        """

        url = "/config"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

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
            response200 = Config.parse_obj(response.json())

            return response200
        return response

    def reload_config(
        self,
    ) -> StatusOK:
        """Reload configuration

        Reload the configuration file to pick up on any changes made to it.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `ReloadConfig <https://api.mattermost.com/#operation/ReloadConfig>`_
        """

        url = "/config/reload"

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

    def get_client_config(
        self,
        *,
        format: str,
    ) -> None:
        """Get client configuration

        Get a subset of the server configuration needed by the client.

        Permissions:
            No permission required.

        Api Reference:
            `GetClientConfig <https://api.mattermost.com/#operation/GetClientConfig>`_
        """

        url = "/config/client"
        params: Dict[str, Any] = {
            "format": format,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        return response

    def get_environment_config(
        self,
    ) -> EnvironmentConfig:
        """Get configuration made through environment variables

        Retrieve a json object mirroring the server configuration where fields
        are set to true
        if the corresponding config setting is set through an environment
        variable. Settings
        that haven't been set through environment variables will be missing from
        the object.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            4.10

        Api Reference:
            `GetEnvironmentConfig <https://api.mattermost.com/#operation/GetEnvironmentConfig>`_
        """

        url = "/config/environment"

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
            response200 = EnvironmentConfig.parse_obj(response.json())

            return response200
        return response

    def patch_config(
        self,
        *,
        json_body: Union[Config, Dict],
    ) -> Config:
        """Patch configuration

        Submit configuration to patch. As of server version 4.8, the
        `PluginSettings.EnableUploads` setting cannot be modified by this
        endpoint.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.20

        Api Reference:
            `PatchConfig <https://api.mattermost.com/#operation/PatchConfig>`_
        """

        url = "/config/patch"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

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
            response200 = Config.parse_obj(response.json())

            return response200
        return response

    def upload_license_file(
        self,
        *,
        multipart_data: Union[UploadLicenseFileMultipartData, Dict],
    ) -> StatusOK:
        """Upload license file

        Upload a license to enable enterprise features.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            4.0

        Api Reference:
            `UploadLicenseFile <https://api.mattermost.com/#operation/UploadLicenseFile>`_
        """

        url = "/license"

        multipart_body_data = UploadLicenseFileMultipartData.parse_obj(multipart_data)

        request_kwargs = {
            "url": url,
            "data": multipart_body_data.get_data(),
            "files": multipart_body_data.get_files(),
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 201:
            response201 = StatusOK.parse_obj(response.json())

            return response201
        return response

    def remove_license_file(
        self,
    ) -> None:
        """Remove license file

        Remove the license file from the server. This will disable all
        enterprise features.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            4.0

        Api Reference:
            `RemoveLicenseFile <https://api.mattermost.com/#operation/RemoveLicenseFile>`_
        """

        url = "/license"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.delete(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        return response

    def get_client_license(
        self,
        *,
        format: str,
    ) -> None:
        """Get client license

        Get a subset of the server license needed by the client.

        Permissions:
            No permission required but having the `manage_system`
            permission returns more information.

        Api Reference:
            `GetClientLicense <https://api.mattermost.com/#operation/GetClientLicense>`_
        """

        url = "/license/client"
        params: Dict[str, Any] = {
            "format": format,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        return response

    def request_license_renewal_link(
        self,
    ) -> LicenseRenewalLink:
        """Request the license renewal link

        Request the renewal link that would be used to start the license renewal
        process

        Permissions:
            Must have `sysconsole_write_about` permission.
        Minimum Server Version:
            5.32

        Api Reference:
            `RequestLicenseRenewalLink <https://api.mattermost.com/#operation/RequestLicenseRenewalLink>`_
        """

        url = "/license/renewal"

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
            response200 = LicenseRenewalLink.parse_obj(response.json())

            return response200
        return response

    def request_trial_license(
        self,
        *,
        json_body: Union[RequestTrialLicenseJsonBody, Dict],
    ) -> None:
        """Request and install a trial license for your server

        Request and install a trial license for your server

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.25

        Api Reference:
            `RequestTrialLicense <https://api.mattermost.com/#operation/RequestTrialLicense>`_
        """

        url = "/trial-license"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

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

        return response

    def get_prev_trial_license(
        self,
    ) -> None:
        """Get last trial license used

        Get the last trial license used on the sevrer

        Permissions:
            Must have `manage_systems` permissions.
        Minimum Server Version:
            5.36

        Api Reference:
            `GetPrevTrialLicense <https://api.mattermost.com/#operation/GetPrevTrialLicense>`_
        """

        url = "/trial-license/prev"

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

        return response

    def get_audits(
        self,
        *,
        page: Optional[int] = 0,
        per_page: Optional[int] = 60,
    ) -> List[Audit]:
        """Get audits

        Get a page of audits for all users on the system, selected with `page`
        and `per_page` query parameters.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `GetAudits <https://api.mattermost.com/#operation/GetAudits>`_
        """

        url = "/audits"
        params: Dict[str, Any] = {
            "page": page,
            "per_page": per_page,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
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
                response200_item = Audit.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def invalidate_caches(
        self,
    ) -> StatusOK:
        """Invalidate all the caches

        Purge all the in-memory caches for the Mattermost server. This can have
        a temporary negative effect on performance while the caches are re-
        populated.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `InvalidateCaches <https://api.mattermost.com/#operation/InvalidateCaches>`_
        """

        url = "/caches/invalidate"

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

    def get_logs(
        self,
        *,
        page: Optional[int] = 0,
        logs_per_page: Optional[str] = "10000",
    ) -> List[str]:
        """Get logs

        Get a page of server logs, selected with `page` and `logs_per_page`
        query parameters.

        Permissions:
            Must have `manage_system` permission.

        Api Reference:
            `GetLogs <https://api.mattermost.com/#operation/GetLogs>`_
        """

        url = "/logs"
        params: Dict[str, Any] = {
            "page": page,
            "logs_per_page": logs_per_page,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = cast(List[str], response.json())

            return response200
        return response

    def post_log(
        self,
        *,
        json_body: Union[PostLogJsonBody, Dict],
    ) -> PostLogResponse200:
        """Add log message

        Add log messages to the server logs.
        Logged in users can log ERROR or DEBUG messages when
        `ServiceSettings.EnableDeveloper` is `true` or just DEBUG messages when
        `false`.
        Non-logged in users can log ERROR or DEBUG messages when
        `ServiceSettings.EnableDeveloper` is `true` and cannot log when `false`.

        Permissions:
            Users with `manage_system` permission can log ERROR or DEBUG
            messages.

        Api Reference:
            `PostLog <https://api.mattermost.com/#operation/PostLog>`_
        """

        url = "/logs"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

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
            response200 = PostLogResponse200.parse_obj(response.json())

            return response200
        return response

    def get_analytics_old(
        self,
        *,
        name: Optional[str] = "standard",
        team_id: Optional[str] = None,
    ) -> None:
        """Get analytics

        Get some analytics data about the system. This endpoint uses the old
        format, the `/analytics` route is reserved for the new format when it
        gets implemented.

        The returned JSON changes based on the `name` query parameter but is
        always key/value pairs.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            4.0

        Api Reference:
            `GetAnalyticsOld <https://api.mattermost.com/#operation/GetAnalyticsOld>`_
        """

        url = "/analytics/old"
        params: Dict[str, Any] = {
            "name": name,
            "team_id": team_id,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        return response

    def get_server_busy_expires(
        self,
    ) -> Server_Busy:
        """Get server busy expiry time.

        Gets the timestamp corresponding to when the server busy flag will be
        automatically cleared.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.20

        Api Reference:
            `GetServerBusyExpires <https://api.mattermost.com/#operation/GetServerBusyExpires>`_
        """

        url = "/server_busy"

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
            response200 = Server_Busy.parse_obj(response.json())

            return response200
        return response

    def set_server_busy(
        self,
        *,
        seconds: Optional[str] = "3600",
    ) -> StatusOK:
        """Set the server busy (high load) flag

        Marks the server as currently having high load which disables non-
        critical services such as search, statuses and typing notifications.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.20

        Api Reference:
            `SetServerBusy <https://api.mattermost.com/#operation/SetServerBusy>`_
        """

        url = "/server_busy"
        params: Dict[str, Any] = {
            "seconds": seconds,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
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

    def clear_server_busy(
        self,
    ) -> StatusOK:
        """Clears the server busy (high load) flag

        Marks the server as not having high load which re-enables non-critical
        services such as search, statuses and typing notifications.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.20

        Api Reference:
            `ClearServerBusy <https://api.mattermost.com/#operation/ClearServerBusy>`_
        """

        url = "/server_busy"

        request_kwargs = {
            "url": url,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.delete(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def get_redirect_location(
        self,
        *,
        url: str,
    ) -> None:
        """Get redirect location



        Permissions:
            Must be logged in.
        Minimum Server Version:
            3.10

        Api Reference:
            `GetRedirectLocation <https://api.mattermost.com/#operation/GetRedirectLocation>`_
        """

        url = "/redirect_location"
        params: Dict[str, Any] = {
            "url": url,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "params": params,
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.get(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        return response

    def get_image_by_url(
        self,
    ) -> None:
        """Get an image by url

        Fetches an image via Mattermost image proxy.

        Permissions:
            Must be logged in.
        Minimum Server Version:
            3.10

        Api Reference:
            `GetImageByUrl <https://api.mattermost.com/#operation/GetImageByUrl>`_
        """

        url = "/image"

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

        return response

    def upgrade_to_enterprise(
        self,
    ) -> PushNotification:
        """Executes an inplace upgrade from Team Edition to Enterprise Edition

        It downloads the Mattermost Enterprise Edition of your current version
        and replace your current version with it. After the upgrade you need to
        restart the Mattermost server.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.27

        Api Reference:
            `UpgradeToEnterprise <https://api.mattermost.com/#operation/UpgradeToEnterprise>`_
        """

        url = "/upgrade_to_enterprise"

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

        if response.status_code == 202:
            response202 = PushNotification.parse_obj(response.json())

            return response202
        return response

    def upgrade_to_enterprise_status(
        self,
    ) -> UpgradeToEnterpriseStatusResponse200:
        """Get the current status for the inplace upgrade from Team Edition to
        Enterprise Edition

        It returns the percentage of completion of the current upgrade or the
        error if there is any.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.27

        Api Reference:
            `UpgradeToEnterpriseStatus <https://api.mattermost.com/#operation/UpgradeToEnterpriseStatus>`_
        """

        url = "/upgrade_to_enterprise/status"

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
            response200 = UpgradeToEnterpriseStatusResponse200.parse_obj(
                response.json()
            )

            return response200
        return response

    def restart_server(
        self,
    ) -> StatusOK:
        """Restart the system after an upgrade from Team Edition to Enterprise
        Edition

        It restarts the current running mattermost instance to execute the new
        Enterprise binary.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.27

        Api Reference:
            `RestartServer <https://api.mattermost.com/#operation/RestartServer>`_
        """

        url = "/restart"

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

    def get_warn_metrics_status(
        self,
    ) -> StatusOK:
        """Get the warn metrics status (enabled or disabled)

        Get the status of a set of metrics (enabled or disabled) from the
        Systems table.

        The returned JSON contains the metrics that we need to warn the admin on
        with regard
        to their status (we return the ones whose status is \"true\", which
        means that they are
        in a \"warnable\" state - e.g. a threshold has been crossed or some
        other condition has
        been fulfilled).

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `GetWarnMetricsStatus <https://api.mattermost.com/#operation/GetWarnMetricsStatus>`_
        """

        url = "/warn_metrics/status"

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
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def send_warn_metric_ack(
        self,
        warn_metric_id: str,
        *,
        json_body: Union[SendWarnMetricAckJsonBody, Dict],
    ) -> StatusOK:
        """Acknowledge a warning of a metric status

        Acknowledge a warning for the warn_metric_id metric crossing a threshold
        (or some
        similar condition being fulfilled) - attempts to send an ack email to
        acknowledge@mattermost.com and sets the \"ack\" status for all the warn
        metrics in the system.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.26

        Api Reference:
            `SendWarnMetricAck <https://api.mattermost.com/#operation/SendWarnMetricAck>`_
        """

        url = f"/warn_metrics/ack/{warn_metric_id}"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

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

    def send_trial_license_warn_metric_ack(
        self,
        warn_metric_id: str,
    ) -> StatusOK:
        """Request trial license and acknowledge a warning of a metric status

        Request a trial license and acknowledge a warning for the warn_metric_id
        metric crossing a threshold (or some
        similar condition being fulfilled) - sets the \"ack\" status for all the
        warn metrics in the system.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.28

        Api Reference:
            `SendTrialLicenseWarnMetricAck <https://api.mattermost.com/#operation/SendTrialLicenseWarnMetricAck>`_
        """

        url = f"/warn_metrics/trial-license-ack/{warn_metric_id}"

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

    def check_integrity(
        self,
    ) -> List[IntegrityCheckResult]:
        """Perform a database integrity check

        Performs a database integrity check.

        Minimum Server Version:
            5.28.0
        Local Mode Only:
            This endpoint is only available through [local
            mode](https://docs.mattermost.com/administration/mmctl-cli-
            tool.html#local-mode).
        Warning:
            This check may temporarily harm system performance.

        Api Reference:
            `CheckIntegrity <https://api.mattermost.com/#operation/CheckIntegrity>`_
        """

        url = "/integrity"

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
            response200 = []
            _response200 = response.json()
            for response200_item_data in _response200:
                response200_item = IntegrityCheckResult.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def generate_support_packet(
        self,
    ) -> None:
        """Download a zip file which contains helpful and useful information for
        troubleshooting your mattermost instance.

        Download a zip file which contains helpful and useful information for
        troubleshooting your mattermost instance.
        ##### License
        Requires either a E10 or E20 license.

        Permissions:
            Must have any of the system console read permissions.
        Minimum Server Version:
            5.32

        Api Reference:
            `GenerateSupportPacket <https://api.mattermost.com/#operation/GenerateSupportPacket>`_
        """

        url = "/system/support_packet"

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

        return response

    def update_marketplace_visited_by_admin(
        self,
        *,
        json_body: Union[System, Dict],
    ) -> StatusOK:
        """Stores that the Plugin Marketplace has been visited by at least an
        admin.

        Stores the system-level status that specifies that at least an admin has
        visited the in-product Plugin Marketplace.

        Permissions:
            Must have `manage_system` permissions.
        Minimum Server Version:
            5.33

        Api Reference:
            `UpdateMarketplaceVisitedByAdmin <https://api.mattermost.com/#operation/UpdateMarketplaceVisitedByAdmin>`_
        """

        url = "/plugins/marketplace/first_admin_visit"

        if isinstance(json_body, BaseModel):
            json_json_body = json_body.dict(exclude_unset=True)
        else:
            json_json_body = json_body

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
