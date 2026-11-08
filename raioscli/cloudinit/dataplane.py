# raioscli/cloudinit/dataplane.py

from pathlib import Path

SSH_PUB_KEY = (
    Path(".raios")
    / "ssh"
    / "id_ed25519.pub"
)


def generate_dataplane_user_data(node_name: str):
    ssh_key = SSH_PUB_KEY.read_text().strip()

    return f"""#cloud-config
hostname: {node_name}

users:
  - default
  - name: raios
    groups: wheel
    shell: /bin/bash
    sudo: ALL=(ALL) NOPASSWD:ALL
    lock_passwd: true
    ssh_authorized_keys:
      - {ssh_key}

disable_root: true
ssh_pwauth: false

package_update: true
package_upgrade: true

packages:
  - openssh-server

write_files:
  - path: /opt/raios/node-role
    content: dataplane

  - path: /opt/raios/node-id
    content: {node_name}

runcmd:
  - systemctl enable sshd
  - systemctl start sshd
  - mkdir -p /opt/raios
  - echo dataplane > /opt/raios/node-role
  - echo {node_name} > /opt/raios/node-id
"""
