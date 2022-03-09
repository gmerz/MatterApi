""" Module to access the Migrate endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Dict, Union

from pydantic import BaseModel

from ...models import MigrateAuthToLdapJsonBody, MigrateAuthToSamlJsonBody
from ..base import ApiBaseClass


class MigrateApi(ApiBaseClass):
    """ """

    async def migrate_auth_to_ldap(
        self,
        *,
        json_body: Union[MigrateAuthToLdapJsonBody, Dict],
    ) -> None:
        """Migrate user accounts authentication type to LDAP.

        Migrates accounts from one authentication provider to another. For
        example, you can upgrade your authentication provider from email to
        LDAP.

        Permissions:
            Must have `manage_system` permission.
        Minimum Server Version:
            5.28

        Api Reference:
            `MigrateAuthToLdap <https://api.mattermost.com/#operation/MigrateAuthToLdap>`_
        """

        url = "/users/migrate_auth/ldap"

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

    async def migrate_auth_to_saml(
        self,
        *,
        json_body: Union[MigrateAuthToSamlJsonBody, Dict],
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
        async with self.client._get_httpx_client() as httpx_client:
            response = await httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        return response
