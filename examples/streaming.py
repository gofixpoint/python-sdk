from fixpoint_sdk import FixpointClient, ThumbsReaction

def main() -> None:
    """An example of using FixpointClient to make LLM calls and record feedback."""

    # Make sure that the enviroment variables set:
    # - `FIXPOINT_API_KEY` is set to your Fixpoint API key
    # - `OPENAI_API_KEY` is set to your normal OpenAI API key
    # Create a FixpointClient instance (uses the FIXPOINT_API_KEY env var)
    client = FixpointClient()

    # Call create method on FixpointClient instance. You can specify a user to
    # associate with the request. The user will be automatically passed through
    # to OpenAI's API.
    openai_response, fixpoint_input_log_response, fixpoint_output_log_response = (
        client.chat.completions.create(
            streaming=True,
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What are you?"},
            ],
            user="some-user-id",
        )
    )
