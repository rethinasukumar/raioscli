from pathlib import Path
import urllib.request
import zipfile

CACHE_DIR = Path(".raios/images")

IMAGE_URL = (
    "https://cdn.amazonlinux.com/al2023/os-images/"
    "2023.12.20261029.0/hyperv/"
    "al2023-hyperv-2023.12.20261029.0-"
    "kernel-6.1-x86_64.xfs.gpt.vhdx.zip"
)

ZIP_FILE = (
    CACHE_DIR /
    "amazon-linux-2023.zip"
)


def ensure_image():

    CACHE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    existing = list(
        CACHE_DIR.glob("*.vhdx")
    )

    if existing:

        print(
            "[RAIOS] Using cached Amazon Linux image."
        )

        return str(existing[0])

    print()
    print(
        "[RAIOS] Downloading Amazon Linux..."
    )

    print(
        f"[RAIOS] URL: {IMAGE_URL}"
    )

    urllib.request.urlretrieve(
        IMAGE_URL,
        ZIP_FILE
    )

    print(
        "[RAIOS] Extracting Amazon Linux..."
    )

    with zipfile.ZipFile(
        ZIP_FILE,
        "r"
    ) as z:
        z.extractall(CACHE_DIR)

    vhdx_files = list(
        CACHE_DIR.glob("*.vhdx")
    )

    if not vhdx_files:
        raise RuntimeError(
            "No VHDX found in archive."
        )

    print(
        "[RAIOS] Amazon Linux extracted."
    )

    print(
        f"[RAIOS] Image: {vhdx_files[0]}"
    )

    return str(vhdx_files[0])