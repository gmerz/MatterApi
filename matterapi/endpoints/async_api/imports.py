""" Module to access the Imports endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods

from ..base import ApiBaseClass


class ImportsApi(ApiBaseClass):
    """Endpoints related to import files."""

    async def list_imports(
        self,
    ) -> None:
        """List import files

        Lists all available import files.

        Permissions:
            Must have `manage_system` permissions.
        Minimum Server Version:
            5.31

        Api Reference:
            `ListImports <https://api.mattermost.com/#operation/ListImports>`_
        """

        url = "/imports"

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

        return response
