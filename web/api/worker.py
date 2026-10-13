"""Cloudflare's ASGI entry point for the FastAPI app."""

from workers import asgi

from app import app

Default = asgi.entrypoint(app)
