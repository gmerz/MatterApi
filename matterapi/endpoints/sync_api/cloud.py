""" Module to access the Cloud endpoints """
# pylint: disable=too-many-lines,too-many-locals,too-many-public-methods,too-few-public-methods

from typing import Dict, List, Union

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

    def get_cloud_products(
        self,
    ) -> List[Product]:
        """Get cloud products

        Retrieve a list of all products that are offered for Mattermost Cloud.

        Permissions:
            Must have `manage_system` permission and be licensed for
            Cloud.
        Minimum Server Version:
            5.28
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `GetCloudProducts <https://api.mattermost.com/#operation/GetCloudProducts>`_
        """

        url = "/cloud/products"

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
                response200_item = Product.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def create_customer_payment(
        self,
    ) -> PaymentSetupIntent:
        """Create a customer setup payment intent

        Creates a customer setup payment intent for the given Mattermost cloud
        installation.

        Permissions:
            Must have `manage_system` permission and be licensed for
            Cloud.
        Minimum Server Version:
            5.28
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `CreateCustomerPayment <https://api.mattermost.com/#operation/CreateCustomerPayment>`_
        """

        url = "/cloud/payment"

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

        if response.status_code == 201:
            response201 = PaymentSetupIntent.parse_obj(response.json())

            return response201
        return response

    def confirm_customer_payment(
        self,
        *,
        multipart_data: Union[ConfirmCustomerPaymentMultipartData, Dict],
    ) -> None:
        """Completes the payment setup intent

        Confirms the payment setup intent initiated when posting to
        `/cloud/payment`.

        Permissions:
            Must have `manage_system` permission and be licensed for
            Cloud.
        Minimum Server Version:
            5.28
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `ConfirmCustomerPayment <https://api.mattermost.com/#operation/ConfirmCustomerPayment>`_
        """

        url = "/cloud/payment/confirm"

        multipart_body_data = ConfirmCustomerPaymentMultipartData.parse_obj(
            multipart_data
        )

        request_kwargs = {
            "url": url,
            "data": multipart_body_data.get_data(),
        }
        # pylint: disable-next=protected-access
        with self.client._get_httpx_client() as httpx_client:
            response = httpx_client.post(
                **request_kwargs,
            )

        if self.skip_response_parsing:
            return response

        return response

    def get_cloud_customer(
        self,
    ) -> CloudCustomer:
        """Get cloud customer

        Retrieves the customer information for the Mattermost Cloud customer
        bound to this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for
            Cloud.
        Minimum Server Version:
            5.28
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `GetCloudCustomer <https://api.mattermost.com/#operation/GetCloudCustomer>`_
        """

        url = "/cloud/customer"

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
            response200 = CloudCustomer.parse_obj(response.json())

            return response200
        return response

    def update_cloud_customer(
        self,
        *,
        json_body: Union[UpdateCloudCustomerJsonBody, Dict],
    ) -> CloudCustomer:
        """Update cloud customer

        Updates the customer information for the Mattermost Cloud customer bound
        to this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for
            Cloud.
        Minimum Server Version:
            5.29
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `UpdateCloudCustomer <https://api.mattermost.com/#operation/UpdateCloudCustomer>`_
        """

        url = "/cloud/customer"

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
            response200 = CloudCustomer.parse_obj(response.json())

            return response200
        return response

    def update_cloud_customer_address(
        self,
        *,
        json_body: Union[Address, Dict],
    ) -> CloudCustomer:
        """Update cloud customer address

        Updates the company address for the Mattermost Cloud customer bound to
        this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for
            Cloud.
        Minimum Server Version:
            5.29
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `UpdateCloudCustomerAddress <https://api.mattermost.com/#operation/UpdateCloudCustomerAddress>`_
        """

        url = "/cloud/customer/address"

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
            response200 = CloudCustomer.parse_obj(response.json())

            return response200
        return response

    def get_subscription(
        self,
    ) -> Subscription:
        """Get cloud subscription

        Retrieves the subscription information for the Mattermost Cloud customer
        bound to this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for
            Cloud.
        Minimum Server Version:
            5.28
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `GetSubscription <https://api.mattermost.com/#operation/GetSubscription>`_
        """

        url = "/cloud/subscription"

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
            response200 = Subscription.parse_obj(response.json())

            return response200
        return response

    def get_invoices_for_subscription(
        self,
    ) -> List[Invoice]:
        """Get cloud subscription invoices

        Retrieves the invoices for the subscription bound to this installation.

        Permissions:
            Must have `manage_system` permission and be licensed for
            Cloud.
        Minimum Server Version:
            5.30
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `GetInvoicesForSubscription <https://api.mattermost.com/#operation/GetInvoicesForSubscription>`_
        """

        url = "/cloud/subscription/invoices"

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
                response200_item = Invoice.parse_obj(response200_item_data)

                response200.append(response200_item)

            return response200
        return response

    def get_invoice_for_subscription_as_pdf(
        self,
        invoice_id: str,
    ) -> None:
        """Get cloud invoice PDF

        Retrieves the PDF for the invoice passed as parameter

        Permissions:
            Must have `manage_system` permission and be licensed for
            Cloud.
        Minimum Server Version:
            5.30
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `GetInvoiceForSubscriptionAsPdf <https://api.mattermost.com/#operation/GetInvoiceForSubscriptionAsPdf>`_
        """

        url = f"/cloud/subscription/invoices/{invoice_id}/pdf"

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

    def post_endpoint_for_cws_webhooks(
        self,
    ) -> None:
        """POST endpoint for CWS Webhooks

        An endpoint for processing webhooks from the Customer Portal

        Permissions:
            This endpoint should only be accessed by CWS, in a
            Mattermost Cloud instance
        Minimum Server Version:
            5.30
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `PostEndpointForCwsWebhooks <https://api.mattermost.com/#operation/PostEndpointForCwsWebhooks>`_
        """

        url = "/cloud/webhook"

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

        return response

    def get_subscription_stats(
        self,
    ) -> SubscriptionStats:
        """GET endpoint for cloud subscription stats

        An endpoint that returns stats about a user's subscription. For example
        remaining seats on a free tier

        Permissions:
            This endpoint should only be accessed in a Mattermost Cloud
            instance
        Minimum Server Version:
            5.34
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `GetSubscriptionStats <https://api.mattermost.com/#operation/GetSubscriptionStats>`_
        """

        url = "/cloud/subscription/stats"

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
            response200 = SubscriptionStats.parse_obj(response.json())

            return response200
        return response

    def send_admin_upgrade_request_email(
        self,
    ) -> None:
        """POST endpoint for triggering sending emails to admin with request to
        upgrade workspace

        An endpoint that triggers sending emails to all sys admins to request
        them to upgrade the workspace when a user tries to invite more users

        Permissions:
            This endpoint should only be accessed in a Mattermost Cloud
            instance
        Minimum Server Version:
            5.34
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `SendAdminUpgradeRequestEmail <https://api.mattermost.com/#operation/SendAdminUpgradeRequestEmail>`_
        """

        url = "/cloud/subscription/limitreached/invite"

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

        return response

    def send_admin_upgrade_request_email_on_join(
        self,
    ) -> None:
        """POST endpoint for triggering sending emails to admin with request to
        upgrade workspace

        An endpoint that triggers sending emails to all sys admins to request
        them to upgrade the workspace when a user tries to join the workspace

        Permissions:
            This endpoint should only be accessed in a Mattermost Cloud
            instance
        Minimum Server Version:
            5.34
        Warning:
            This is intended for internal use and is subject to change.

        Api Reference:
            `SendAdminUpgradeRequestEmailOnJoin <https://api.mattermost.com/#operation/SendAdminUpgradeRequestEmailOnJoin>`_
        """

        url = "/cloud/subscription/limitreached/join"

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

        return response
