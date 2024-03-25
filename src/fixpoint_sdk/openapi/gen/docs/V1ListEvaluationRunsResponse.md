# V1ListEvaluationRunsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_runs** | [**List[V1EvaluationRun]**](V1EvaluationRun.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_list_evaluation_runs_response import V1ListEvaluationRunsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListEvaluationRunsResponse from a JSON string
v1_list_evaluation_runs_response_instance = V1ListEvaluationRunsResponse.from_json(json)
# print the JSON string representation of the object
print(V1ListEvaluationRunsResponse.to_json())

# convert the object into a dict
v1_list_evaluation_runs_response_dict = v1_list_evaluation_runs_response_instance.to_dict()
# create an instance of V1ListEvaluationRunsResponse from a dict
v1_list_evaluation_runs_response_form_dict = v1_list_evaluation_runs_response.from_dict(v1_list_evaluation_runs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


