from dotenv.main import load_dotenv
import os
import base64
import glob
load_dotenv()

email_attachment_folder_path = os.environ['EMAIL_ATTACHMENT_FOLDER_PATH']

file_content_types = {
    ".txt": "text/plain",
    ".html": "text/html",
    ".css": "text/css",
    ".js": "application/javascript",
    ".json": "application/json",
    ".xml": "application/xml",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".bmp": "image/bmp",
    ".pdf": "application/pdf",
    ".doc": "application/msword",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".xls": "application/vnd.ms-excel",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".ppt": "application/vnd.ms-powerpoint",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ".zip": "application/zip",
    ".tar": "application/x-tar",
    ".gz": "application/gzip",
    ".mp3": "audio/mpeg",
    ".wav": "audio/wav",
    ".avi": "video/x-msvideo",
    ".mp4": "video/mp4",
}


def base64converter(file_path):
    with open(file_path, "rb") as attachment_file:
        return base64.b64encode(attachment_file.read())


def get_attachments():
    """
    This function gets all the attachments from the target folder and convert them into binary files\n
    Output: List of object containing 3 things:\n
    ContentType -> Type of attachment,\n
    Filename -> Attachment Name,\n
    Base64Content -> Binary content of attachment
    """

    # Use glob to get all file paths in the folder
    file_paths = glob.glob(email_attachment_folder_path + "/*")

    # attachment object list
    attachment_list = []

    # Get the file path
    for file_path in file_paths:
        attach_obj = {}
        attach_obj["content_type"] = file_content_types[os.path.splitext(
            os.path.basename(file_path))[1]]
        attach_obj["name"] = os.path.basename(file_path)

        # Read the attachment content as bytes
        attachment_content = base64converter(file_path)
        # Convert bytes to a base64-encoded string
        attach_obj["content"] = attachment_content.decode('utf-8')

        attachment_list.append(attach_obj)

    return attachment_list
