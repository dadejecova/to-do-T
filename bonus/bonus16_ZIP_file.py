import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    destination_path = pathlib.Path(dest_dir, "bonus_compressed.zip")
    with zipfile.ZipFile(destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["bonus01.py", "bonus02.1.py"], dest_dir="destination")