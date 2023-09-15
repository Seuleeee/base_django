from pygelf import GelfHttpHandler


class CustomGelfHttpHandler(
    GelfHttpHandler
):  # TODO: Move this to common surromind library
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection_enabled = True

    def emit(self, response):
        if self.connection_enabled:
            try:
                super().emit(response)
            except ConnectionRefusedError:
                # TODO: Think of a way to notify that pygelf logger is down.
                self.connection_enabled = False


__all__ = ("CustomGelfHttpHandler",)
