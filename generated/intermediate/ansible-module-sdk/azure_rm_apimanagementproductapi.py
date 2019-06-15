#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_apimanagementproductapi
version_added: '2.9'
short_description: Manage Azure ProductApi instance.
description:
  - 'Create, update and delete instance of Azure ProductApi.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
    required: true
  api_id:
    description:
      - >-
        API revision identifier. Must be unique in the current API Management
        service instance. Non-current revision has ;rev=n as a suffix where n is
        the revision number.
    required: true
  id:
    description:
      - Resource ID.
  type:
    description:
      - Type of API.
  description:
    description:
      - Description of the API. May include HTML formatting tags.
  authentication_settings:
    description:
      - Collection of authentication settings included into this API.
    suboptions:
      o_auth2:
        description:
          - OAuth2 Authentication settings
        suboptions:
          authorization_server_id:
            description:
              - OAuth authorization server identifier.
          scope:
            description:
              - operations scope.
      openid:
        description:
          - OpenID Connect Authentication Settings
        suboptions:
          openid_provider_id:
            description:
              - OAuth authorization server identifier.
          bearer_token_sending_methods:
            description:
              - How to send token to the server.
            type: list
      subscription_key_required:
        description:
          - >-
            Specifies whether subscription key is required during call to this
            API, true - API is included into closed products only, false - API
            is included into open products alone, null - there is a mix of
            products.
  subscription_key_parameter_names:
    description:
      - Protocols over which API is made available.
    suboptions:
      header:
        description:
          - Subscription key header name.
      query:
        description:
          - Subscription key query string parameter name.
  api_revision:
    description:
      - >-
        Describes the Revision of the Api. If no value is provided, default
        revision 1 is created
  api_version:
    description:
      - Indicates the Version identifier of the API if the API is versioned
  is_current:
    description:
      - Indicates if API revision is current api revision.
  is_online:
    description:
      - Indicates if API revision is accessible via the gateway.
  api_revision_description:
    description:
      - Description of the Api Revision.
  api_version_description:
    description:
      - Description of the Api Version.
  api_version_set_id:
    description:
      - A resource identifier for the related ApiVersionSet.
  subscription_required:
    description:
      - >-
        Specifies whether an API or Product subscription is required for
        accessing the API.
  source_api_id:
    description:
      - API identifier of the source API.
  display_name:
    description:
      - API name. Must be 1 to 300 characters long.
  service_url:
    description:
      - >-
        Absolute URL of the backend service implementing this API. Cannot be
        more than 2000 characters long.
  path:
    description:
      - >-
        Relative URL uniquely identifying this API and all of its resource paths
        within the API Management service instance. It is appended to the API
        endpoint base URL specified during the service instance creation to form
        a public URL for this API.
    required: true
  protocols:
    description:
      - Describes on which protocols the operations in this API can be invoked.
    type: list
  api_version_set:
    description:
      - Version set details
    suboptions:
      id:
        description:
          - >-
            Identifier for existing API Version Set. Omit this value to create a
            new Version Set.
      name:
        description:
          - The display Name of the API Version Set.
      description:
        description:
          - Description of API Version Set.
      versioning_scheme:
        description:
          - >-
            An value that determines where the API Version identifer will be
            located in a HTTP request.
      version_query_name:
        description:
          - >-
            Name of query parameter that indicates the API Version if
            versioningScheme is set to `query`.
      version_header_name:
        description:
          - >-
            Name of HTTP header parameter that indicates the API Version if
            versioningScheme is set to `header`.
  state:
    description:
      - Assert the state of the ProductApi.
      - >-
        Use C(present) to create or update an ProductApi and C(absent) to delete
        it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementCreateProductApi
  azure_rm_apimanagementproductapi:
    resource_group: myResourceGroup
    name: myService
    product_id: myProduct
    api_id: myApis
- name: ApiManagementDeleteProductApi
  azure_rm_apimanagementproductapi:
    resource_group: myResourceGroup
    name: myService
    product_id: myProduct
    api_id: myApis
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type for API Management resource.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Api entity contract properties.
  returned: always
  type: dict
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMProductApi(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='service_name',
                required=true
            ),
            product_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            api_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            authentication_settings=dict(
                type='dict',
                disposition='/',
                options=dict(
                    o_auth2=dict(
                        type='dict',
                        options=dict(
                            authorization_server_id=dict(
                                type='str'
                            ),
                            scope=dict(
                                type='str'
                            )
                        )
                    ),
                    openid=dict(
                        type='dict',
                        options=dict(
                            openid_provider_id=dict(
                                type='str'
                            ),
                            bearer_token_sending_methods=dict(
                                type='list'
                            )
                        )
                    ),
                    subscription_key_required=dict(
                        type='boolean'
                    )
                )
            ),
            subscription_key_parameter_names=dict(
                type='dict',
                disposition='/',
                options=dict(
                    header=dict(
                        type='str'
                    ),
                    query=dict(
                        type='str'
                    )
                )
            ),
            type=dict(
                type='str',
                disposition='/',
                choices=['http',
                         'soap']
            ),
            api_revision=dict(
                type='str',
                disposition='/'
            ),
            api_version=dict(
                type='str',
                disposition='/'
            ),
            is_current=dict(
                type='boolean',
                disposition='/'
            ),
            is_online=dict(
                type='boolean',
                disposition='/'
            ),
            api_revision_description=dict(
                type='str',
                disposition='/'
            ),
            api_version_description=dict(
                type='str',
                disposition='/'
            ),
            api_version_set_id=dict(
                type='str',
                disposition='/'
            ),
            subscription_required=dict(
                type='boolean',
                disposition='/'
            ),
            source_api_id=dict(
                type='str',
                disposition='/'
            ),
            display_name=dict(
                type='str',
                disposition='/'
            ),
            service_url=dict(
                type='str',
                disposition='/'
            ),
            path=dict(
                type='str',
                disposition='/',
                required=true
            ),
            protocols=dict(
                type='list',
                disposition='/'
            ),
            api_version_set=dict(
                type='dict',
                disposition='/',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    name=dict(
                        type='str'
                    ),
                    description=dict(
                        type='str'
                    ),
                    versioning_scheme=dict(
                        type='str',
                        choices=['Segment',
                                 'Query',
                                 'Header']
                    ),
                    version_query_name=dict(
                        type='str'
                    ),
                    version_header_name=dict(
                        type='str'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.product_id = None
        self.api_id = None
        self.id = None
        self.name = None
        self.type = None
        self.properties = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMProductApi, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                supports_check_mode=True,
                                                supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if self.location is None:
            self.location = resource_group.location

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.product_api.create_or_update(resource_group_name=self.resource_group,
                                                                     service_name=self.name,
                                                                     product_id=self.product_id,
                                                                     api_id=self.api_id)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ProductApi instance.')
            self.fail('Error creating the ProductApi instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ProductApi instance {0}'.format(self.))
        try:
            response = self.mgmt_client.product_api.delete(resource_group_name=self.resource_group,
                                                           service_name=self.name,
                                                           product_id=self.product_id,
                                                           api_id=self.api_id)
        except CloudError as e:
            self.log('Error attempting to delete the ProductApi instance.')
            self.fail('Error deleting the ProductApi instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ProductApi instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.product_api.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMProductApi()


if __name__ == '__main__':
    main()