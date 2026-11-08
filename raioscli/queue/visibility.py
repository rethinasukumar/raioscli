class VisibilityManager:

    def __init__(self):
        self.inflight = {}

    def lock(self, message_id):
        self.inflight[message_id] = True

    def release(self, message_id):
        self.inflight.pop(message_id, None)
