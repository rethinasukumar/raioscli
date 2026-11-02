from pathlib import Path
import subprocess

SSH_DIR = Path(".raios/ssh")


def ensure_keypair():
    SSH_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    private_key = SSH_DIR / "id_ed25519"
    public_key = SSH_DIR / "id_ed25519.pub"

    if public_key.exists():
        return (
            str(private_key),
            str(public_key)
        )

    subprocess.run(
        [
            "ssh-keygen",
            "-t",
            "ed25519",
            "-N",
            "",
            "-f",
            str(private_key)
        ],
        check=True
    )

    print(
        "[RAIOS] SSH keypair generated."
    )

    return (
        str(private_key),
        str(public_key)
    )
