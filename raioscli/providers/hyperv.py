import subprocess
import time


# --------------------------------------------------
# PowerShell Runner
# --------------------------------------------------

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
        print("Status : Available")
    else:
        print("Status : Unavailable")

    print()


# --------------------------------------------------
# Virtual Switches
# --------------------------------------------------

def list_switches():

    cmd = """
    Get-VMSwitch |
    Select-Object Name, SwitchType
    """

    return run_ps(cmd)


# --------------------------------------------------
# VM Lifecycle
# --------------------------------------------------

def create_vm(
    name,
    memory_mb=2048,
    switch_name="Default Switch"
):

    cmd = f"""
    New-VM `
        -Name "{name}" `
        -MemoryStartupBytes {memory_mb}MB `
        -Generation 2 `
        -SwitchName "{switch_name}"
    """

    return run_ps(cmd)


def start_vm(name):

    return run_ps(
        f'Start-VM -Name "{name}"'
    )


def stop_vm(name):

    return run_ps(
        f'Stop-VM -Name "{name}" -Force'
    )


def delete_vm(name):

    cmd = f"""
    Stop-VM -Name "{name}" -Force -ErrorAction SilentlyContinue
    Remove-VM -Name "{name}" -Force -ErrorAction SilentlyContinue
    """

    return run_ps(cmd)


# --------------------------------------------------
# Storage
# --------------------------------------------------

def attach_vhdx(
    vm_name,
    vhdx_path
):

    cmd = f"""
    Add-VMHardDiskDrive `
        -VMName "{vm_name}" `
        -Path "{vhdx_path}"
    """

    return run_ps(cmd)


def attach_seed_iso(
    vm_name,
    iso_path
):

    cmd = f"""
    Add-VMDvdDrive `
        -VMName "{vm_name}" `
        -Path "{iso_path}"
    """

    return run_ps(cmd)


# --------------------------------------------------
# Firmware
# --------------------------------------------------

def disable_secure_boot(vm_name):

    cmd = f"""
    Set-VMFirmware `
        -VMName "{vm_name}" `
        -EnableSecureBoot Off
    """

    return run_ps(cmd)


def set_boot_disk_first(vm_name):

    cmd = f"""
    $disk = Get-VMHardDiskDrive `
        -VMName "{vm_name}"

    Set-VMFirmware `
        -VMName "{vm_name}" `
        -FirstBootDevice $disk
    """

    return run_ps(cmd)


# --------------------------------------------------
# VM State
# --------------------------------------------------

def get_vm_state(name):

    cmd = f"""
    try {{
        (Get-VM -Name "{name}" -ErrorAction Stop).State
    }}
    catch {{
        ""
    }}
    """

    result = run_ps(cmd)

    return result.stdout.strip()


def vm_is_running(name):

    return get_vm_state(name) == "Running"


def wait_for_vm(
    name,
    timeout=60
):

    for _ in range(timeout):

        if vm_is_running(name):
            return True

        time.sleep(1)

    return False


# --------------------------------------------------
# Queries
# --------------------------------------------------

def list_vms():

    cmd = """
    Get-VM |
    Select-Object Name, State
    """

    return run_ps(cmd)


def get_vm_info(name):

    cmd = f"""
    Get-VM -Name "{name}" |
    Select-Object
        Name,
        State,
        ProcessorCount,
        MemoryStartup
    """

    return run_ps(cmd)


def get_vm_network(name):

    cmd = f"""
    Get-VMNetworkAdapter -VMName "{name}" |
    Select-Object
        VMName,
        SwitchName,
        MacAddress,
        IPAddresses
    """

    return run_ps(cmd)


# --------------------------------------------------
# RAIOS Helpers
# --------------------------------------------------

def create_controlplane_vm(
    memory_mb=2048,
    switch_name="Default Switch"
):

    return create_vm(
        "cp-1",
        memory_mb,
        switch_name
    )


def create_dataplane_vm(
    memory_mb=2048,
    switch_name="Default Switch"
):

    return create_vm(
        "dp-1",
        memory_mb,
        switch_name
    )


def start_controlplane():

    return start_vm("cp-1")


def start_dataplane():

    return start_vm("dp-1")
