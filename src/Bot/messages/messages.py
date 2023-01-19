



class Message:

    def __init__(self, message):
        self.message = message

    def is_valid(self):
        if self.message.from_user.is_bot:
            return False
        if self.message.content_type != 'text':
            return False
        return True

    def verify_message(self):
        pass

    def menu(self):
        return "Saber o que tem no menu /HOJE"
        