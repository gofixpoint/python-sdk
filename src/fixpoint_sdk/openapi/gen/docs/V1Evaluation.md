# V1Evaluation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**eval_type** | [**EvaluationEvaluationType**](EvaluationEvaluationType.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_evaluation import V1Evaluation

# TODO update the JSON string below
json = "{}"
# create an instance of V1Evaluation from a JSON string
v1_evaluation_instance = V1Evaluation.from_json(json)
# print the JSON string representation of the object
print(V1Evaluation.to_json())

# convert the object into a dict
v1_evaluation_dict = v1_evaluation_instance.to_dict()
# create an instance of V1Evaluation from a dict
v1_evaluation_form_dict = v1_evaluation.from_dict(v1_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


