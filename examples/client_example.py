#!/usr/bin/env python
"""
Example usage of the LlamaAPI client.
"""
import logging
import os

from llamaapi import (
    ApiKeyAuth,
    BearerAuth,
    LoggingMiddleware,
    MemoryCache,
    RetryMiddleware,
    create_client,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def simple_client_example():
    """Basic API client example with API key auth."""
    # Get API key from environment
    api_key = os.environ.get("API_KEY", "demo-api-key")

    # Create API client
    client = create_client(
        base_url="https://api.example.com/v1",
        auth=ApiKeyAuth(api_key),
        timeout=10,
        retries=3,
    )

    # Make GET request
    response = client.get("users")
    response.raise_for_status()
    users = response.json()
    print(f"Found {len(users)} users")

    # Make POST request
    new_user = {"name": "John Doe", "email": "john.doe@example.com"}
    response = client.post("users", json=new_user)
    response.raise_for_status()
    created_user = response.json()
    print(f"Created user: {created_user['name']} (ID: {created_user['id']})")

    # Make PUT request to update user
    updated_data = {"name": "John Smith"}
    response = client.put(f"users/{created_user['id']}", json=updated_data)
    response.raise_for_status()
    updated_user = response.json()
    print(f"Updated user: {updated_user['name']}")

    # Make DELETE request
    response = client.delete(f"users/{created_user['id']}")
    response.raise_for_status()
    print(f"Deleted user with ID: {created_user['id']}")


def advanced_client_example():
    """Advanced API client example with middleware and caching."""
    # Get API key from environment
    token = os.environ.get("AUTH_TOKEN", "demo-token")

    # Create middleware stack
    middleware = [
        LoggingMiddleware(log_headers=True, log_body=True),
        RetryMiddleware(max_retries=3, backoff_factor=0.5),
    ]

    # Create API client with middleware and caching
    client = create_client(
        base_url="https://api.example.com/v1",
        auth=BearerAuth(token),
        timeout=15,
        middleware=middleware,
        cache=MemoryCache(max_size=100),
    )

    # Make GET request (will be cached)
    print("Making first request (not cached)...")
    response = client.get("products", params={"category": "electronics"})
    response.raise_for_status()
    products = response.json()
    print(f"Found {len(products)} products")

    # Make same request again (should use cache)
    print("Making second request (should use cache)...")
    response = client.get("products", params={"category": "electronics"})
    response.raise_for_status()
    products = response.json()
    print(f"Found {len(products)} products from cache")

    # Streaming response example
    print("Streaming large dataset...")
    with client.stream("GET", "large-dataset") as response:
        for chunk in response.iter_lines():
            if chunk:
                print(f"Received chunk: {len(chunk)} bytes")


def error_handling_example():
    """Example demonstrating error handling."""
    client = create_client(
        base_url="https://api.example.com/v1",
        auth=ApiKeyAuth("invalid-key"),
    )

    try:
        # This should result in an authentication error
        response = client.get("protected-resource")
        response.raise_for_status()
    except Exception as e:
        print(f"Caught error: {type(e).__name__} - {str(e)}")

    try:
        # This should result in a resource not found error
        response = client.get("nonexistent-resource")
        response.raise_for_status()
    except Exception as e:
        print(f"Caught error: {type(e).__name__} - {str(e)}")

    try:
        # This should result in a validation error
        response = client.post("users", json={"invalid": "data"})
        response.raise_for_status()
    except Exception as e:
        print(f"Caught error: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    print("=== Simple Client Example ===")
    simple_client_example()

    print("\n=== Advanced Client Example ===")
    advanced_client_example()

    print("\n=== Error Handling Example ===")
    error_handling_example()
