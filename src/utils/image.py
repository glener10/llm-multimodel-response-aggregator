import os


def get_image_mime_type(input):
    _, suffix = os.path.splitext(input)
    suffix = suffix.lower()
    if suffix == ".png":
        return "image/png"
    elif suffix in [".jpg", ".jpeg"]:
        return "image/jpeg"
    else:
        raise ValueError("unsupported image type")