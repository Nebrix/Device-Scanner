import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXIT_SUCCESS = 0
REPO_LINK = "https://github.com/SecLabX/Device-Scanner"

def update():
    cache_dir = os.path.join(BASE_DIR, "cache")
    
    os.makedirs(cache_dir, exist_ok=True)

    os.system(f"git clone {REPO_LINK} {cache_dir}")

    cache_file = os.path.join(cache_dir, "version")

    if os.path.exists(cache_file):
        with open(cache_file, "r") as cache_data:
            cached_version = cache_data.read()
        
        version_path = os.path.join(cache_dir, "version")

        with open(version_path, "r") as version_data:
            current_version = version_data.read()

        if current_version == cached_version:
            print("You're already up to date!")

            if os.name == "nt":
                os.system(f"rmdir /s /q {cache_dir}")
            else:
                os.system(f"rm -rf {cache_dir}")
        else:
            os.system(f"git pull {REPO_LINK}")
    
    return EXIT_SUCCESS

if __name__ == "__main__":
    update()
