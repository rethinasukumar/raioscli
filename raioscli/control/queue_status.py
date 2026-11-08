def queue_status(queue):

    print()
    print("RAIOS QUEUE")
    print("-" * 40)

    print(
        f"Name     : {queue.name}"
    )

    print(
        f"Messages : {queue.count()}"
    )

    print()
