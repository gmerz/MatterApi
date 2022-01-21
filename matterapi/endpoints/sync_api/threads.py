from typing import Any, Dict, Optional

from ...models import UserThreads
from ..base import ApiBaseClass


class ThreadsApi(ApiBaseClass):
    """None"""

    def get_user_threads(
        self,
        user_id: str,
        team_id: str,
        *,
        since: Optional[int] = None,
        deleted: Optional[bool] = False,
        extended: Optional[bool] = False,
        page: Optional[int] = 0,
        page_size: Optional[int] = 30,
        totals_only: Optional[bool] = False,
    ) -> UserThreads:
        """Get all threads that user is following

        Get all threads that user is following

        Permissions:
            Must be logged in as the user or have `edit_other_users` permission.
        Minimum Server Version:
            5.29
        """

        url = "{}/users/{user_id}/teams/{team_id}/threads".format(
            self.client.base_url, user_id=user_id, team_id=team_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()
        params: Dict[str, Any] = {
            "since": since,
            "deleted": deleted,
            "extended": extended,
            "page": page,
            "pageSize": page_size,
            "totalsOnly": totals_only,
        }
        params = {k: v for k, v in params.items() if v is not None}

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "params": params,
        }

        response = self.client.get(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        if response.status_code == 200:
            response_200 = UserThreads.parse_obj(response.json())

            return response_200
        return response

    def get_thread_mention_counts_by_channel(
        self,
        user_id: str,
        team_id: str,
    ) -> None:
        """Get all unread mention counts from followed threads, per-channel

        Get all unread mention counts from followed threads

        Permissions:
            Must be logged in as the user or have `edit_other_users` permission.
        Minimum Server Version:
            5.29
        """

        url = "{}/users/{user_id}/teams/{team_id}/threads/mention_counts".format(
            self.client.base_url, user_id=user_id, team_id=team_id
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

        return response

    def update_threads_read_for_user(
        self,
        user_id: str,
        team_id: str,
    ) -> None:
        """Mark all threads that user is following as read

        Mark all threads that user is following as read

        Permissions:
            Must be logged in as the user or have `edit_other_users` permission.
        Minimum Server Version:
            5.29
        """

        url = "{}/users/{user_id}/teams/{team_id}/threads/read".format(
            self.client.base_url, user_id=user_id, team_id=team_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = self.client.put(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        return response

    def update_thread_read_for_user(
        self,
        user_id: str,
        team_id: str,
        thread_id: str,
        timestamp: str,
    ) -> None:
        """Mark a thread that user is following read state to the timestamp

        Mark a thread that user is following as read

        Permissions:
            Must be logged in as the user or have `edit_other_users` permission.
        Minimum Server Version:
            5.29
        """

        url = "{}/users/{user_id}/teams/{team_id}/threads/{thread_id}/read/{timestamp}".format(
            self.client.base_url,
            user_id=user_id,
            team_id=team_id,
            thread_id=thread_id,
            timestamp=timestamp,
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = self.client.put(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        return response

    def start_following_thread(
        self,
        user_id: str,
        team_id: str,
        thread_id: str,
    ) -> None:
        """Start following a thread

        Start following a thread

        Permissions:
            Must be logged in as the user or have `edit_other_users` permission.
        Minimum Server Version:
            5.29
        """

        url = "{}/users/{user_id}/teams/{team_id}/threads/{thread_id}/following".format(
            self.client.base_url, user_id=user_id, team_id=team_id, thread_id=thread_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = self.client.put(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        return response

    def stop_following_thread(
        self,
        user_id: str,
        team_id: str,
        thread_id: str,
    ) -> None:
        """Stop following a thread

        Stop following a thread

        Permissions:
            Must be logged in as the user or have `edit_other_users` permission.
        Minimum Server Version:
            5.29
        """

        url = "{}/users/{user_id}/teams/{team_id}/threads/{thread_id}/following".format(
            self.client.base_url, user_id=user_id, team_id=team_id, thread_id=thread_id
        )
        headers: Dict[str, Any] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        request_kwargs = {
            "url": url,
            "headers": headers,
            "cookies": cookies,
        }

        response = self.client.delete(
            **request_kwargs,
        )

        if self.skip_response_parsing == True:
            return response

        return response

    def get_user_thread(
        self,
        user_id: str,
        team_id: str,
        thread_id: str,
    ) -> None:
        """Get a thread followed by the user

        Get a thread

        Permissions:
            Must be logged in as the user or have `edit_other_users` permission.
        Minimum Server Version:
            5.29
        """

        url = "{}/users/{user_id}/teams/{team_id}/threads/{thread_id}".format(
            self.client.base_url, user_id=user_id, team_id=team_id, thread_id=thread_id
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

        return response
