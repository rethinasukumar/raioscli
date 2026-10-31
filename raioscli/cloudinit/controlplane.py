def generate_controlplane_user_data():

    return """#cloud-config

hostname: cp-1

users:
  - default

  - name: raios
    groups: wheel
    shell: /bin/bash
    sudo: ALL=(ALL) NOPASSWD:ALL
    lock_passwd: false
    plain_text_passwd: raios123

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
