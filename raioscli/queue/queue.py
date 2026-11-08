from raioscli.queue.storage import (
    load,
    save
)
from raioscli.queue.message import Message


def create_queue(name):
    save(name, [])
    print(
        f"[RAIOS] Queue created: {name}"
    )


def send_message(
    queue_name,
    body
):
    queue = load(queue_name)

    msg = Message.create(body)

    queue.append(msg.__dict__)

    save(
        queue_name,
        queue
    )

    print(
        f"[RAIOS] Message queued: {msg.id}"
    )


def receive_message(queue_name):
    queue = load(queue_name)

    if not queue:
        print(
            "[RAIOS] Queue empty"
        )
        return

    msg = queue.pop(0)

    save(
        queue_name,
        queue
    )

    print()
    print("RAIOS MESSAGE")
    print("-" * 40)
    print(f"ID   : {msg['id']}")
    print(f"Body : {msg['body']}")
