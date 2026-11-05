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

    if private_key.exists() and public_key.exists():
        return (
            str(private_key),
            public_key.read_text().strip()
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

    return (
        str(private_key),
        public_key.read_text().strip()
    )
