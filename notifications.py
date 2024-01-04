from winotify import Notification

def answer(text, who="Джарвіс", timeout=5, callbacks=[]):
    notification = Notification(
        app_id="Джарвіс",
        title=who,
        msg=text,
    )
    for callback in callbacks:
        notification.add_actions(callback[0], callback[1])
    notification.show()