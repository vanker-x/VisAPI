import typing as t
from functools import cached_property

from visapi.interface._types import HTTPScheme, HTTPMethod


class Request:
    def __init__(self, scope, receive, send):
        self.scope = scope
        self.receive = receive
        self.send = send

    @property
    def path(self) -> str:
        return self.scope["path"]

    @property
    def method(self) -> HTTPMethod:
        return self.scope["method"].upper()

    @cached_property
    def query(self):
        return {}

    @property
    def http_version(self) -> str:
        return self.scope["http_version"]

    @property
    def scheme(self) -> HTTPScheme:
        return self.scope["scheme"]


