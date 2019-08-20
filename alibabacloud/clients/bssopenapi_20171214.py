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

from alibabacloud.client import AlibabaCloudClient
from alibabacloud.request import APIRequest
from alibabacloud.utils.parameter_validation import verify_params


class BssOpenApiClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'BssOpenApi'
        self.api_version = '2017-12-14'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def create_ag_account(
            self,
            first_name=None,
            login_email=None,
            province_name=None,
            city_name=None,
            account_attr=None,
            postcode=None,
            enterprise_name=None,
            nation_code=None,
            last_name=None):
        api_request = APIRequest('CreateAgAccount', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "FirstName": first_name,
            "LoginEmail": login_email,
            "ProvinceName": province_name,
            "CityName": city_name,
            "AccountAttr": account_attr,
            "Postcode": postcode,
            "EnterpriseName": enterprise_name,
            "NationCode": nation_code,
            "LastName": last_name}
        return self._handle_request(api_request).result

    def get_customer_account_info(self, owner_id=None):
        api_request = APIRequest('GetCustomerAccountInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_customer_list(self,):
        api_request = APIRequest('GetCustomerList', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def change_reseller_consume_amount(
            self,
            adjust_type=None,
            amount=None,
            out_biz_id=None,
            extend_map=None,
            currency=None,
            source=None,
            owner_id=None,
            business_type=None):
        api_request = APIRequest('ChangeResellerConsumeAmount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AdjustType": adjust_type,
            "Amount": amount,
            "OutBizId": out_biz_id,
            "ExtendMap": extend_map,
            "Currency": currency,
            "Source": source,
            "OwnerId": owner_id,
            "BusinessType": business_type}
        return self._handle_request(api_request).result

    def set_reseller_user_status(self, owner_id=None, status=None, business_type=None):
        api_request = APIRequest('SetResellerUserStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "Status": status, "BusinessType": business_type}
        return self._handle_request(api_request).result

    def create_reseller_user_quota(
            self,
            amount=None,
            out_biz_id=None,
            currency=None,
            owner_id=None):
        api_request = APIRequest('CreateResellerUserQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Amount": amount,
            "OutBizId": out_biz_id,
            "Currency": currency,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_reseller_user_quota(self, amount=None, out_biz_id=None, currency=None, owner_id=None):
        api_request = APIRequest('SetResellerUserQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Amount": amount,
            "OutBizId": out_biz_id,
            "Currency": currency,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_reseller_available_quota(self, item_codes=None, owner_id=None):
        api_request = APIRequest('QueryResellerAvailableQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ItemCodes": item_codes, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_reseller_user_alarm_threshold(
            self,
            alarm_type=None,
            alarm_thresholds=None,
            owner_id=None):
        api_request = APIRequest('SetResellerUserAlarmThreshold', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AlarmType": alarm_type,
            "AlarmThresholds": alarm_thresholds,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_account_transactions(
            self,
            record_id=None,
            page_size=None,
            transaction_channel_sn=None,
            create_time_start=None,
            transaction_number=None,
            page_num=None,
            create_time_end=None):
        api_request = APIRequest('QueryAccountTransactions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordID": record_id,
            "PageSize": page_size,
            "TransactionChannelSN": transaction_channel_sn,
            "CreateTimeStart": create_time_start,
            "TransactionNumber": transaction_number,
            "PageNum": page_num,
            "CreateTimeEnd": create_time_end}
        return self._handle_request(api_request).result

    def unsubscribe_bill_to_oss(self, subscribe_type=None, mult_account_rel_subscribe=None):
        api_request = APIRequest('UnsubscribeBillToOSS', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SubscribeType": subscribe_type,
                               "MultAccountRelSubscribe": mult_account_rel_subscribe}
        return self._handle_request(api_request).result

    def subscribe_bill_to_oss(
            self,
            bucket_owner_id=None,
            subscribe_type=None,
            subscribe_bucket=None,
            mult_account_rel_subscribe=None):
        api_request = APIRequest('SubscribeBillToOSS', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BucketOwnerId": bucket_owner_id,
            "SubscribeType": subscribe_type,
            "SubscribeBucket": subscribe_bucket,
            "MultAccountRelSubscribe": mult_account_rel_subscribe}
        return self._handle_request(api_request).result

    def query_user_oms_data(
            self,
            data_type=None,
            marker=None,
            page_size=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            table=None):
        api_request = APIRequest('QueryUserOmsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataType": data_type,
            "Marker": marker,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "Table": table}
        return self._handle_request(api_request).result

    def cancel_order(self, order_id=None, owner_id=None):
        api_request = APIRequest('CancelOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OrderId": order_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def apply_invoice(
            self,
            invoicing_type=None,
            apply_user_nick=None,
            invoice_by_amount=None,
            customer_id=None,
            list_of_selected_ids=None,
            process_way=None,
            caller_bid=None,
            owner_id=None,
            invoice_amount=None,
            address_id=None,
            caller_uid=None):
        api_request = APIRequest('ApplyInvoice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InvoicingType": invoicing_type,
            "ApplyUserNick": apply_user_nick,
            "InvoiceByAmount": invoice_by_amount,
            "CustomerId": customer_id,
            "SelectedIds": list_of_selected_ids,
            "ProcessWay": process_way,
            "callerBid": caller_bid,
            "OwnerId": owner_id,
            "InvoiceAmount": invoice_amount,
            "AddressId": address_id,
            "callerUid": caller_uid}
        repeat_info = {"SelectedIds": ('SelectedIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def query_customer_address_list(self, caller_bid=None, owner_id=None, caller_uid=None):
        api_request = APIRequest('QueryCustomerAddressList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "callerBid": caller_bid,
            "OwnerId": owner_id,
            "callerUid": caller_uid}
        return self._handle_request(api_request).result

    def query_evaluate_list(
            self,
            end_search_time=None,
            out_biz_id=None,
            sort_type=None,
            list_of_biz_type_list=None,
            type_=None,
            owner_id=None,
            page_num=None,
            start_search_time=None,
            end_biz_time=None,
            page_size=None,
            end_amount=None,
            bill_cycle=None,
            start_amount=None,
            start_biz_time=None):
        api_request = APIRequest('QueryEvaluateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndSearchTime": end_search_time,
            "OutBizId": out_biz_id,
            "SortType": sort_type,
            "BizTypeList": list_of_biz_type_list,
            "Type": type_,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "StartSearchTime": start_search_time,
            "EndBizTime": end_biz_time,
            "PageSize": page_size,
            "EndAmount": end_amount,
            "BillCycle": bill_cycle,
            "StartAmount": start_amount,
            "StartBizTime": start_biz_time}
        repeat_info = {"BizTypeList": ('BizTypeList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def query_invoicing_customer_list(self, owner_id=None):
        api_request = APIRequest('QueryInvoicingCustomerList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_bill_overview(
            self,
            product_code=None,
            subscription_type=None,
            billing_cycle=None,
            product_type=None):
        api_request = APIRequest('QueryBillOverview', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SubscriptionType": subscription_type,
            "BillingCycle": billing_cycle,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def query_bill(
            self,
            product_code=None,
            is_hide_zero_charge=None,
            is_display_local_currency=None,
            subscription_type=None,
            page_size=None,
            billing_cycle=None,
            type_=None,
            owner_id=None,
            page_num=None,
            product_type=None):
        api_request = APIRequest('QueryBill', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "IsHideZeroCharge": is_hide_zero_charge,
            "IsDisplayLocalCurrency": is_display_local_currency,
            "SubscriptionType": subscription_type,
            "PageSize": page_size,
            "BillingCycle": billing_cycle,
            "Type": type_,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def query_instance_bill(
            self,
            is_billing_item=None,
            product_code=None,
            is_hide_zero_charge=None,
            subscription_type=None,
            page_size=None,
            billing_cycle=None,
            owner_id=None,
            page_num=None,
            product_type=None):
        api_request = APIRequest('QueryInstanceBill', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IsBillingItem": is_billing_item,
            "ProductCode": product_code,
            "IsHideZeroCharge": is_hide_zero_charge,
            "SubscriptionType": subscription_type,
            "PageSize": page_size,
            "BillingCycle": billing_cycle,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def enable_bill_generation(self, product_code=None, owner_id=None):
        api_request = APIRequest('EnableBillGeneration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ProductCode": product_code, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_redeem(
            self,
            expiry_time_end=None,
            page_size=None,
            expiry_time_start=None,
            page_num=None,
            effective_or_not=None):
        api_request = APIRequest('QueryRedeem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExpiryTimeEnd": expiry_time_end,
            "PageSize": page_size,
            "ExpiryTimeStart": expiry_time_start,
            "PageNum": page_num,
            "EffectiveOrNot": effective_or_not}
        return self._handle_request(api_request).result

    def convert_charge_type(
            self,
            period=None,
            product_code=None,
            instance_id=None,
            subscription_type=None,
            owner_id=None,
            product_type=None):
        api_request = APIRequest('ConvertChargeType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "ProductCode": product_code,
            "InstanceId": instance_id,
            "SubscriptionType": subscription_type,
            "OwnerId": owner_id,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def create_instance(
            self,
            product_code=None,
            period=None,
            client_token=None,
            subscription_type=None,
            renew_period=None,
            list_of_parameter=None,
            renewal_status=None,
            owner_id=None,
            product_type=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "Period": period,
            "ClientToken": client_token,
            "SubscriptionType": subscription_type,
            "RenewPeriod": renew_period,
            "Parameter": list_of_parameter,
            "RenewalStatus": renewal_status,
            "OwnerId": owner_id,
            "ProductType": product_type}
        repeat_info = {"Parameter": ('Parameter', 'list', 'dict', [('Code', 'str', None, None),
                                                                   ('Value', 'str', None, None),
                                                                   ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_instance(
            self,
            product_code=None,
            instance_id=None,
            client_token=None,
            subscription_type=None,
            modify_type=None,
            list_of_parameter=None,
            owner_id=None,
            product_type=None):
        api_request = APIRequest('ModifyInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "InstanceId": instance_id,
            "ClientToken": client_token,
            "SubscriptionType": subscription_type,
            "ModifyType": modify_type,
            "Parameter": list_of_parameter,
            "OwnerId": owner_id,
            "ProductType": product_type}
        repeat_info = {"Parameter": ('Parameter', 'list', 'dict', [('Code', 'str', None, None),
                                                                   ('Value', 'str', None, None),
                                                                   ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_pricing_module(
            self,
            product_code=None,
            subscription_type=None,
            owner_id=None,
            product_type=None):
        api_request = APIRequest('DescribePricingModule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SubscriptionType": subscription_type,
            "OwnerId": owner_id,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def query_product_list(self, query_total_count=None, page_size=None, page_num=None):
        api_request = APIRequest('QueryProductList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "QueryTotalCount": query_total_count,
            "PageSize": page_size,
            "PageNum": page_num}
        return self._handle_request(api_request).result

    def query_instance_gaap_cost(
            self,
            product_code=None,
            subscription_type=None,
            page_size=None,
            billing_cycle=None,
            page_num=None,
            product_type=None):
        api_request = APIRequest('QueryInstanceGaapCost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SubscriptionType": subscription_type,
            "PageSize": page_size,
            "BillingCycle": billing_cycle,
            "PageNum": page_num,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def renew_instance(
            self,
            product_code=None,
            instance_id=None,
            client_token=None,
            renew_period=None,
            owner_id=None,
            product_type=None):
        api_request = APIRequest('RenewInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "InstanceId": instance_id,
            "ClientToken": client_token,
            "RenewPeriod": renew_period,
            "OwnerId": owner_id,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def get_order_detail(self, order_id=None, owner_id=None):
        api_request = APIRequest('GetOrderDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OrderId": order_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_orders(
            self,
            product_code=None,
            subscription_type=None,
            page_size=None,
            payment_status=None,
            create_time_start=None,
            page_num=None,
            owner_id=None,
            create_time_end=None,
            product_type=None,
            order_type=None):
        api_request = APIRequest('QueryOrders', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SubscriptionType": subscription_type,
            "PageSize": page_size,
            "PaymentStatus": payment_status,
            "CreateTimeStart": create_time_start,
            "PageNum": page_num,
            "OwnerId": owner_id,
            "CreateTimeEnd": create_time_end,
            "ProductType": product_type,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def query_monthly_instance_consumption(
            self,
            product_code=None,
            subscription_type=None,
            page_size=None,
            billing_cycle=None,
            owner_id=None,
            page_num=None,
            product_type=None):
        api_request = APIRequest('QueryMonthlyInstanceConsumption', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SubscriptionType": subscription_type,
            "PageSize": page_size,
            "BillingCycle": billing_cycle,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def query_settlement_bill(
            self,
            product_code=None,
            is_hide_zero_charge=None,
            subscription_type=None,
            page_size=None,
            end_time=None,
            billing_cycle=None,
            start_time=None,
            owner_id=None,
            page_num=None,
            type_=None,
            product_type=None):
        api_request = APIRequest('QuerySettlementBill', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "IsHideZeroCharge": is_hide_zero_charge,
            "SubscriptionType": subscription_type,
            "PageSize": page_size,
            "EndTime": end_time,
            "BillingCycle": billing_cycle,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "Type": type_,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def query_monthly_bill(self, billing_cycle=None):
        api_request = APIRequest('QueryMonthlyBill', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BillingCycle": billing_cycle}
        return self._handle_request(api_request).result

    def set_renewal(
            self,
            product_code=None,
            instance_ids=None,
            subscription_type=None,
            renewal_status=None,
            renewal_period_unit=None,
            renewal_period=None,
            owner_id=None,
            product_type=None):
        api_request = APIRequest('SetRenewal', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "InstanceIDs": instance_ids,
            "SubscriptionType": subscription_type,
            "RenewalStatus": renewal_status,
            "RenewalPeriodUnit": renewal_period_unit,
            "RenewalPeriod": renewal_period,
            "OwnerId": owner_id,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def query_available_instances(
            self,
            product_code=None,
            subscription_type=None,
            owner_id=None,
            page_num=None,
            end_time_start=None,
            product_type=None,
            create_time_end=None,
            instance_ids=None,
            end_time_end=None,
            page_size=None,
            create_time_start=None,
            region=None,
            renew_status=None):
        api_request = APIRequest('QueryAvailableInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SubscriptionType": subscription_type,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "EndTimeStart": end_time_start,
            "ProductType": product_type,
            "CreateTimeEnd": create_time_end,
            "InstanceIDs": instance_ids,
            "EndTimeEnd": end_time_end,
            "PageSize": page_size,
            "CreateTimeStart": create_time_start,
            "Region": region,
            "RenewStatus": renew_status}
        return self._handle_request(api_request).result

    def create_resource_package(
            self,
            duration=None,
            product_code=None,
            specification=None,
            owner_id=None,
            package_type=None,
            effective_date=None,
            pricing_cycle=None):
        api_request = APIRequest('CreateResourcePackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "ProductCode": product_code,
            "Specification": specification,
            "OwnerId": owner_id,
            "PackageType": package_type,
            "EffectiveDate": effective_date,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def query_resource_package_instances(
            self,
            expiry_time_end=None,
            product_code=None,
            page_size=None,
            owner_id=None,
            expiry_time_start=None,
            page_num=None):
        api_request = APIRequest('QueryResourcePackageInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExpiryTimeEnd": expiry_time_end,
            "ProductCode": product_code,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "ExpiryTimeStart": expiry_time_start,
            "PageNum": page_num}
        return self._handle_request(api_request).result

    def get_resource_package_price(
            self,
            duration=None,
            product_code=None,
            specification=None,
            owner_id=None,
            package_type=None,
            effective_date=None,
            pricing_cycle=None):
        api_request = APIRequest('GetResourcePackagePrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "ProductCode": product_code,
            "Specification": specification,
            "OwnerId": owner_id,
            "PackageType": package_type,
            "EffectiveDate": effective_date,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def get_subscription_price(
            self,
            service_period_quantity=None,
            product_code=None,
            instance_id=None,
            quantity=None,
            service_period_unit=None,
            subscription_type=None,
            list_of_module_list=None,
            owner_id=None,
            region=None,
            order_type=None,
            product_type=None):
        api_request = APIRequest('GetSubscriptionPrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ServicePeriodQuantity": service_period_quantity,
            "ProductCode": product_code,
            "InstanceId": instance_id,
            "Quantity": quantity,
            "ServicePeriodUnit": service_period_unit,
            "SubscriptionType": subscription_type,
            "ModuleList": list_of_module_list,
            "OwnerId": owner_id,
            "Region": region,
            "OrderType": order_type,
            "ProductType": product_type}
        repeat_info = {"ModuleList": ('ModuleList', 'list', 'dict', [('ModuleCode', 'str', None, None),
                                                                     ('ModuleStatus', 'str', None, None),
                                                                     ('Tag', 'str', None, None),
                                                                     ('Config', 'str', None, None),
                                                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_pay_as_you_go_price(
            self,
            product_code=None,
            subscription_type=None,
            list_of_module_list=None,
            owner_id=None,
            region=None,
            product_type=None):
        api_request = APIRequest('GetPayAsYouGoPrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SubscriptionType": subscription_type,
            "ModuleList": list_of_module_list,
            "OwnerId": owner_id,
            "Region": region,
            "ProductType": product_type}
        repeat_info = {"ModuleList": ('ModuleList', 'list', 'dict', [('ModuleCode', 'str', None, None),
                                                                     ('PriceType', 'str', None, None),
                                                                     ('Config', 'str', None, None),
                                                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def query_prepaid_cards(
            self,
            expiry_time_end=None,
            expiry_time_start=None,
            effective_or_not=None):
        api_request = APIRequest('QueryPrepaidCards', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExpiryTimeEnd": expiry_time_end,
            "ExpiryTimeStart": expiry_time_start,
            "EffectiveOrNot": effective_or_not}
        return self._handle_request(api_request).result

    def query_cash_coupons(
            self,
            expiry_time_end=None,
            expiry_time_start=None,
            effective_or_not=None):
        api_request = APIRequest('QueryCashCoupons', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExpiryTimeEnd": expiry_time_end,
            "ExpiryTimeStart": expiry_time_start,
            "EffectiveOrNot": effective_or_not}
        return self._handle_request(api_request).result

    def query_account_balance(self,):
        api_request = APIRequest('QueryAccountBalance', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def describe_resource_package_product(self, product_code=None):
        api_request = APIRequest('DescribeResourcePackageProduct', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ProductCode": product_code}
        return self._handle_request(api_request).result
