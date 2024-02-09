import requests
from lib.env import get_fixpoint_api_key

BASE_URL = "https://api.fixpoint.co"

def create_openai_input_log(model_name, request, trace_id=None):
  url = '{}/v1/openai_chats/{model_name}/input_logs'.format(BASE_URL, model_name=model_name)

  requestObj = {
    'model_name': model_name,
    'messages': request['messages'],
  }

  if 'temperature' in request:
    requestObj['temperature'] = request['temperature']

  # If trace_id exists, add it to the requestObj
  if trace_id:
    requestObj['trace_id'] = trace_id

  return post_to_fixpoint(url, request)

def create_openai_output_log(model_name, input_log_results, open_ai_response, trace_id=None):

  url = '{}/v1/openai_chats/{model_name}/output_logs'.format(BASE_URL, model_name=model_name)

  # If input_log_results doesn't have id then error
  if 'name' not in input_log_results:
    raise ValueError('input_log_results must have a name')

  # If open_ai_response doesn't have id then error
  if 'id' not in open_ai_response:
    raise ValueError('open_ai_response must have an id')

  choices = []
  for choice in open_ai_response['choices']:
    choices.append({
      "index": str(choice['index']),
      "message": choice['message'],
      "finish_reason": choice['finish_reason'],
    })

  requestObj = {
    'input_name': input_log_results['name'],
    'openai_id': open_ai_response['id'],
    'model_name': model_name,
    'choices': choices,
    'usage': open_ai_response['usage'],
  }

  # If trace_id exists, add it to the requestObj
  if trace_id:
    requestObj['trace_id'] = trace_id

  return post_to_fixpoint(url, requestObj)

def post_to_fixpoint(url, reqOrRespObj):
  apiKey = get_fixpoint_api_key()
  headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer {}'.format(apiKey),
  }

  return requests.post(url, headers=headers, json=reqOrRespObj)
