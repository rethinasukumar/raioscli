import subprocess


def run_ps(command):

    result = subprocess.run(
        ["powershell", "-Command", command],
        capture_output=True,
        text=True
    )

    return result


def create_vm(
    name,
    memory_mb=2048,
    switch_name="Default Switch"
):

    cmd = f'''
New-VM `
-Name "{name}" `
-MemoryStartupBytes {memory_mb}MB `
-Generation 2 `
-SwitchName "{switch_name}"
'''

    return run_ps(cmd)


def start_vm(name):

    cmd = f'''
Start-VM -Name "{name}"
'''

    return run_ps(cmd)


def stop_vm(name):

    cmd = f'''
Stop-VM -Name "{name}" -Force
'''

    return run_ps(cmd)


def delete_vm(name):

    cmd = f'''
Remove-VM -Name "{name}" -Force
'''

    return run_ps(cmd)


def list_vms():

    cmd = '''
Get-VM | Select-Object Name,State
'''

    return run_ps(cmd)


def provider_info():

    result = run_ps(
        "(Get-Service vmms).Status"
    )

    print()
    print("HYPER-V PROVIDER")
    print("-" * 30)

    if result.returncode == 0:
        print("Status : ✅ Available")
    else:
        print("Status : ❌ Unavailable")

    print()

def get_vm_info(name):

    cmd = f"""
Get-VM -Name "{name}" |
Select-Object Name,State,ProcessorCount,MemoryStartup
"""

    return run_ps(cmd)


def stop_vm(name):

    cmd = f"""
Stop-VM -Name "{name}" -Force
"""

    return run_ps(cmd)


def delete_vm(name):

    cmd = f"""
Stop-VM -Name "{name}" -Force -ErrorAction SilentlyContinue
Remove-VM -Name "{name}" -Force
"""

    return run_ps(cmd)
