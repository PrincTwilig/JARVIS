import g4f
import logging
from notifications import answer
from helpers import isCommand

class ChatGPT:
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("ChatGPT")

        self.pre_prompt = "Ти асистент Джарвіс вжийся в роль робота ассистента, відповідай на українській мові. Відповідь повинна бути дуже коротка і точна. Вот повідомлення користувача: \n\n"


    def analyze_text(self, text):
        text, is_command = isCommand(text, ["скажи", "як", "скільки", "хто", "де", "чому", "що"])

        if not is_command:
            return
        
        self.logger.info(f"Аналізуємо текст: {text}")
        
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{self.pre_prompt}{text}"}],
            stream=True,
        )

        full_response = ""
        for message in response:
            full_response += message

        self.logger.info(f"Відповідь: {full_response}")
        answer(full_response)