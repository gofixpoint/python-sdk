from client import FixpointClient

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

main()
