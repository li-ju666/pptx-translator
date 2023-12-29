import googletrans
import deepl
# import openai


# base translator class
class BaseTranslator:
    def __init__(self, source_language, target_language):
        self.source_language = self.get_language(source_language)
        self.target_language = self.get_language(target_language)

    def translate(self, texts):
        raise NotImplementedError

    @staticmethod
    def get_language(source_language):
        raise NotImplementedError


# google translator
class GoogleTranslator(BaseTranslator):
    def __init__(self, source_language, target_language):
        super().__init__(source_language, target_language)
        self.translator = googletrans.Translator()

    def translate(self, texts):
        texts = [each.replace("\n", "") for each in texts]
        print(f"Translating text: {texts}")
        try:
            results = self.translator.translate(
                texts, src=self.source_language, dest=self.target_language)
            return [r.text for r in results]
        except Exception as e:
            print(e)
            return texts

    @staticmethod
    def get_language(source_language):
        lang_dict = {
            "chinese": "zh-CN",
            "english": "en",
            "spanish": "es",
            "french": "fr",
            "german": "de",
            "italian": "it",
        }
        return lang_dict[source_language.lower()]


# deepL translator
class DeeplTranslator(BaseTranslator):
    def __init__(
        self, source_language, target_language,
        autho_key="df4ba94a-33fb-1434-a879-6898bb4a0145:fx"
    ):
        super().__init__(source_language, target_language)

        self.translator = deepl.Translator(autho_key)

    def translate(self, texts):
        texts = [each.replace("\n", " ") for each in texts]
        print(f"Translating text: {texts}")
        try:
            results = self.translator.translate_text(
                texts, source_lang=self.source_language,
                target_lang=self.target_language)

            return [r.text for r in results]
        except Exception as e:
            print(e)
            return texts

    @staticmethod
    def get_language(source_language):
        lang_dict = {
            "chinese": "ZH",
            "english": "EN-US",
        }
        return lang_dict[source_language.lower()]


# Currently GPTTranslator is not working, due to the API limit of OpenAI

# class GPTTranslator(BaseTranslator):
#     def __init__(self, source_language, target_language):
#         super().__init__(source_language, target_language)
#         self.client = openai.OpenAI(
#             api_key="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")

#     def translate(self, texts):
#         texts = "\n".join(texts)
#         prompt = f"Translate these from {self.source_language} to {self.target_language}" + \
#             f" and strictly keep the format. Different sentences are separated by newline characters: \n{texts}"
#         print(prompt)

#         response = self.client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system",
#                     "content": "Translate texts in a PowerPoint file."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         texts = response.choices[0].text.strip().split("\n")
#         print(texts)
#         return texts

#     @staticmethod
#     def get_language(language):
#         lang_dict = {
#             "chinese": "Chinese",
#             "english": "English",
#         }
#         return lang_dict[language.lower()]


# get translator
def get_translator(source_language, target_language, translator="google"):
    translator_dict = {
        "google": GoogleTranslator,
        "deepl": DeeplTranslator,
        # "gpt": GPTTranslator,
    }
    return translator_dict[translator](source_language, target_language)
