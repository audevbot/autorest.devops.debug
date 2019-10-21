# SubscriptionCreate
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
TOPIC_NAME="mytopic"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/topics/$TOPIC_NAME/subscriptions/$SUBSCRIPTION_ID?api-version=2017-04-01 --body '
{
  "properties": {
    "enableBatchedOperations": True
  }
}
'