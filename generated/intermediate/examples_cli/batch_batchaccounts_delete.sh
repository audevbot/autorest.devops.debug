# BatchAccountDelete
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME?api-version=2018-12-01