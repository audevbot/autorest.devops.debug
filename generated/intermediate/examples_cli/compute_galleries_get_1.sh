# List galleries in a resource group.
RESOURCE_GROUP="myresourcegroup"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries?api-version=2019-03-01