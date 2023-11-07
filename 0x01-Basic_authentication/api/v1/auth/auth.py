#!/usr/bin/env python3
"""Module for auth.py"""
from flask import request
from typing import List, TypeVar

class Auth:
    """Authorize """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth"""
        return False
    def authorization_header(self, request=None) -> str:
        """Authorize header"""
        return None
    def current_user(self, request=None) -> TypeVar('User'):
        """Current user """
        return None
    