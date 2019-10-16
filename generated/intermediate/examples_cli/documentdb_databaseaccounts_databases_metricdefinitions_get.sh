# CosmosDBDatabaseGetMetricDefinitions
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
DATABASE_NAME="mydatabase"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/databases/$DATABASE_NAME/metricDefinitions?api-version=2015-04-08