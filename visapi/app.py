import typing as t
from visapi.routing import router
from visapi.interface.rsgi import handler as rsgi_handler
from visapi.interface.asgi import handler as asgi_handler


class VisAPI:
    rsgi_http_handler = rsgi_handler.HTTPHandler
    rsgi_websocket_handler = rsgi_handler.WebsocketHandler
    asgi_http_handler = asgi_handler.HTTPHandler
    asgi_websocket_handler = asgi_handler.WebsocketHandler
    asgi_lifespan_handler = asgi_handler.LifeSpanHandler
    router_cls = router.Router

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.handler_mapping = dict(
            rsgi_http_handler=self.rsgi_http_handler(self),
            rsgi_ws_handler=self.rsgi_websocket_handler(self),
            asgi_http_handler=self.asgi_http_handler(self),
            asgi_websocket_handler=self.asgi_websocket_handler(self),
            asgi_lifespan_handler=self.asgi_lifespan_handler(self),
        )
        self.router = self.router_cls()

    def __call__(self, scope, receive, send):
        """
        ASGI entry-point function
        :param scope:
        :param receive:
        :param send:
        :return:
        """
        return self.handler_mapping[f"asgi_{scope['type']}_handler"](scope, receive, send)

    def __rsgi__(self, scope, proto):
        """
        RSGI entry-point function
        :param scope:
        :param proto:
        :return:
        """
        return self.handler_mapping[f"rsgi_{scope.proto}_handler"](scope, proto)
