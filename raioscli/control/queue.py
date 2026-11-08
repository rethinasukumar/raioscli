from raioscli.providers.queue import QueueProvider
from raioscli.queue.message import create_message


provider = QueueProvider()


def queue_create(name):
    return provider.create(name)


def queue_send(queue, body):

    message = create_message(body)
    queue.send(message)

    print(
        f"[RAIOS] Message queued: {message.id}"
    )


def queue_receive(queue):

    message = queue.receive()

    if not message:
        print("[RAIOS] Queue empty")
        return

    print(message.body)

def queue_create(name):
    print(f"[RAIOS] Queue created: {name}")

def queue_list():
    print("[RAIOS] Queue list")

def queue_send(queue, message):
    print(f"[RAIOS] Sent to {queue}: {message}")

def queue_receive(queue):
    print(f"[RAIOS] Receiving from {queue}")

def queue_delete(queue):
    print(f"[RAIOS] Deleted queue: {queue}")
