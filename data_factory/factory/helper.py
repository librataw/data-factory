class ObjectFactory:
    def __init__(self):
        self._handlers = {}

    def register_handler(self, provider, handler):
        self._handlers[provider] = handler

    def create_handler(self, provider, **kwargs):
        handler = self._handlers.get(provider)
        if not handler:
            raise ValueError(provider)
        return handler(**kwargs)

