from client import FixpointClient
from src.lib.requests import ThumbsReaction

def main():
  # Create a FixpointClient instance
  client = FixpointClient()

  # Call create method on FixpointClient instance
  client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What are you?"
      }
    ]
  )

  # Optionally, you can pass in a trace_id into a create method to associate other logs with the same trace_id
  client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What are you?"
      }
    ],
    trace_id="some-trace-id"
  )

  # Record user feedback. One user giving a thumbs up to a log, the other giving a thumbs down
  client.fixpoint.user_feedback.create({
    "likes": [
      {
        "log_name": "d5c8252c-83a4-4301-a1e4-62781509eec5", # This is an internal uuid for the log
        "thumbs_reaction": ThumbsReaction.THUMBS_UP,
        "user_id": "some-user-id", # This is the user id of the user who gave the thumbs up
      },
      {
        "log_name": "d5c8252c-83a4-4301-a1e4-62781509eec5", # This is an internal uuid for the log
        "thumbs_reaction": ThumbsReaction.THUMBS_DOWN,
        "user_id": "some-other-user-id", # This is the user id of the user who gave the thumbs down
      }
    ]
  })

  # Record an attribute
  client.fixpoint.attributes.create({
    "log_attribute": {
      "key": "conversion",
      "value": "true",
      "log_name": "d5c8252c-83a4-4301-a1e4-62781509eec5", # This is an internal uuid for the log
    }
  })

main()
