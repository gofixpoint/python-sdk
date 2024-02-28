import enum
import requests
import typing

BASE_URL = "https://api.fixpoint.co"

class ThumbsReaction(enum.Enum):
  THUMBS_UNSPECIFIED = 0
  THUMBS_UP = 1
  THUMBS_DOWN = 2

class OriginType(enum.Enum):
  ORIGIN_UNSPECIFIED = 0
  ORIGIN_USER_FEEDBACK = 1
  ORIGIN_ADMIN = 2

class Requester:
  api_key: str
  base_url: str

  def __init__(self, api_key: str, base_url: typing.Optional[str]):
    self.api_key = api_key
    if not base_url:
      self.base_url = BASE_URL
    else:
      self.base_url = base_url

  def create_openai_input_log(self, model_name, request, trace_id=None):
    url = '{}/v1/openai_chats/{model_name}/input_logs'.format(self.base_url, model_name=model_name)

    requestObj = {
      'model_name': model_name,
      'messages': request['messages'],
    }

    if 'user' in request:
      requestObj['user_id'] = request['user']

    if 'temperature' in request:
      requestObj['temperature'] = request['temperature']

    # If trace_id exists, add it to the requestObj
    if trace_id:
      requestObj['trace_id'] = trace_id

    return self.post_to_fixpoint(url, requestObj)


  def create_openai_output_log(self, model_name, input_log_results, open_ai_response, trace_id=None):
    url = '{}/v1/openai_chats/{model_name}/output_logs'.format(self.base_url, model_name=model_name)

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

    return self.post_to_fixpoint(url, requestObj)


  def create_user_feedback(self, request):
    url = '{}/v1/likes'.format(self.base_url)

    if 'likes' not in request:
      raise ValueError('request must have a likes')
    
    if not isinstance(request['likes'], list):
      raise ValueError('request.likes must be a list')
    
    for like in request['likes']:
      if 'log_name' not in like:
        raise ValueError('request must have a log_name')

      if 'thumbs_reaction' not in like:
        raise ValueError('request must have a thumbs_reaction')
      like['thumbs_reaction'] = like['thumbs_reaction'].value
      
      if 'user_id' not in like:
        raise ValueError('request must have a user_id')

      like['origin'] = OriginType.ORIGIN_USER_FEEDBACK.value

    return self.post_to_fixpoint(url, request)


  def create_attribute(self, request):
    url = '{}/v1/attributes'.format(self.base_url)

    if 'log_attribute' not in request:
      raise ValueError('request must have a log_attribute')
    
    log_attribute = request['log_attribute']

    if 'key' not in log_attribute:
      raise ValueError('log_attribute must have a key')
    
    if 'value' not in log_attribute:
      raise ValueError('log_attribute must have a value')
    
    if 'log_name' not in log_attribute:
      raise ValueError('log_attribute must have a log_name')
    
    return self.post_to_fixpoint(url, request)


  def post_to_fixpoint(self, url, reqOrRespObj):
    headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer {}'.format(self.api_key),
    }

    return requests.post(url, headers=headers, json=reqOrRespObj)
