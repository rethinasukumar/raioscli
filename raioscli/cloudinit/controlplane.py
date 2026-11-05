from pathlib import Path

SSH_PUB_KEY = (
    Path(".raios")
    / "ssh"
    / "id_ed25519.pub"
)

def generate_controlplane_user_data():

    ssh_key = SSH_PUB_KEY.read_text().strip()

    return f"""#cloud-config
hostname: cp-1

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
    content: controlplane

  - path: /opt/raios/node-id
    content: cp-1

runcmd:
  - systemctl enable sshd
  - systemctl start sshd
  - mkdir -p /opt/raios
  - echo controlplane > /opt/raios/node-role
  - echo cp-1 > /opt/raios/node-id
"""
