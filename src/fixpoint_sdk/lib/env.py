import os
import typing
import sys

from .exc import InitException

def get_fixpoint_api_key(api_key: typing.Optional[str]):
  if api_key:
    return api_key
  if 'FIXPOINT_API_KEY' not in os.environ:
    print("FIXPOINT_API_KEY env variable not set.")
    raise InitException("Fixpoint API key not set")
  else:
    key = os.environ['FIXPOINT_API_KEY']
    if not key:
      print("FIXPOINT_API_KEY env variable is empty.")
      raise InitException("Fixpoint API key is empty")
    return key
 