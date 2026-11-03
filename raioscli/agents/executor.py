from raioscli.control.deploy import deploy_region


class Executor:
    def deploy(self):
        print("[RAIOS] Executing region deployment")
        deploy_region()
