#!/usr/bin/env python3
"""Module for auth.py"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authorize """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth"""
        if path is None:
            return True
        if excluded_paths is None:
            return True
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]
            if path.startswith(excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorize header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user """
        return None
