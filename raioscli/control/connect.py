import subprocess

def ssh_connect(ip):
    subprocess.run(
        [
            "ssh",
            "-i",
            ".raios/ssh/id_ed25519",
            f"raios@{ip}"
        ]
    )
