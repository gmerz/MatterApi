""" Module to access the Saml endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from pydantic import BaseModel

from ...models import (
    MigrateAuthToSamlJsonBody,
    ResetSamlAuthDataToEmailJsonBody,
    ResetSamlAuthDataToEmailResponse200,
    SamlCertificateStatus,
    StatusOK,
    UploadSamlIdpCertificateMultipartData,
    UploadSamlPrivateCertificateMultipartData,
    UploadSamlPublicCertificateMultipartData,
)
from ..base import ApiBaseClass


class SamlApi(ApiBaseClass):
    """Endpoints for configuring and interacting with SAML."""

    def migrate_auth_to_saml(
        self,
        *,
        json_body: MigrateAuthToSamlJsonBody,
    ) -> None:
        """Migrate user accounts authentication type to SAML.

        Migrates accounts from one authentication provider to another. For
        example, you can upgrade your authentication provider from email to
        SAML.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.28

        Api Reference:
            `MigrateAuthToSaml <https://api.mattermost.com/#operation/MigrateAuthToSaml>`_
        """

        url = "/users/migrate_auth/saml"

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

    def get_saml_metadata(
        self,
    ) -> str:
        """Get metadata

        Get SAML metadata from the server. SAML must be configured properly.

        Permissions:
            No permission required.

        Api Reference:
            `GetSamlMetadata <https://api.mattermost.com/#operation/GetSamlMetadata>`_
        """

        url = "/saml/metadata"

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
            response200 = response.json()
            return response200
        return response

    def get_saml_metadata_from_idp(
        self,
    ) -> str:
        """Get metadata from Identity Provider

        Get SAML metadata from the Identity Provider. SAML must be configured
        properly.

        Permissions:
            No permission required.

        Api Reference:
            `GetSamlMetadataFromIdp <https://api.mattermost.com/#operation/GetSamlMetadataFromIdp>`_
        """

        url = "/saml/metadatafromidp"

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
            response200 = response.json()
            return response200
        return response

    def upload_saml_idp_certificate(
        self,
        *,
        multipart_data: UploadSamlIdpCertificateMultipartData,
    ) -> StatusOK:
        """Upload IDP certificate

        Upload the IDP certificate to be used with your SAML configuration. The
        server will pick a hard-coded filename for the IdpCertificateFile
        setting in your `config.json`.

        Permissions:
            Must have `sysconsole_write_authentication` permission.

        Api Reference:
            `UploadSamlIdpCertificate <https://api.mattermost.com/#operation/UploadSamlIdpCertificate>`_
        """

        url = "/saml/certificate/idp"

        multipart_body_data = UploadSamlIdpCertificateMultipartData.parse_obj(
            multipart_data
        )

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

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def delete_saml_idp_certificate(
        self,
    ) -> StatusOK:
        """Remove IDP certificate

        Delete the current IDP certificate being used with your SAML
        configuration. This will also disable SAML on your system as this
        certificate is required for SAML.

        Permissions:
            Must have `sysconsole_write_authentication` permission.

        Api Reference:
            `DeleteSamlIdpCertificate <https://api.mattermost.com/#operation/DeleteSamlIdpCertificate>`_
        """

        url = "/saml/certificate/idp"

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

    def upload_saml_public_certificate(
        self,
        *,
        multipart_data: UploadSamlPublicCertificateMultipartData,
    ) -> StatusOK:
        """Upload public certificate

        Upload the public certificate to be used for encryption with your SAML
        configuration. The server will pick a hard-coded filename for the
        PublicCertificateFile setting in your `config.json`.

        Permissions:
            Must have `sysconsole_write_authentication` permission.

        Api Reference:
            `UploadSamlPublicCertificate <https://api.mattermost.com/#operation/UploadSamlPublicCertificate>`_
        """

        url = "/saml/certificate/public"

        multipart_body_data = UploadSamlPublicCertificateMultipartData.parse_obj(
            multipart_data
        )

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

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def delete_saml_public_certificate(
        self,
    ) -> StatusOK:
        """Remove public certificate

        Delete the current public certificate being used with your SAML
        configuration. This will also disable encryption for SAML on your system
        as this certificate is required for that.

        Permissions:
            Must have `sysconsole_write_authentication` permission.

        Api Reference:
            `DeleteSamlPublicCertificate <https://api.mattermost.com/#operation/DeleteSamlPublicCertificate>`_
        """

        url = "/saml/certificate/public"

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

    def upload_saml_private_certificate(
        self,
        *,
        multipart_data: UploadSamlPrivateCertificateMultipartData,
    ) -> StatusOK:
        """Upload private key

        Upload the private key to be used for encryption with your SAML
        configuration. The server will pick a hard-coded filename for the
        PrivateKeyFile setting in your `config.json`.

        Permissions:
            Must have `sysconsole_write_authentication` permission.

        Api Reference:
            `UploadSamlPrivateCertificate <https://api.mattermost.com/#operation/UploadSamlPrivateCertificate>`_
        """

        url = "/saml/certificate/private"

        multipart_body_data = UploadSamlPrivateCertificateMultipartData.parse_obj(
            multipart_data
        )

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

        if response.status_code == 200:
            response200 = StatusOK.parse_obj(response.json())

            return response200
        return response

    def delete_saml_private_certificate(
        self,
    ) -> StatusOK:
        """Remove private key

        Delete the current private key being used with your SAML configuration.
        This will also disable encryption for SAML on your system as this key is
        required for that.

        Permissions:
            Must have `sysconsole_write_authentication` permission.

        Api Reference:
            `DeleteSamlPrivateCertificate <https://api.mattermost.com/#operation/DeleteSamlPrivateCertificate>`_
        """

        url = "/saml/certificate/private"

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

    def get_saml_certificate_status(
        self,
    ) -> SamlCertificateStatus:
        """Get certificate status

        Get the status of the uploaded certificates and keys in use by your SAML
        configuration.

        Permissions:
            Must have `sysconsole_write_authentication` permission.

        Api Reference:
            `GetSamlCertificateStatus <https://api.mattermost.com/#operation/GetSamlCertificateStatus>`_
        """

        url = "/saml/certificate/status"

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
            response200 = SamlCertificateStatus.parse_obj(response.json())

            return response200
        return response

    def reset_saml_auth_data_to_email(
        self,
        *,
        json_body: ResetSamlAuthDataToEmailJsonBody,
    ) -> ResetSamlAuthDataToEmailResponse200:
        """Reset AuthData to Email

        Reset the AuthData field of SAML users to their email. This is meant to
        be used when the \"id\" attribute is set to an empty value (\"\") from a
        previously non-empty value.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.35

        Api Reference:
            `ResetSamlAuthDataToEmail <https://api.mattermost.com/#operation/ResetSamlAuthDataToEmail>`_
        """

        url = "/saml/reset_auth_data"

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
            response200 = ResetSamlAuthDataToEmailResponse200.parse_obj(response.json())

            return response200
        return response
