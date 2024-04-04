# pylint: disable=unused-variable

"""Examples using the inference router.

The inference router can send LLM inference requests to different models based
on configurable rules.
"""


from fixpoint_sdk import openapi_client, ChatRouterClient
from fixpoint_sdk.openapi.exceptions import ApiException


def main() -> None:
    """Example using inference router."""
    client = ChatRouterClient()

    # Define routing configuration
    routing_config_req = openapi_client.V1CreateRoutingConfigRequest(
        fallback_strategy=openapi_client.V1FallbackStrategy.FALLBACK_STRATEGY_NEXT,
        terminal_state=openapi_client.V1TerminalState.TERMINAL_STATE_ERROR,
        models=[
            openapi_client.V1Model(
                provider="openai",
                name="gpt-3.5-turbo-0125",
                spend_cap=openapi_client.V1SpendCap(
                    amount="0.0001",
                    currency="USD",
                    reset_interval=openapi_client.V1ResetInterval.RESET_INTERVAL_MONTHLY,
                ),
            ),
            openapi_client.V1Model(
                provider="openai",
                name="gpt-3.5-turbo-0301",
                spend_cap=openapi_client.V1SpendCap(
                    amount="0.0001",
                    currency="USD",
                    reset_interval=openapi_client.V1ResetInterval.RESET_INTERVAL_MONTHLY,
                ),
            ),
        ],
        description="This is a test routing config.",
    )

    try:
        routing_config = client.fixpoint.proxy_client.llm_proxy_create_routing_config(
            routing_config_req
        )
    except ApiException as e:
        print(
            f"Exception when calling LLMProxyApi->llm_proxy_create_routing_config: {e}\n"
        )
    print(f"Routing config created. ID = {routing_config.id}")

    try:
        completion = client.chat.completions.create(
            mode="test",
            user="some-user-id",
            trace_id="some-trace-id",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What are you?"},
            ],
        )
    except ApiException as e:
        print(f"Exception when calling ChatCompletionsApi->create: {e}\n")

    print("Received chat completion inference response.")
    print(completion.completion)


if __name__ == "__main__":
    main()
