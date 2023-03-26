import os
root_folder = "demo/gallery/"

content = ""

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

        elements.append(
            f"""
        <a class="spotlight" href="{image_path}">
            <img src="{image_path}">
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
