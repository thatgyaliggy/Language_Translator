"""Import IBM Language Translator"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('b1uOUJ0kiH_-Rnk8pHI5cL8uElfQkokm5nqoRozadvCc')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/\
    instances/c3658a5b-c032-4f49-9468-a676d32a1295')

def english_to_french(english_text):
    """Translates English to French"""
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def english_to_german(english_text):
    """Translates English to German"""
    translation = language_translator.translate(text=english_text, model_id='en-de').get_result()
    german_text = translation['translations'][0]['translation']
    return german_text
