# -*- coding: utf-8 -*-
# Copyright 2018 New Vector Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from synapse.server_notices.consent_server_notices import ConsentServerNotices


class ServerNoticesSender(object):
    """A centralised place which sends server notices automatically when
    Certain Events take place
    """
    def __init__(self, hs):
        """

        Args:
            hs (synapse.server.HomeServer):
        """
        # todo: it would be nice to make this more dynamic
        self._consent_server_notices = ConsentServerNotices(hs)

    def on_user_syncing(self, user_id):
        """Called when the user performs a sync operation.

        This is only called when /sync (or /events) is called on the synapse
        master. In a deployment with synchrotrons, on_user_ip is called

        Args:
            user_id (str): mxid of user who synced

        Returns:
            Deferred
        """
        return self._consent_server_notices.maybe_send_server_notice_to_user(
            user_id,
        )

    def on_user_ip(self, user_id):
        """Called when a worker process saw a client request.

        Args:
            user_id (str): mxid

        Returns:
            Deferred
        """
        return self._consent_server_notices.maybe_send_server_notice_to_user(
            user_id,
        )
