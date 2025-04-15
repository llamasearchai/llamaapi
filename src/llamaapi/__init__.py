"""
LlamaAPI - Flexible API client and server utilities for LlamaSearch.ai applications.
"""

__version__ = "0.1.0"
__author__ = "Nik Jois"
__email__ = "nikjois@llamasearch.ai" = "Nik Jois"
__email__ = "nikjois@llamasearch.ai" = "Nik Jois"

from llamaapi.auth import ApiKeyAuth, BasicAuth, BearerAuth, OAuth2Auth
from llamaapi.cache import FileCache, MemoryCache, RedisCache

# Client
from llamaapi.client import ApiClient, ApiRequest, ApiResponse
from llamaapi.exceptions import (
    ApiError,
    AuthenticationError,
    AuthorizationError,
    RateLimitError,
    ResourceNotFoundError,
    ServerError,
    ValidationError,
)
from llamaapi.middleware import (
    CompressionMiddleware,
    HeadersMiddleware,
    LoggingMiddleware,
    RateLimitMiddleware,
    RetryMiddleware,
    TimingMiddleware,
)

# OpenAPI
from llamaapi.openapi import OpenAPISchema, add_openapi_route, generate_openapi_schema

# Server
from llamaapi.server import (
    API,
    HttpMethod,
    Request,
    Response,
    Route,
    add_cors_headers,
    create_api,
    log_request,
    require_auth,
    validate_json_schema,
)

__all__ = [
    # Client
    "ApiClient", 
    "ApiRequest", 
    "ApiResponse",
    "ApiKeyAuth", 
    "BearerAuth", 
    "BasicAuth", 
    "OAuth2Auth",
    "MemoryCache", 
    "FileCache", 
    "RedisCache",
    "LoggingMiddleware", 
    "RetryMiddleware", 
    "HeadersMiddleware", 
    "TimingMiddleware", 
    "CompressionMiddleware", 
    "RateLimitMiddleware",
    "ApiError", 
    "AuthenticationError", 
    "AuthorizationError", 
    "ValidationError", 
    "ResourceNotFoundError", 
    "RateLimitError", 
    "ServerError",
    
    # Server
    "Request", 
    "Response", 
    "API", 
    "Route", 
    "HttpMethod", 
    "create_api", 
    "require_auth", 
    "log_request", 
    "validate_json_schema", 
    "add_cors_headers",
    
    # OpenAPI
    "generate_openapi_schema",
    "add_openapi_route",
    "OpenAPISchema",
]

# Helper function to create a new API client instance
def create_client(
    base_url, 
    auth=None, 
    timeout=30, 
    retries=3, 
    middleware=None, 
    cache=None, 
    **kwargs
):
    """
    Create a new API client instance.
    
    Args:
        base_url: The base URL for the API.
        auth: Authentication method (instance of BaseAuth).
        timeout: Request timeout in seconds.
        retries: Number of times to retry failed requests.
        middleware: List of middleware components.
        cache: Cache implementation to use.
        **kwargs: Additional arguments to pass to ApiClient.
        
    Returns:
        An instance of ApiClient.
    """
    return ApiClient(
        base_url=base_url, 
        auth=auth, 
        timeout=timeout, 
        retries=retries, 
        middleware=middleware, 
        cache=cache, 
        **kwargs
    ) 