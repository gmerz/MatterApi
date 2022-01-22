from typing import Any, Dict, List

from pydantic import BaseModel

from ...models import (
    Address,
    CloudCustomer,
    ConfirmCustomerPaymentMultipartData,
    Invoice,
    PaymentSetupIntent,
    Product,
    Subscription,
    SubscriptionStats,
    UpdateCloudCustomerJsonBody,
)
from ..base import ApiBaseClass


class CloudApi(ApiBaseClass):
    """ """

    async def get_cloud_products(
        self,
    ) -> List[Product]:
        """Get cloud products

        Retrieve a list of all products that are offered for Mattermost Cloud.

        Permissions:
            Must have `manage_system` permission and be licensed for Cloud.
        Minimum Server Version:
            5.28

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/products".format(self.client.base_url)
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
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = Product.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response

    async def create_customer_payment(
        self,
    ) -> PaymentSetupIntent:
        """Create a customer setup payment intent

        Creates a customer setup payment intent for the given Mattermost cloud
        installation.

        Permissions:
            Must have `manage_system` permission and be licensed for Cloud.
        Minimum Server Version:
            5.28

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/payment".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        if response.status_code == 201:
            response_201 = PaymentSetupIntent.parse_obj(response.json())

            return response_201
        return response

    async def confirm_customer_payment(
        self,
        *,
        multipart_data: ConfirmCustomerPaymentMultipartData,
    ) -> None:
        """Completes the payment setup intent

        Confirms the payment setup intent initiated when posting to
        `/cloud/payment`.

        Permissions:
            Must have `manage_system` permission and be licensed for Cloud.
        Minimum Server Version:
            5.28

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/payment/confirm".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        multipart_body_data = ConfirmCustomerPaymentMultipartData.parse_obj(
            multipart_data
        )

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "data": multipart_body_data.get_data(),
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        return response

    async def get_cloud_customer(
        self,
    ) -> CloudCustomer:
        """Get cloud customer

        Retrieves the customer information for the Mattermost Cloud customer
        bound to this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for Cloud.
        Minimum Server Version:
            5.28

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/customer".format(self.client.base_url)
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
            response_200 = CloudCustomer.parse_obj(response.json())

            return response_200
        return response

    async def update_cloud_customer(
        self,
        *,
        json_body: UpdateCloudCustomerJsonBody,
    ) -> CloudCustomer:
        """Update cloud customer

        Updates the customer information for the Mattermost Cloud customer bound
        to this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for Cloud.
        Minimum Server Version:
            5.29

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/customer".format(self.client.base_url)
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
            response_200 = CloudCustomer.parse_obj(response.json())

            return response_200
        return response

    async def update_cloud_customer_address(
        self,
        *,
        json_body: Address,
    ) -> CloudCustomer:
        """Update cloud customer address

        Updates the company address for the Mattermost Cloud customer bound to
        this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for Cloud.
        Minimum Server Version:
            5.29

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/customer/address".format(self.client.base_url)
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
            response_200 = CloudCustomer.parse_obj(response.json())

            return response_200
        return response

    async def get_subscription(
        self,
    ) -> Subscription:
        """Get cloud subscription

        Retrieves the subscription information for the Mattermost Cloud customer
        bound to this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for Cloud.
        Minimum Server Version:
            5.28

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/subscription".format(self.client.base_url)
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
            response_200 = Subscription.parse_obj(response.json())

            return response_200
        return response

    async def get_invoices_for_subscription(
        self,
    ) -> List[Invoice]:
        """Get cloud subscription invoices

        Retrieves the invoices for the subscription bound to this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for Cloud.
        Minimum Server Version:
            5.30

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/subscription/invoices".format(self.client.base_url)
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
            response_200 = []
            _response_200 = response.json()
            for response_200_item_data in _response_200:
                response_200_item = Invoice.parse_obj(response_200_item_data)

                response_200.append(response_200_item)

            return response_200
        return response

    async def get_invoice_for_subscription_as_pdf(
        self,
        invoice_id: str,
    ) -> None:
        """Get cloud invoice PDF

        Retrieves the PDF for the invoice passed as parameter

        Permissions:
            Must have `manage_system` permission and be licensed for Cloud.
        Minimum Server Version:
            5.30

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/subscription/invoices/{invoice_id}/pdf".format(
            self.client.base_url, invoice_id=invoice_id
        )
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

        return response

    async def post_endpoint_for_cws_webhooks(
        self,
    ) -> None:
        """POST endpoint for CWS Webhooks

        An endpoint for processing webhooks from the Customer Portal

        Permissions:
            This endpoint should only be accessed by CWS, in a Mattermost Cloud
        instance
        Minimum Server Version:
            5.30

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/webhook".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        return response

    async def get_subscription_stats(
        self,
    ) -> SubscriptionStats:
        """GET endpoint for cloud subscription stats

        An endpoint that returns stats about a user's subscription. For example
        remaining seats on a free tier

        Permissions:
            This endpoint should only be accessed in a Mattermost Cloud instance
        Minimum Server Version:
            5.34

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/subscription/stats".format(self.client.base_url)
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
            response_200 = SubscriptionStats.parse_obj(response.json())

            return response_200
        return response

    async def send_admin_upgrade_request_email(
        self,
    ) -> None:
        """POST endpoint for triggering sending emails to admin with request to
        upgrade workspace

        An endpoint that triggers sending emails to all sys admins to request
        them to upgrade the workspace when a user tries to invite more users

        Permissions:
            This endpoint should only be accessed in a Mattermost Cloud instance
        Minimum Server Version:
            5.34

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/subscription/limitreached/invite".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        return response

    async def send_admin_upgrade_request_email_on_join(
        self,
    ) -> None:
        """POST endpoint for triggering sending emails to admin with request to
        upgrade workspace

        An endpoint that triggers sending emails to all sys admins to request
        them to upgrade the workspace when a user tries to join the workspace

        Permissions:
            This endpoint should only be accessed in a Mattermost Cloud instance
        Minimum Server Version:
            5.34

        Warning:
            This is intended for internal use and is subject to change.
        """

        url = "{}/cloud/subscription/limitreached/join".format(self.client.base_url)
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = await self.client.post(
            **request_kwargs,
        )

        if self.skip_response_parsing:
            return response

        return response
