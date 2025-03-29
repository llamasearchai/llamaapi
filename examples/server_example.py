#!/usr/bin/env python
"""
Example usage of the LlamaAPI server utilities.
"""
import asyncio
import logging
import uvicorn
from fastapi import FastAPI, Request as FastAPIRequest
from fastapi.responses import JSONResponse

from llamaapi import (
    create_api,
    HttpMethod,
    Request,
    Response,
    log_request,
    require_auth,
    validate_json_schema,
    add_cors_headers
)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create API instance
api = create_api(name="Example API", version="1.0.0")

# Sample in-memory database
users = {
    "1": {"id": "1", "name": "John Doe", "email": "john.doe@example.com"},
    "2": {"id": "2", "name": "Jane Smith", "email": "jane.smith@example.com"},
}

next_user_id = 3

# Add global middleware
api.add_middleware(log_request)

# User schema for validation
user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 2},
        "email": {"type": "string", "format": "email"},
    },
    "required": ["name", "email"],
    "additionalProperties": False,
}

# Authentication middleware example
async def auth_middleware(request: Request) -> Request:
    # Simple API key check in header
    api_key = request.headers.get("X-API-Key")
    if api_key == "secret-api-key":
        request.context["user"] = {"id": "admin", "role": "admin"}
    return request

api.add_middleware(auth_middleware)

# Route handlers
@api.route("/users", methods=HttpMethod.GET)
async def get_users(request: Request) -> Response:
    """Get all users or filter by query parameters."""
    # Check for filter parameters
    name_filter = request.query_params.get("name")
    
    if name_filter:
        filtered_users = {
            user_id: user for user_id, user in users.items() 
            if name_filter.lower() in user["name"].lower()
        }
        return Response().with_json(list(filtered_users.values()))
    
    return Response().with_json(list(users.values()))

@api.route("/users/{user_id}", methods=HttpMethod.GET)
async def get_user(request: Request) -> Response:
    """Get a single user by ID."""
    user_id = request.path_params.get("user_id")
    
    if user_id not in users:
        return Response(status_code=404).with_json(
            {"error": f"User with ID {user_id} not found", "code": "not_found"}
        )
    
    return Response().with_json(users[user_id])

@api.route(
    "/users", 
    methods=HttpMethod.POST,
    middleware=[validate_json_schema(user_schema)]
)
async def create_user(request: Request) -> Response:
    """Create a new user."""
    global next_user_id
    
    user_data = request.json()
    user_id = str(next_user_id)
    next_user_id += 1
    
    new_user = {
        "id": user_id,
        **user_data
    }
    
    users[user_id] = new_user
    
    return Response(status_code=201).with_json(new_user)

@api.route(
    "/users/{user_id}", 
    methods=HttpMethod.PUT,
    middleware=[validate_json_schema(user_schema)]
)
async def update_user(request: Request) -> Response:
    """Update an existing user."""
    user_id = request.path_params.get("user_id")
    
    if user_id not in users:
        return Response(status_code=404).with_json(
            {"error": f"User with ID {user_id} not found", "code": "not_found"}
        )
    
    user_data = request.json()
    
    # Update the user
    users[user_id] = {
        "id": user_id,
        **user_data
    }
    
    return Response().with_json(users[user_id])

@api.route("/users/{user_id}", methods=HttpMethod.DELETE)
@require_auth
async def delete_user(request: Request) -> Response:
    """Delete a user (requires authentication)."""
    user_id = request.path_params.get("user_id")
    
    if user_id not in users:
        return Response(status_code=404).with_json(
            {"error": f"User with ID {user_id} not found", "code": "not_found"}
        )
    
    # Check for admin role
    if request.context.get("user", {}).get("role") != "admin":
        return Response(status_code=403).with_json(
            {"error": "Admin role required", "code": "forbidden"}
        )
    
    # Delete the user
    deleted_user = users.pop(user_id)
    
    return Response().with_json({"message": f"User {deleted_user['name']} deleted"})

# FastAPI integration
fastapi_app = FastAPI(title="LlamaAPI Server Example")

@fastapi_app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def proxy_to_llamaapi(request: FastAPIRequest, path: str):
    """
    Proxy requests to our LlamaAPI instance.
    """
    # Build llamaapi Request from FastAPI request
    body = await request.body()
    if body:
        try:
            body = await request.json()
        except:
            pass
    
    llamaapi_request = Request(
        method=request.method,
        path=f"/{path}",
        headers=dict(request.headers),
        query_params=dict(request.query_params),
        body=body
    )
    
    # Process the request with our API
    response = await api.handle_request(llamaapi_request)
    
    # Convert to FastAPI response
    return JSONResponse(
        content=response.body,
        status_code=response.status_code,
        headers=response.headers
    )

if __name__ == "__main__":
    # Run the FastAPI app with uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000) 