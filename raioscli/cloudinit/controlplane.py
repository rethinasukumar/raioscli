def generate_controlplane_user_data():

    return """#cloud-config

hostname: cp-1

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
  - echo "RAIOS Controlplane Bootstrapped"
"""
