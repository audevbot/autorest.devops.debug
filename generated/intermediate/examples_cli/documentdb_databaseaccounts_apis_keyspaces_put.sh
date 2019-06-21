# CosmosDBCassandraKeyspaceCreateUpdate
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
API_NAME="myapi"
KEYSPACE_NAME="mykeyspace"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$API_NAME/keyspaces/$KEYSPACE_NAME --api-version 2015-04-08 --is-full-object --properties '
{
  "properties": {
    "resource": {
      "id": "keyspaceName"
    },
    "options": {}
  }
}
'