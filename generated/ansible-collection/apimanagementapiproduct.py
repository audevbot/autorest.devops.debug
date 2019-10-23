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
module: apimanagementapiproduct
version_added: '2.9'
short_description: Manage Azure ApiProduct instance.
description:
  - 'Create, update and delete instance of Azure ApiProduct.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  api_id:
    description:
      - >-
        API identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  value:
    description:
      - Page values.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type for API Management resource.
        type: str
      description:
        description:
          - Product description. May include HTML formatting tags.
        type: str
      terms:
        description:
          - >-
            Product terms of use. Developers trying to subscribe to the product
            will be presented and required to accept these terms before they can
            complete the subscription process.
        type: str
      subscription_required:
        description:
          - >-
            Whether a product subscription is required for accessing APIs
            included in this product. If true, the product is referred to as
            "protected" and a valid subscription key is required for a request
            to an API included in the product to succeed. If false, the product
            is referred to as "open" and requests to an API included in the
            product can be made without a subscription key. If property is
            omitted when creating a new product it's value is assumed to be
            true.
        type: boolean
      approval_required:
        description:
          - >-
            whether subscription approval is required. If false, new
            subscriptions will be approved automatically enabling developers to
            call the product’s APIs immediately after subscribing. If true,
            administrators must manually approve the subscription before the
            developer can any of the product’s APIs. Can be present only if
            subscriptionRequired property is present and has a value of false.
        type: boolean
      subscriptions_limit:
        description:
          - >-
            Whether the number of subscriptions a user can have to this product
            at the same time. Set to null or omit to allow unlimited per user
            subscriptions. Can be present only if subscriptionRequired property
            is present and has a value of false.
        type: number
      state:
        description:
          - >-
            whether product is published or not. Published products are
            discoverable by users of developer portal. Non published products
            are visible only to administrators. Default state of Product is
            notPublished.
        type: str
      display_name:
        description:
          - Product name.
        required: true
        type: str
  next_link:
    description:
      - Next page link if any.
    type: str
  state:
    description:
      - Assert the state of the ApiProduct.
      - >-
        Use C(present) to create or update an ApiProduct and C(absent) to delete
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
[]

'''

RETURN = '''
value:
  description:
    - Page values.
  returned: always
  type: dict
  sample: null
  contains:
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
        - Product entity contract properties.
      returned: always
      type: dict
      sample: null
    description:
      description:
        - Product description. May include HTML formatting tags.
      returned: always
      type: str
      sample: null
    terms:
      description:
        - >-
          Product terms of use. Developers trying to subscribe to the product
          will be presented and required to accept these terms before they can
          complete the subscription process.
      returned: always
      type: str
      sample: null
    subscription_required:
      description:
        - >-
          Whether a product subscription is required for accessing APIs included
          in this product. If true, the product is referred to as "protected"
          and a valid subscription key is required for a request to an API
          included in the product to succeed. If false, the product is referred
          to as "open" and requests to an API included in the product can be
          made without a subscription key. If property is omitted when creating
          a new product it's value is assumed to be true.
      returned: always
      type: boolean
      sample: null
    approval_required:
      description:
        - >-
          whether subscription approval is required. If false, new subscriptions
          will be approved automatically enabling developers to call the
          product’s APIs immediately after subscribing. If true, administrators
          must manually approve the subscription before the developer can any of
          the product’s APIs. Can be present only if subscriptionRequired
          property is present and has a value of false.
      returned: always
      type: boolean
      sample: null
    subscriptions_limit:
      description:
        - >-
          Whether the number of subscriptions a user can have to this product at
          the same time. Set to null or omit to allow unlimited per user
          subscriptions. Can be present only if subscriptionRequired property is
          present and has a value of false.
      returned: always
      type: number
      sample: null
    state:
      description:
        - >-
          whether product is published or not. Published products are
          discoverable by users of developer portal. Non published products are
          visible only to administrators. Default state of Product is
          notPublished.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - Product name.
      returned: always
      type: str
      sample: null
next_link:
  description:
    - Next page link if any.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApiProduct(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                disposition='serviceName',
                required=true
            ),
            api_id=dict(
                type='str',
                updatable=False,
                disposition='apiId',
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.api_id = None
        self.value = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMApiProduct, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/apis' +
                    '/{{ api_name }}' +
                    '/products')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ api_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("ApiProduct instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ApiProduct instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ApiProduct instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('ApiProduct instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ApiProduct instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["value"] = response["value"]
           self.results["next_link"] = response["next_link"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the ApiProduct instance {0}'.format(self.))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
            else:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
        except CloudError as exc:
            self.log('Error attempting to create the ApiProduct instance.')
            self.fail('Error creating the ApiProduct instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ApiProduct instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the ApiProduct instance.')
            self.fail('Error deleting the ApiProduct instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ApiProduct instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("ApiProduct instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ApiProduct instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMApiProduct()


if __name__ == '__main__':
    main()
