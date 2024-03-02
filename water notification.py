from plyer import notification
title = 'MESSAGE NOTIFYING WATER'
message='Anju , Please drink water now.The time is reached out of limit.\nThank You!!!'
notification.notify(
    title=title,
    message=message,
    app_icon=None,
    timeout=10,
    toast=False
)