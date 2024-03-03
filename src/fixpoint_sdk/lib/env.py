"""Utilities for setting up or parsing the configuration environment."""

import os
import typing

from .exc import InitException


def get_fixpoint_api_key(api_key: typing.Optional[str]) -> str:
    """Returns the Fixpoint API key from the environment or the argument.

    Returns the Fixpoint API key from the environment or the argument,
    preferring the argument. If no key is defined, we raise an exception.
    """
    if api_key:
        return api_key

    if "FIXPOINT_API_KEY" not in os.environ:
        print("FIXPOINT_API_KEY env variable not set.")
        raise InitException("Fixpoint API key not set")

    key = os.environ["FIXPOINT_API_KEY"]
    if not key:
        print("FIXPOINT_API_KEY env variable is empty.")
        raise InitException("Fixpoint API key is empty")
    return key
