
import asyncio
import argparse
import httpx

async def send_slack_message(channel: str, message: str):
    """
    Sends a message to a Slack channel using the Slack MCP.
    """
    mcp_address = "http://localhost:8080"  # Assuming the MCP is running locally
    url = f"{mcp_address}/v1/chat.postMessage"
    payload = {
        "channel": channel,
        "text": message
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            print(f"Successfully sent report to #{channel}")
            return response.json()
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
        return None
    except htt.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a report to a Slack channel via MCP.")
    parser.add_argument("--channel", required=True, help="The Slack channel to send the report to.")
    parser.add_argument("--message", required=True, help="The message to send.")
    args = parser.parse_args()

    asyncio.run(send_slack_message(args.channel, args.message))
