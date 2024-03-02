import requests
import os


class RunBot:
    def __init__(self, user_file_path, first_name):
        self.first_name = first_name
        self.API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
        self.headers = {"Authorization": "YOUR_KEY"}
        self.user_file_path = user_file_path
        self.load_prompt()

    def load_prompt(self):
        if not self.user_file_exists():
            with open("text files/malarPrompt.txt", "r",encoding="utf-8") as file:
                self.prompt_text = file.read()
                file.close()
        else:
            with open(self.user_file_path, "r",encoding="utf-8") as user_file:
                self.prompt_text = user_file.read()
                user_file.close()


    def user_file_exists(self):
        return os.path.exists(self.user_file_path)

    def print_text_after_last_occurrence(self, input_string):
        index = input_string.rfind(self.command)
        result = input_string[index + len(self.command):]
        return result


    def bot_output(self, command):
        self.command = command
        response = requests.post(self.API_URL, headers=self.headers,
                                 json={"inputs": self.prompt_text + f"\n {command}"})
        output = response.json()
        op = output[0]["generated_text"]
        output_final = self.print_text_after_last_occurrence(op)
        start = output_final.find("<|assistant|>") + len("<|assistant|>")
        end = output_final.find("<a/>")
        output_final = output_final[start:end]

        # Update prompt_text
        self.prompt_text += f"\n <|{self.first_name}|> {command} <u/> <|assistant|> {output_final} <a/>"

        with open(self.user_file_path, "w",encoding="utf-8") as user_file:
                 user_file.write(self.prompt_text.replace("user", self.first_name) + '\n')
                 user_file.close()


        return output_final

