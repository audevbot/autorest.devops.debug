# Create or update specific Redirect Routing Rule
#
# This script expects that the following environment vars are set:
#
# AZURE_TENANT: your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: your Azure Active Directory Application Client ID
# AZURE_SECRET: your Azure Active Directory Application Secret
# AZURE_SUBSCRIPTION_ID: your Azure Subscription Id

import os
import traceback
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_configuration import AzureConfiguration
from msrest.service_client import ServiceClient
from msrest.polling import LROPoller
from msrestazure.polling.arm_polling import ARMPolling
from msrest.pipeline import ClientRawResponse
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
FRONT_DOOR_NAME = "myfrontdoor"
ROUTING_RULE_NAME = "myroutingrule"
FRONTEND_ENDPOINT_NAME = "myfrontendendpoint"

BODY = {
  "name": "redirectRoutingRule1",
  "properties": {
    "frontendEndpoints": [
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
      },
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
      }
    ],
    "acceptedProtocols": [
      "Https"
    ],
    "patternsToMatch": [
      "/*"
    ],
    "routeConfiguration": {
      "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorRedirectConfiguration",
      "redirectType": "Moved",
      "redirectProtocol": "HttpsOnly",
      "customHost": "www.bing.com",
      "customPath": "/api",
      "customFragment": "fragment",
      "customQueryString": "a=b"
    },
    "enabledState": "Enabled"
  }
}

API_VERSION = '2019-04-01'

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_SECRET'],
        tenant=os.environ['AZURE_TENANT']
    )
    return credentials


def run_example():
    credentials = get_credentials()

    config = AzureConfiguration('https://management.azure.com')
    service_client = ServiceClient(credentials, config)

    query_parameters = {}
    query_parameters['api-version'] = API_VERSION

    header_parameters = {}
    header_parameters['Content-Type'] = 'application/json; charset=utf-8'

    operation_config = {}
    request = service_client.put("/subscriptions/" + SUBSCRIPTION + "/resourceGroups/" + RESOURCE_GR + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_N + "/routingRules/" + ROUTING_RULE_N, query_parameters)
    response = service_client.send(request, header_parameters, BODY, **operation_config)
    print(response.text)


if __name__ == "__main__":
    run_example()