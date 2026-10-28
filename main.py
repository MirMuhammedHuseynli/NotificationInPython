from PIL.ImageFile import ImageFile
from plyer import notification
from PIL import Image
filename = "images (1).jpg"
ico_filename = "icon.ico"
img = Image.open(filename)
img.save(ico_filename, format="ICO", sizes=[(256, 256)])
notification.notify(
    title = "Reminder",
    message = "Wake up!",
    app_icon =ico_filename,
    timeout = 10,
)
