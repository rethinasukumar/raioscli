from pathlib import Path

SSH_PUB_KEY = (
    Path(".raios")
    / "ssh"
    / "id_ed25519.pub"
)


def generate_controlplane_user_data():

    if not SSH_PUB_KEY.exists():
        raise RuntimeError(
            "SSH keypair not generated."
        )

    ssh_key = (
        SSH_PUB_KEY
        .read_text()
        .strip()
    )

    return f"""#cloud-config
hostname: cp-1

users:
  - default
  - name: raios
    groups: wheel
    shell: /bin/bash
    sudo: ALL=(ALL) NOPASSWD:ALL
    lock_passwd: false
    plain_text_passwd: raios123
    ssh_authorized_keys:
      - {ssh_key}

ssh_pwauth: true

chpasswd:
  expire: false

package_update: true
package_upgrade: true

write_files:
  - path: /opt/raios/node-role
    content: controlplane

  - path: /opt/raios/node-id
    content: cp-1

runcmd:
  - mkdir -p /opt/raios
  - echo controlplane > /opt/raios/node-role
  - echo cp-1 > /opt/raios/node-id
  - echo "RAIOS Controlplane Bootstrapped" > /var/log/raios-bootstrap.log
"""
