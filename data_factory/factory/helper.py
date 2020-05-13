class ObjectFactory:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, provider, handler):
        self.handlers[provider] = handler()

    def get_handler(self, provider):
        handler = self.handlers.get(provider)
        if not handler:
            raise ValueError(provider)
        return handler

    def get_handlers(self):
        return list(self.handlers.keys())
