import os
root_folder = "demo/gallery/"

content = ""

def set_thumbnail(image_path):
    thumb_path = f"{image_path}.thumb.jpg"
    result = os.system(f"convert {image_path} -thumbnail 300x300 {thumb_path}")
    if result != 0:
        raise Exception(f"failed to convert image {image_path}")
    return thumb_path

for folder in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder)

    parent_start = f"""
    <div style="display: none" id="{folder}-spotlight" class="spotlight-group" data-fit="contain" data-autohide="all" data-animation="fade" data-control="close">
"""
    parent_end = """
    </div>
"""

    elements = []
    for image in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image)
        thumb_path = set_thumbnail(image_path)

        elements.append(
            f"""
        <a class="spotlight" href="{image_path}">
            <img src="{thumb_path}">
        </a>
"""
        )

    parent = parent_start + "\n".join(elements) + parent_end

    content += parent + "\n"

with open("index.html.template") as infile:
    html = infile.read()

html = html.replace("{{content}}", content)

with open("index.html", "w") as outfile:
    outfile.write(html)
