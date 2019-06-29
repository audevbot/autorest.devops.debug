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
module: azure_rm_apimanagementapioperation
version_added: '2.9'
short_description: Manage Azure ApiOperation instance.
description:
  - 'Create, update and delete instance of Azure ApiOperation.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  api_id:
    description:
      - >-
        API revision identifier. Must be unique in the current API Management
        service instance. Non-current revision has ;rev=n as a suffix where n is
        the revision number.
    required: true
  operation_id:
    description:
      - >-
        Operation identifier within an API. Must be unique in the current API
        Management service instance.
    required: true
  template_parameters:
    description:
      - Collection of URL template parameters.
    type: list
    suboptions:
      name:
        description:
          - Parameter name.
        required: true
      description:
        description:
          - Parameter description.
      type:
        description:
          - Parameter type.
        required: true
      default_value:
        description:
          - Default parameter value.
      required:
        description:
          - Specifies whether parameter is required or not.
      values:
        description:
          - Parameter values.
        type: list
  description:
    description:
      - Description of the operation. May include HTML formatting tags.
  request:
    description:
      - An entity containing request details.
    suboptions:
      description:
        description:
          - Operation request description.
      query_parameters:
        description:
          - Collection of operation request query parameters.
        type: list
        suboptions:
          name:
            description:
              - Parameter name.
            required: true
          description:
            description:
              - Parameter description.
          type:
            description:
              - Parameter type.
            required: true
          default_value:
            description:
              - Default parameter value.
          required:
            description:
              - Specifies whether parameter is required or not.
          values:
            description:
              - Parameter values.
            type: list
      headers:
        description:
          - Collection of operation request headers.
        type: list
        suboptions:
          name:
            description:
              - Parameter name.
            required: true
          description:
            description:
              - Parameter description.
          type:
            description:
              - Parameter type.
            required: true
          default_value:
            description:
              - Default parameter value.
          required:
            description:
              - Specifies whether parameter is required or not.
          values:
            description:
              - Parameter values.
            type: list
      representations:
        description:
          - Collection of operation request representations.
        type: list
        suboptions:
          content_type:
            description:
              - >-
                Specifies a registered or custom content type for this
                representation, e.g. application/xml.
            required: true
          sample:
            description:
              - An example of the representation.
          schema_id:
            description:
              - >-
                Schema identifier. Applicable only if 'contentType' value is
                neither 'application/x-www-form-urlencoded' nor
                'multipart/form-data'.
          type_name:
            description:
              - >-
                Type name defined by the schema. Applicable only if
                'contentType' value is neither
                'application/x-www-form-urlencoded' nor 'multipart/form-data'.
          form_parameters:
            description:
              - >-
                Collection of form parameters. Required if 'contentType' value
                is either 'application/x-www-form-urlencoded' or
                'multipart/form-data'..
            type: list
            suboptions:
              name:
                description:
                  - Parameter name.
                required: true
              description:
                description:
                  - Parameter description.
              type:
                description:
                  - Parameter type.
                required: true
              default_value:
                description:
                  - Default parameter value.
              required:
                description:
                  - Specifies whether parameter is required or not.
              values:
                description:
                  - Parameter values.
                type: list
  responses:
    description:
      - Array of Operation responses.
    type: list
    suboptions:
      status_code:
        description:
          - Operation response HTTP status code.
        required: true
      description:
        description:
          - Operation response description.
      representations:
        description:
          - Collection of operation response representations.
        type: list
        suboptions:
          content_type:
            description:
              - >-
                Specifies a registered or custom content type for this
                representation, e.g. application/xml.
            required: true
          sample:
            description:
              - An example of the representation.
          schema_id:
            description:
              - >-
                Schema identifier. Applicable only if 'contentType' value is
                neither 'application/x-www-form-urlencoded' nor
                'multipart/form-data'.
          type_name:
            description:
              - >-
                Type name defined by the schema. Applicable only if
                'contentType' value is neither
                'application/x-www-form-urlencoded' nor 'multipart/form-data'.
          form_parameters:
            description:
              - >-
                Collection of form parameters. Required if 'contentType' value
                is either 'application/x-www-form-urlencoded' or
                'multipart/form-data'..
            type: list
            suboptions:
              name:
                description:
                  - Parameter name.
                required: true
              description:
                description:
                  - Parameter description.
              type:
                description:
                  - Parameter type.
                required: true
              default_value:
                description:
                  - Default parameter value.
              required:
                description:
                  - Specifies whether parameter is required or not.
              values:
                description:
                  - Parameter values.
                type: list
      headers:
        description:
          - Collection of operation response headers.
        type: list
        suboptions:
          name:
            description:
              - Parameter name.
            required: true
          description:
            description:
              - Parameter description.
          type:
            description:
              - Parameter type.
            required: true
          default_value:
            description:
              - Default parameter value.
          required:
            description:
              - Specifies whether parameter is required or not.
          values:
            description:
              - Parameter values.
            type: list
  policies:
    description:
      - Operation Policies
  display_name:
    description:
      - Operation Name.
    required: true
  method:
    description:
      - >-
        A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST
        but not limited by only them.
    required: true
  url_template:
    description:
      - >-
        Relative URL template identifying the target resource for this
        operation. May include parameters. Example:
        /customers/{cid}/orders/{oid}/?date={date}
    required: true
  id:
    description:
      - Resource ID.
  name:
    description:
      - Resource name.
  type:
    description:
      - Resource type for API Management resource.
  state:
    description:
      - Assert the state of the ApiOperation.
      - >-
        Use C(present) to create or update an ApiOperation and C(absent) to
        delete it.
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
- name: ApiManagementCreateApiOperation
  azure_rm_apimanagementapioperation:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    operation_id: myOperation
    template_parameters: []
    description: This can only be done by the logged in user.
    request:
      description: Created user object
      query_parameters: []
      headers: []
      representations:
        - content_type: application/json
          schema_id: 592f6c1d0af5840ca8897f0c
          type_name: User
    responses:
      - status_code: '200'
        description: successful operation
        representations:
          - content_type: application/xml
          - content_type: application/json
        headers: []
    display_name: createUser2
    method: POST
    url_template: /user1
- name: ApiManagementUpdateApiOperation
  azure_rm_apimanagementapioperation:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    operation_id: myOperation
    template_parameters: []
    request:
      query_parameters:
        - name: param1
          description: >-
            A sample parameter that is required and has a default value of
            "sample".
          type: string
          default_value: sample
          required: true
          values:
            - sample
    responses:
      - status_code: '200'
        description: Returned in all cases.
        representations: []
        headers: []
      - status_code: '500'
        description: Server Error.
        representations: []
        headers: []
    display_name: Retrieve resource
    method: GET
    url_template: /resource
- name: ApiManagementDeleteApiOperation
  azure_rm_apimanagementapioperation:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    operation_id: myOperation
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
    - Properties of the Operation Contract.
  returned: always
  type: dict
  sample: null
  contains:
    template_parameters:
      description:
        - Collection of URL template parameters.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Parameter name.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Parameter description.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Parameter type.
          returned: always
          type: str
          sample: null
        default_value:
          description:
            - Default parameter value.
          returned: always
          type: str
          sample: null
        required:
          description:
            - Specifies whether parameter is required or not.
          returned: always
          type: boolean
          sample: null
        values:
          description:
            - Parameter values.
          returned: always
          type: str
          sample: null
    description:
      description:
        - Description of the operation. May include HTML formatting tags.
      returned: always
      type: str
      sample: null
    request:
      description:
        - An entity containing request details.
      returned: always
      type: dict
      sample: null
      contains:
        description:
          description:
            - Operation request description.
          returned: always
          type: str
          sample: null
        query_parameters:
          description:
            - Collection of operation request query parameters.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Parameter name.
              returned: always
              type: str
              sample: null
            description:
              description:
                - Parameter description.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Parameter type.
              returned: always
              type: str
              sample: null
            default_value:
              description:
                - Default parameter value.
              returned: always
              type: str
              sample: null
            required:
              description:
                - Specifies whether parameter is required or not.
              returned: always
              type: boolean
              sample: null
            values:
              description:
                - Parameter values.
              returned: always
              type: str
              sample: null
        headers:
          description:
            - Collection of operation request headers.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Parameter name.
              returned: always
              type: str
              sample: null
            description:
              description:
                - Parameter description.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Parameter type.
              returned: always
              type: str
              sample: null
            default_value:
              description:
                - Default parameter value.
              returned: always
              type: str
              sample: null
            required:
              description:
                - Specifies whether parameter is required or not.
              returned: always
              type: boolean
              sample: null
            values:
              description:
                - Parameter values.
              returned: always
              type: str
              sample: null
        representations:
          description:
            - Collection of operation request representations.
          returned: always
          type: dict
          sample: null
          contains:
            content_type:
              description:
                - >-
                  Specifies a registered or custom content type for this
                  representation, e.g. application/xml.
              returned: always
              type: str
              sample: null
            sample:
              description:
                - An example of the representation.
              returned: always
              type: str
              sample: null
            schema_id:
              description:
                - >-
                  Schema identifier. Applicable only if 'contentType' value is
                  neither 'application/x-www-form-urlencoded' nor
                  'multipart/form-data'.
              returned: always
              type: str
              sample: null
            type_name:
              description:
                - >-
                  Type name defined by the schema. Applicable only if
                  'contentType' value is neither
                  'application/x-www-form-urlencoded' nor 'multipart/form-data'.
              returned: always
              type: str
              sample: null
            form_parameters:
              description:
                - >-
                  Collection of form parameters. Required if 'contentType' value
                  is either 'application/x-www-form-urlencoded' or
                  'multipart/form-data'..
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Parameter name.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Parameter description.
                  returned: always
                  type: str
                  sample: null
                type:
                  description:
                    - Parameter type.
                  returned: always
                  type: str
                  sample: null
                default_value:
                  description:
                    - Default parameter value.
                  returned: always
                  type: str
                  sample: null
                required:
                  description:
                    - Specifies whether parameter is required or not.
                  returned: always
                  type: boolean
                  sample: null
                values:
                  description:
                    - Parameter values.
                  returned: always
                  type: str
                  sample: null
    responses:
      description:
        - Array of Operation responses.
      returned: always
      type: dict
      sample: null
      contains:
        status_code:
          description:
            - Operation response HTTP status code.
          returned: always
          type: number
          sample: null
        description:
          description:
            - Operation response description.
          returned: always
          type: str
          sample: null
        representations:
          description:
            - Collection of operation response representations.
          returned: always
          type: dict
          sample: null
          contains:
            content_type:
              description:
                - >-
                  Specifies a registered or custom content type for this
                  representation, e.g. application/xml.
              returned: always
              type: str
              sample: null
            sample:
              description:
                - An example of the representation.
              returned: always
              type: str
              sample: null
            schema_id:
              description:
                - >-
                  Schema identifier. Applicable only if 'contentType' value is
                  neither 'application/x-www-form-urlencoded' nor
                  'multipart/form-data'.
              returned: always
              type: str
              sample: null
            type_name:
              description:
                - >-
                  Type name defined by the schema. Applicable only if
                  'contentType' value is neither
                  'application/x-www-form-urlencoded' nor 'multipart/form-data'.
              returned: always
              type: str
              sample: null
            form_parameters:
              description:
                - >-
                  Collection of form parameters. Required if 'contentType' value
                  is either 'application/x-www-form-urlencoded' or
                  'multipart/form-data'..
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Parameter name.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Parameter description.
                  returned: always
                  type: str
                  sample: null
                type:
                  description:
                    - Parameter type.
                  returned: always
                  type: str
                  sample: null
                default_value:
                  description:
                    - Default parameter value.
                  returned: always
                  type: str
                  sample: null
                required:
                  description:
                    - Specifies whether parameter is required or not.
                  returned: always
                  type: boolean
                  sample: null
                values:
                  description:
                    - Parameter values.
                  returned: always
                  type: str
                  sample: null
        headers:
          description:
            - Collection of operation response headers.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Parameter name.
              returned: always
              type: str
              sample: null
            description:
              description:
                - Parameter description.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Parameter type.
              returned: always
              type: str
              sample: null
            default_value:
              description:
                - Default parameter value.
              returned: always
              type: str
              sample: null
            required:
              description:
                - Specifies whether parameter is required or not.
              returned: always
              type: boolean
              sample: null
            values:
              description:
                - Parameter values.
              returned: always
              type: str
              sample: null
    policies:
      description:
        - Operation Policies
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - Operation Name.
      returned: always
      type: str
      sample: null
    method:
      description:
        - >-
          A Valid HTTP Operation Method. Typical Http Methods like GET, PUT,
          POST but not limited by only them.
      returned: always
      type: str
      sample: null
    url_template:
      description:
        - >-
          Relative URL template identifying the target resource for this
          operation. May include parameters. Example:
          /customers/{cid}/orders/{oid}/?date={date}
      returned: always
      type: str
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


class AzureRMApiOperation(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            api_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            operation_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            template_parameters=dict(
                type='list',
                disposition='/',
                options=dict(
                    name=dict(
                        type='str',
                        required=true
                    ),
                    description=dict(
                        type='str'
                    ),
                    type=dict(
                        type='str',
                        required=true
                    ),
                    default_value=dict(
                        type='str'
                    ),
                    required=dict(
                        type='boolean'
                    ),
                    values=dict(
                        type='list'
                    )
                )
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            request=dict(
                type='dict',
                disposition='/',
                options=dict(
                    description=dict(
                        type='str'
                    ),
                    query_parameters=dict(
                        type='list',
                        options=dict(
                            name=dict(
                                type='str',
                                required=true
                            ),
                            description=dict(
                                type='str'
                            ),
                            type=dict(
                                type='str',
                                required=true
                            ),
                            default_value=dict(
                                type='str'
                            ),
                            required=dict(
                                type='boolean'
                            ),
                            values=dict(
                                type='list'
                            )
                        )
                    ),
                    headers=dict(
                        type='list',
                        options=dict(
                            name=dict(
                                type='str',
                                required=true
                            ),
                            description=dict(
                                type='str'
                            ),
                            type=dict(
                                type='str',
                                required=true
                            ),
                            default_value=dict(
                                type='str'
                            ),
                            required=dict(
                                type='boolean'
                            ),
                            values=dict(
                                type='list'
                            )
                        )
                    ),
                    representations=dict(
                        type='list',
                        options=dict(
                            content_type=dict(
                                type='str',
                                required=true
                            ),
                            sample=dict(
                                type='str'
                            ),
                            schema_id=dict(
                                type='str'
                            ),
                            type_name=dict(
                                type='str'
                            ),
                            form_parameters=dict(
                                type='list',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        required=true
                                    ),
                                    description=dict(
                                        type='str'
                                    ),
                                    type=dict(
                                        type='str',
                                        required=true
                                    ),
                                    default_value=dict(
                                        type='str'
                                    ),
                                    required=dict(
                                        type='boolean'
                                    ),
                                    values=dict(
                                        type='list'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            responses=dict(
                type='list',
                disposition='/',
                options=dict(
                    status_code=dict(
                        type='number',
                        required=true
                    ),
                    description=dict(
                        type='str'
                    ),
                    representations=dict(
                        type='list',
                        options=dict(
                            content_type=dict(
                                type='str',
                                required=true
                            ),
                            sample=dict(
                                type='str'
                            ),
                            schema_id=dict(
                                type='str'
                            ),
                            type_name=dict(
                                type='str'
                            ),
                            form_parameters=dict(
                                type='list',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        required=true
                                    ),
                                    description=dict(
                                        type='str'
                                    ),
                                    type=dict(
                                        type='str',
                                        required=true
                                    ),
                                    default_value=dict(
                                        type='str'
                                    ),
                                    required=dict(
                                        type='boolean'
                                    ),
                                    values=dict(
                                        type='list'
                                    )
                                )
                            )
                        )
                    ),
                    headers=dict(
                        type='list',
                        options=dict(
                            name=dict(
                                type='str',
                                required=true
                            ),
                            description=dict(
                                type='str'
                            ),
                            type=dict(
                                type='str',
                                required=true
                            ),
                            default_value=dict(
                                type='str'
                            ),
                            required=dict(
                                type='boolean'
                            ),
                            values=dict(
                                type='list'
                            )
                        )
                    )
                )
            ),
            policies=dict(
                type='str',
                disposition='/'
            ),
            display_name=dict(
                type='str',
                disposition='/',
                required=true
            ),
            method=dict(
                type='str',
                disposition='/',
                required=true
            ),
            url_template=dict(
                type='str',
                disposition='/',
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
        self.operation_id = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApiOperation, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.api_operation.create_or_update(resource_group_name=self.resource_group,
                                                                       service_name=self.service_name,
                                                                       api_id=self.api_id,
                                                                       operation_id=self.operation_id,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ApiOperation instance.')
            self.fail('Error creating the ApiOperation instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ApiOperation instance {0}'.format(self.))
        try:
            response = self.mgmt_client.api_operation.delete(resource_group_name=self.resource_group,
                                                             service_name=self.service_name,
                                                             api_id=self.api_id,
                                                             operation_id=self.operation_id)
        except CloudError as e:
            self.log('Error attempting to delete the ApiOperation instance.')
            self.fail('Error deleting the ApiOperation instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ApiOperation instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.api_operation.get(resource_group_name=self.resource_group,
                                                          service_name=self.service_name,
                                                          api_id=self.api_id,
                                                          operation_id=self.operation_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApiOperation()


if __name__ == '__main__':
    main()
