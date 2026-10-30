import subprocess


def run_ps(command):

    result = subprocess.run(
        [
            "powershell",
            "-Command",
            command
        ],
        capture_output=True,
        text=True
    )

    return result


# --------------------------------------------------
# Provider Health
# --------------------------------------------------

def is_available():

    result = run_ps(
        "(Get-Service vmms).Status"
    )

    return result.returncode == 0


def provider_info():

    print()
    print("HYPER-V PROVIDER")
    print("-" * 30)

    if is_available():
        print("Status : ✅ Available")
    else:
        print("Status : ❌ Unavailable")

    print()


# --------------------------------------------------
# VM Lifecycle
# --------------------------------------------------

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
Stop-VM -Name "{name}" -Force -ErrorAction SilentlyContinue

Remove-VM -Name "{name}" -Force
'''

    return run_ps(cmd)


# --------------------------------------------------
# VM Queries
# --------------------------------------------------

def list_vms():

    cmd = '''
Get-VM |
Select-Object Name, State
'''

    return run_ps(cmd)


def get_vm_info(name):

    cmd = f'''
Get-VM -Name "{name}" |
Select-Object Name, State, ProcessorCount, MemoryStartup
'''

    return run_ps(cmd)


# --------------------------------------------------
# Future Region Support
# --------------------------------------------------

def create_controlplane_vm(memory_mb=2048):

    return create_vm(
        "cp-1",
        memory_mb
    )


def create_dataplane_vm(memory_mb=2048):

    return create_vm(
        "dp-1",
        memory_mb
    )


def start_controlplane():

    return start_vm("cp-1")


def start_dataplane():

    return start_vm("dp-1")


def stop_controlplane():

    return stop_vm("cp-1")


def stop_dataplane():

    return stop_vm("dp-1")
