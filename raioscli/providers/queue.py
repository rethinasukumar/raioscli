from raioscli.queue.queue import Queue


class QueueProvider:

    def create(self, name):
        return Queue(name)

    def delete(self, queue):
        queue.purge()

    def status(self, queue):

        return {
            "name": queue.name,
            "messages": queue.count(),
        }
