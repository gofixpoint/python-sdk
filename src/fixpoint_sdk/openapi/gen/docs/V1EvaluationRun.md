# V1EvaluationRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**evaluation_name** | **str** | The evaluation we ran. | [optional] 
**log_name** | **str** | The log the evaluation ran on. | [optional] 
**dataset_name** | **str** | the optional dataset from which we pulled the log. Some EvaluationRuns are ran outside of datasets, so this isn&#39;t always set. | [optional] 
**experiment_run_name** | **str** | The optional experiment run that this evaluation run is a part of. | [optional] 
**score** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.v1_evaluation_run import V1EvaluationRun

# TODO update the JSON string below
json = "{}"
# create an instance of V1EvaluationRun from a JSON string
v1_evaluation_run_instance = V1EvaluationRun.from_json(json)
# print the JSON string representation of the object
print(V1EvaluationRun.to_json())

# convert the object into a dict
v1_evaluation_run_dict = v1_evaluation_run_instance.to_dict()
# create an instance of V1EvaluationRun from a dict
v1_evaluation_run_form_dict = v1_evaluation_run.from_dict(v1_evaluation_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


