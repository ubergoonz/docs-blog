import os

def display_tree(directory, prefix=""):
    icons = {
        "folder": "📂",
        "file": "📄"
    }
    entries = sorted(os.listdir(directory))
    for i, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "
        icon = icons["folder"] if os.path.isdir(path) else icons["file"]
        print(f"{prefix}{connector}{icon} {entry}")
        if os.path.isdir(path):
            new_prefix = "    " if is_last else "│   "
            display_tree(path, prefix + new_prefix)

# Run the script
display_tree(".")