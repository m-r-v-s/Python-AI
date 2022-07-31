""" This Module contains two functions:
    - translating from Enlish Text to French Text
    - translating from French Text to English Text (Using IBM Watson)
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
lang_translator = LanguageTranslatorV3(
    version='2022-07-30',
    authenticator=authenticator
)

lang_translator.set_service_url(url)



def english_to_french(english_text):
    """Translate English Text to French Text.
    """
    if english_text is None:
        return None
    french_text_dict = lang_translator.translate(model_id= "en-fr", text=english_text).get_result()
    french_text = french_text_dict['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """Translate French Text to English Text.
    """
    if french_text is None:
        return None
    english_text_dict = lang_translator.translate(model_id= "fr-en", text=french_text).get_result()
    english_text = english_text_dict['translations'][0]['translation']
    return english_text
