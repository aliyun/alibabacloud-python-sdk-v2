# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_special_resource_collection
from alibabacloud.utils.utils import _transfer_params


class _DOMAINResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'domain', _client=_client)
        self.auctions = _create_special_resource_collection(
            _DOMAINAuctionResource, _client, _client.query_auctions,
            'Data.AuctionDetail', 'AuctionId',
        )


class _DOMAINAuctionResource(ServiceResource):

    def __init__(self, auction_id, _client=None):
        ServiceResource.__init__(self, "domain.auction", _client=_client)
        self.auction_id = auction_id

        self.auction_end_time = None
        self.book_end_time = None
        self.booked_partner = None
        self.currency = None
        self.delivery_time = None
        self.domain_name = None
        self.domain_type = None
        self.fail_code = None
        self.high_bid = None
        self.high_bidder = None
        self.next_valid_bid = None
        self.partner_type = None
        self.pay_end_time = None
        self.pay_price = None
        self.pay_status = None
        self.produce_status = None
        self.reserve_met = None
        self.status = None
        self.transfer_in_price = None
        self.your_current_bid = None
        self.your_max_bid = None

    def bid(self, **params):
        _params = _transfer_params(params)
        return self._client.bid_domain(auction_id=self.auction_id, **_params)

    def query_auction_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.query_auction_detail(auction_id=self.auction_id, **_params)

    def query_bid_records(self, **params):
        _params = _transfer_params(params)
        return self._client.query_bid_records(auction_id=self.auction_id, **_params)
