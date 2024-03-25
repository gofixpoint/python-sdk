# ExperimentEvalDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_name** | **str** |  | [optional] 
**success_threshold** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.experiment_eval_definition import ExperimentEvalDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentEvalDefinition from a JSON string
experiment_eval_definition_instance = ExperimentEvalDefinition.from_json(json)
# print the JSON string representation of the object
print(ExperimentEvalDefinition.to_json())

# convert the object into a dict
experiment_eval_definition_dict = experiment_eval_definition_instance.to_dict()
# create an instance of ExperimentEvalDefinition from a dict
experiment_eval_definition_form_dict = experiment_eval_definition.from_dict(experiment_eval_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


