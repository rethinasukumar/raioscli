class QueueMetrics:

    def __init__(self):
        self.sent = 0
        self.received = 0
        self.deleted = 0

    def summary(self):

        return {
            "sent": self.sent,
            "received": self.received,
            "deleted": self.deleted,
        }
