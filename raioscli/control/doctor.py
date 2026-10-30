from pathlib import Path
import shutil


def check_tool(tool_name):
    return shutil.which(tool_name) is not None


def doctor():

    print()
    print("RAIOS Environment Check")
    print("-" * 40)

    checks = {
        "Python": True,
        "AWS CLI": check_tool("aws"),
        "Azure CLI": check_tool("az"),
        "Google CLI": check_tool("gcloud"),
        "Region Config": Path("region.yaml").exists(),
    }

    for name, result in checks.items():
        icon = "✅" if result else "❌"
        print(f"{name:<20} {icon}")

    print()
