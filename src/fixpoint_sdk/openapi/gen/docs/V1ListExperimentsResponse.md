# V1ListExperimentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiments** | [**List[V1Experiment]**](V1Experiment.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_list_experiments_response import V1ListExperimentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListExperimentsResponse from a JSON string
v1_list_experiments_response_instance = V1ListExperimentsResponse.from_json(json)
# print the JSON string representation of the object
print(V1ListExperimentsResponse.to_json())

# convert the object into a dict
v1_list_experiments_response_dict = v1_list_experiments_response_instance.to_dict()
# create an instance of V1ListExperimentsResponse from a dict
v1_list_experiments_response_form_dict = v1_list_experiments_response.from_dict(v1_list_experiments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


