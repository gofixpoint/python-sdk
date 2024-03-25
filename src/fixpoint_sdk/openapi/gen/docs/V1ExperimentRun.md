# V1ExperimentRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**experiment_name** | **str** | The experiment instance this run belongs to. | [optional] 
**dataset_name** | **str** | The dataset on which the experiment ran. | [optional] 
**evaluation_definitions** | [**List[ExperimentEvalDefinition]**](ExperimentEvalDefinition.md) |  | [optional] 
**evaluation_runs** | [**List[V1EvaluationRun]**](V1EvaluationRun.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.v1_experiment_run import V1ExperimentRun

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExperimentRun from a JSON string
v1_experiment_run_instance = V1ExperimentRun.from_json(json)
# print the JSON string representation of the object
print(V1ExperimentRun.to_json())

# convert the object into a dict
v1_experiment_run_dict = v1_experiment_run_instance.to_dict()
# create an instance of V1ExperimentRun from a dict
v1_experiment_run_form_dict = v1_experiment_run.from_dict(v1_experiment_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


