# ApiManagementGetApiOperationPolicy
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"
OPERATION_NAME="myoperation"
POLICY_NAME="mypolicy"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME/operations/$OPERATION_NAME/policies/$POLICY_NAME --api-version 2019-01-01