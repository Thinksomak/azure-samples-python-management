import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


AZURE_SUBSCRIPTION_ID = "AZ_SUBID_GMAIL"

subscription_id = os.environ.get(AZURE_SUBSCRIPTION_ID, None) # your Azure Subscription Id
credentials = DefaultAzureCredential()
client = ResourceManagementClient(credentials, subscription_id)

for item in client.resource_groups.list():
    print('Name - '+item.name + "\n" + 'Resource Type - ' + item.type + "\n" + 'Location - ' + item.location)