# V1Experiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**evaluation_definitions** | [**List[ExperimentEvalDefinition]**](ExperimentEvalDefinition.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1_experiment import V1Experiment

# TODO update the JSON string below
json = "{}"
# create an instance of V1Experiment from a JSON string
v1_experiment_instance = V1Experiment.from_json(json)
# print the JSON string representation of the object
print(V1Experiment.to_json())

# convert the object into a dict
v1_experiment_dict = v1_experiment_instance.to_dict()
# create an instance of V1Experiment from a dict
v1_experiment_form_dict = v1_experiment.from_dict(v1_experiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


