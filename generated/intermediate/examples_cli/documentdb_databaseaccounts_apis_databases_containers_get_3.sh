# CosmosDBGremlinContainerGet
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
APIS_NAME="myapis"
DATABASE_NAME="mydatabase"
CONTAINER_NAME="mycontainer"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$APIS_NAME/databases/$DATABASE_NAME/containers/$CONTAINER_NAME --api-version 2015-04-08