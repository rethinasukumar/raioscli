# raioscli/agents/executor.py

from raioscli.control.bootstrap import (
    bootstrap_controlplane,
    bootstrap_dataplane
)

from raioscli.providers.hyperv import (
    delete_vm
)


class Executor:
    """
    Executes planner actions.
    """

    def execute(self, plan):

        if not plan:
            print(
                "[RAIOS] No actions required."
            )
            return

        print()
        print("RAIOS EXECUTOR")
        print("-" * 40)

        for task in plan:

            action = task["action"]
            node = task["node"]

            #
            # Heal
            #

            if action == "heal":

                print(
                    f"[RAIOS] Healing {node}"
                )

                if node == "cp-1":
                    bootstrap_controlplane()
                else:
                    bootstrap_dataplane(
                        name=node
                    )

            #
            # Scale Out
            #

            elif action == "scale_out":

                print(
                    f"[RAIOS] Scaling OUT {node}"
                )

                bootstrap_dataplane(
                    name=node
                )

            #
            # Scale In
            #

            elif action == "scale_in":

                print(
                    f"[RAIOS] Scaling IN {node}"
                )

                delete_vm(node)

            else:

                print(
                    f"[RAIOS] Unknown action: {action}"
                )

        print()
        print(
            "[RAIOS] Execution complete."
        )
