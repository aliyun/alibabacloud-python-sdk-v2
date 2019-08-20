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


class CasClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'cas'
        self.api_version = '2018-08-13'
        self.location_service_code = 'cas_esign_fdd'
        self.location_endpoint_type = 'openAPI'

    def describe_order_count_for_console_index(self, resource_group_id=None, source_ip=None):
        api_request = APIRequest('DescribeOrderCountForConsoleIndex', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceGroupId": resource_group_id, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_renew_order(self, resource_group_id=None, source_ip=None, order_id=None):
        api_request = APIRequest('DescribeRenewOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id}
        return self._handle_request(api_request).result

    def untag_resources(
            self,
            all_=None,
            list_of_resource_id=None,
            source_ip=None,
            region_id=None,
            list_of_tag_key=None,
            resource_type=None):
        api_request = APIRequest('UntagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "All": all_,
            "ResourceId": list_of_resource_id,
            "SourceIp": source_ip,
            "RegionId": region_id,
            "TagKey": list_of_tag_key,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "TagKey": ('TagKey', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def tag_resources(
            self,
            list_of_resource_id=None,
            source_ip=None,
            region_id=None,
            scope=None,
            tag_owner_uid=None,
            tag_owner_bid=None,
            list_of_tag=None,
            resource_type=None):
        api_request = APIRequest('TagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": list_of_resource_id,
            "SourceIp": source_ip,
            "RegionId": region_id,
            "Scope": scope,
            "TagOwnerUid": tag_owner_uid,
            "TagOwnerBid": tag_owner_bid,
            "Tag": list_of_tag,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_tag_resources(
            self,
            list_of_resource_id=None,
            source_ip=None,
            region_id=None,
            next_token=None,
            list_of_tag=None,
            resource_type=None):
        api_request = APIRequest('ListTagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": list_of_resource_id,
            "SourceIp": source_ip,
            "RegionId": region_id,
            "NextToken": next_token,
            "Tag": list_of_tag,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_tag_keys(
            self,
            source_ip=None,
            region_id=None,
            page_size=None,
            current_page=None,
            resource_type=None):
        api_request = APIRequest('ListTagKeys', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "RegionId": region_id,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def describe_signature_product_state(self, resource_group_id=None, source_ip=None):
        api_request = APIRequest('DescribeSignatureProductState', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceGroupId": resource_group_id, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_order_refund_record(self, resource_group_id=None, source_ip=None):
        api_request = APIRequest('DescribeOrderRefundRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceGroupId": resource_group_id, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def create_order_refund_record(
            self,
            reason=None,
            resource_group_id=None,
            source_ip=None,
            order_id=None):
        api_request = APIRequest('CreateOrderRefundRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Reason": reason,
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id}
        return self._handle_request(api_request).result

    def describe_location_list(self, resource_group_id=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeLocationList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def delete_order(self, resource_group_id=None, source_ip=None, order_id=None, lang=None):
        api_request = APIRequest('DeleteOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def create_cooperation_order(
            self,
            resource_group_id=None,
            product_code=None,
            source_ip=None,
            domain=None,
            from_=None,
            lang=None):
        api_request = APIRequest('CreateCooperationOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "ProductCode": product_code,
            "SourceIp": source_ip,
            "Domain": domain,
            "From": from_,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_sts_auth_status(
            self,
            resource_group_id=None,
            source_ip=None,
            cloud_product=None,
            lang=None):
        api_request = APIRequest('DescribeStsAuthStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "CloudProduct": cloud_product,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_signature_trade_list(
            self,
            resource_group_id=None,
            source_ip=None,
            show_size=None,
            search_type=None,
            current_page=None,
            lang=None,
            search_value=None):
        api_request = APIRequest('DescribeSignatureTradeList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "ShowSize": show_size,
            "SearchType": search_type,
            "CurrentPage": current_page,
            "Lang": lang,
            "SearchValue": search_value}
        return self._handle_request(api_request).result

    def describe_signature_trade_detail(
            self,
            resource_group_id=None,
            source_ip=None,
            lang=None,
            transaction_id=None):
        api_request = APIRequest('DescribeSignatureTradeDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "Lang": lang,
            "TransactionId": transaction_id}
        return self._handle_request(api_request).result

    def describe_signature_statistics(self, resource_group_id=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeSignatureStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_signature_capacity(self, resource_group_id=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeSignatureCapacity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_oss_upload_info(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            document_type=None,
            lang=None):
        api_request = APIRequest('DescribeOSSUploadInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "DocumentType": document_type,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_oss_download_info(
            self,
            resource_group_id=None,
            source_ip=None,
            oss_key=None,
            lang=None):
        api_request = APIRequest('DescribeOSSDownloadInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OssKey": oss_key,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_order_material(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            lang=None):
        api_request = APIRequest('DescribeOrderMaterial', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_order_list(
            self,
            resource_group_id=None,
            source_ip=None,
            show_size=None,
            brand_id=None,
            current_page=None,
            list_of_tag=None,
            keyword=None,
            lang=None,
            status=None):
        api_request = APIRequest('DescribeOrderList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "ShowSize": show_size,
            "BrandId": brand_id,
            "CurrentPage": current_page,
            "Tag": list_of_tag,
            "Keyword": keyword,
            "Lang": lang,
            "Status": status}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_order_document(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            type_=None,
            lang=None):
        api_request = APIRequest('DescribeOrderDocument', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Type": type_,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_order_detail(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            lang=None):
        api_request = APIRequest('DescribeOrderDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_order_audit_fail_record(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            lang=None):
        api_request = APIRequest('DescribeOrderAuditFailRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_help_list(self, resource_group_id=None, source_ip=None, category=None, lang=None):
        api_request = APIRequest('DescribeHelpList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "Category": category,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_expectation_result(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            expectation_type=None,
            lang=None):
        api_request = APIRequest('DescribeExpectationResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "ExpectationType": expectation_type,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_download_domain_verify_configuration(
            self, resource_group_id=None, source_ip=None, order_id=None, lang=None):
        api_request = APIRequest(
            'DescribeDownloadDomainVerifyConfiguration',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_download_certificate(
            self,
            resource_group_id=None,
            source_ip=None,
            server_type=None,
            certificate_id=None,
            lang=None):
        api_request = APIRequest('DescribeDownloadCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "ServerType": server_type,
            "CertificateId": certificate_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_domain_verify_info(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            lang=None):
        api_request = APIRequest('DescribeDomainVerifyInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_domain_verify_configuration_status(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            lang=None):
        api_request = APIRequest(
            'DescribeDomainVerifyConfigurationStatus',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_deployment_region_list(
            self,
            resource_group_id=None,
            source_ip=None,
            certificate_id=None,
            cloud_product=None,
            lang=None):
        api_request = APIRequest('DescribeDeploymentRegionList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "CertificateId": certificate_id,
            "CloudProduct": cloud_product,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_deployment_product(
            self,
            resource_group_id=None,
            source_ip=None,
            certificate_id=None,
            lang=None):
        api_request = APIRequest('DescribeDeploymentProduct', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "CertificateId": certificate_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_deployment_domain_list(
            self,
            resource_group_id=None,
            source_ip=None,
            certificate_id=None,
            cloud_product=None,
            lang=None):
        api_request = APIRequest('DescribeDeploymentDomainList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "CertificateId": certificate_id,
            "CloudProduct": cloud_product,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_deployment_detail(
            self,
            resource_group_id=None,
            source_ip=None,
            certificate_id=None,
            lang=None):
        api_request = APIRequest('DescribeDeploymentDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "CertificateId": certificate_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_certificate_status_count(
            self,
            resource_group_id=None,
            source_ip=None,
            list_of_tag=None,
            lang=None):
        api_request = APIRequest('DescribeCertificateStatusCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "Tag": list_of_tag,
            "Lang": lang}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_certificate_list(
            self,
            resource_group_id=None,
            source_ip=None,
            sort_type=None,
            show_size=None,
            sort_column=None,
            current_page=None,
            list_of_tag=None,
            lang=None,
            keyword=None,
            status=None):
        api_request = APIRequest('DescribeCertificateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "SortType": sort_type,
            "ShowSize": show_size,
            "SortColumn": sort_column,
            "CurrentPage": current_page,
            "Tag": list_of_tag,
            "Lang": lang,
            "Keyword": keyword,
            "Status": status}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_certificate_detail(
            self,
            resource_group_id=None,
            source_ip=None,
            certificate_id=None,
            lang=None):
        api_request = APIRequest('DescribeCertificateDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "CertificateId": certificate_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_certificate_brand_list(self, resource_group_id=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeCertificateBrandList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def delete_certificate(
            self,
            resource_group_id=None,
            source_ip=None,
            certificate_id=None,
            lang=None):
        api_request = APIRequest('DeleteCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "CertificateId": certificate_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def create_web_signature(
            self,
            quantity=None,
            hand_sign_img=None,
            doc_id=None,
            custom_api=None,
            position_page=None,
            doc_title=None,
            position_x=None,
            position_y=None,
            resource_group_id=None,
            source_ip=None,
            people_id=None,
            position_type=None,
            sign_keyword=None,
            notify_url=None,
            validity=None,
            return_url=None,
            lang=None,
            keyword_strategy=None):
        api_request = APIRequest('CreateWebSignature', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Quantity": quantity,
            "HandSignImg": hand_sign_img,
            "DocId": doc_id,
            "CustomApi": custom_api,
            "PositionPage": position_page,
            "DocTitle": doc_title,
            "PositionX": position_x,
            "PositionY": position_y,
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "PeopleId": people_id,
            "PositionType": position_type,
            "SignKeyword": sign_keyword,
            "NotifyUrl": notify_url,
            "Validity": validity,
            "ReturnUrl": return_url,
            "Lang": lang,
            "KeywordStrategy": keyword_strategy}
        return self._handle_request(api_request).result

    def create_un_deployment(
            self,
            resource_group_id=None,
            source_ip=None,
            deployment_id=None,
            lang=None):
        api_request = APIRequest('CreateUnDeployment', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "DeploymentId": deployment_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def create_signature_people_certificate(
            self,
            people_name=None,
            resource_group_id=None,
            source_ip=None,
            mobile=None,
            identity_number=None,
            lang=None,
            email=None):
        api_request = APIRequest('CreateSignaturePeopleCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PeopleName": people_name,
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "Mobile": mobile,
            "IdentityNumber": identity_number,
            "Lang": lang,
            "Email": email}
        return self._handle_request(api_request).result

    def create_signature_document(
            self,
            resource_group_id=None,
            source_ip=None,
            doc_content=None,
            lang=None,
            doc_title=None):
        api_request = APIRequest('CreateSignatureDocument', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "DocContent": doc_content,
            "Lang": lang,
            "DocTitle": doc_title}
        return self._handle_request(api_request).result

    def create_signature(
            self,
            icon_id=None,
            quantity=None,
            hand_sign_img=None,
            doc_id=None,
            custom_api=None,
            position_page=None,
            doc_title=None,
            position_x=None,
            position_y=None,
            resource_group_id=None,
            source_ip=None,
            people_id=None,
            position_type=None,
            sign_keyword=None,
            notify_url=None,
            validity=None,
            return_url=None,
            lang=None,
            keyword_strategy=None):
        api_request = APIRequest('CreateSignature', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IconId": icon_id,
            "Quantity": quantity,
            "HandSignImg": hand_sign_img,
            "DocId": doc_id,
            "CustomApi": custom_api,
            "PositionPage": position_page,
            "DocTitle": doc_title,
            "PositionX": position_x,
            "PositionY": position_y,
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "PeopleId": people_id,
            "PositionType": position_type,
            "SignKeyword": sign_keyword,
            "NotifyUrl": notify_url,
            "Validity": validity,
            "ReturnUrl": return_url,
            "Lang": lang,
            "KeywordStrategy": keyword_strategy}
        return self._handle_request(api_request).result

    def create_order_revoke(
            self,
            reason=None,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            lang=None):
        api_request = APIRequest('CreateOrderRevoke', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Reason": reason,
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def create_order_material(
            self,
            leader_name=None,
            city=None,
            country_code=None,
            leader_email=None,
            company_address=None,
            resource_group_id=None,
            company_code=None,
            person_email=None,
            province=None,
            domain_auth_type=None,
            leader_phone=None,
            source_ip=None,
            csr_content=None,
            lang=None,
            person_name=None,
            person_id_card_number=None,
            order_id=None,
            leader_title=None,
            person_title=None,
            post_code=None,
            create_csr=None,
            person_phone=None,
            company_name=None,
            company_phone=None,
            company_type=None,
            domain=None,
            person_department=None):
        api_request = APIRequest('CreateOrderMaterial', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LeaderName": leader_name,
            "City": city,
            "CountryCode": country_code,
            "LeaderEmail": leader_email,
            "CompanyAddress": company_address,
            "ResourceGroupId": resource_group_id,
            "CompanyCode": company_code,
            "PersonEmail": person_email,
            "Province": province,
            "DomainAuthType": domain_auth_type,
            "LeaderPhone": leader_phone,
            "SourceIp": source_ip,
            "CsrContent": csr_content,
            "Lang": lang,
            "PersonName": person_name,
            "PersonIdCardNumber": person_id_card_number,
            "OrderId": order_id,
            "LeaderTitle": leader_title,
            "PersonTitle": person_title,
            "PostCode": post_code,
            "CreateCsr": create_csr,
            "PersonPhone": person_phone,
            "CompanyName": company_name,
            "CompanyPhone": company_phone,
            "CompanyType": company_type,
            "Domain": domain,
            "PersonDepartment": person_department}
        return self._handle_request(api_request).result

    def create_order_document(
            self,
            resource_group_id=None,
            oss_key=None,
            source_ip=None,
            order_id=None,
            document_type=None,
            lang=None,
            ext_name=None):
        api_request = APIRequest('CreateOrderDocument', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "OssKey": oss_key,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "DocumentType": document_type,
            "Lang": lang,
            "ExtName": ext_name}
        return self._handle_request(api_request).result

    def create_order_cancel(self, resource_group_id=None, source_ip=None, order_id=None, lang=None):
        api_request = APIRequest('CreateOrderCancel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def create_order_audit(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            lang=None,
            type_=None):
        api_request = APIRequest('CreateOrderAudit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang,
            "Type": type_}
        return self._handle_request(api_request).result

    def create_filing_signature_document(
            self,
            resource_group_id=None,
            source_ip=None,
            doc_id=None,
            lang=None):
        api_request = APIRequest('CreateFilingSignatureDocument', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "DocId": doc_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def create_domain_verify_configuration_status(
            self,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            lang=None,
            type_=None):
        api_request = APIRequest('CreateDomainVerifyConfigurationStatus',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang,
            "Type": type_}
        return self._handle_request(api_request).result

    def create_deployment(
            self,
            resource_group_id=None,
            source_ip=None,
            certificate_id=None,
            domain=None,
            cloud_product=None,
            lang=None,
            region=None):
        api_request = APIRequest('CreateDeployment', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "CertificateId": certificate_id,
            "Domain": domain,
            "CloudProduct": cloud_product,
            "Lang": lang,
            "Region": region}
        return self._handle_request(api_request).result

    def create_certificate_name(
            self,
            resource_group_id=None,
            source_ip=None,
            certificate_id=None,
            name=None,
            lang=None):
        api_request = APIRequest('CreateCertificateName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "CertificateId": certificate_id,
            "Name": name,
            "Lang": lang}
        return self._handle_request(api_request).result

    def create_certificate(
            self,
            resource_group_id=None,
            source_ip=None,
            name=None,
            cert=None,
            lang=None,
            key=None):
        api_request = APIRequest('CreateCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "Name": name,
            "Cert": cert,
            "Lang": lang,
            "Key": key}
        return self._handle_request(api_request).result

    def create_ali_dns_record_id(
            self,
            record_id=None,
            resource_group_id=None,
            source_ip=None,
            order_id=None,
            lang=None):
        api_request = APIRequest('CreateAliDnsRecordId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordId": record_id,
            "ResourceGroupId": resource_group_id,
            "SourceIp": source_ip,
            "OrderId": order_id,
            "Lang": lang}
        return self._handle_request(api_request).result
