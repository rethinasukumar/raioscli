class Planner:
    def __init__(self):
        self.plan = [
            "create_vm",
            "attach_disk",
            "boot_vm",
        ]

    def get_plan(self):
        return self.plan
