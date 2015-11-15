import requests
import constants
from user import User
from neomodel import UniqueProperty
from reflection import Reflection
import string
from nltk.tokenize import word_tokenize
from word import Word
from neomodel.cardinality import AttemptedCardinalityViolation


def create_user(user_id):
    """
    Create a user if not already in existence, and return it.
    """
    try:
        user = User(id=user_id).save()
    except UniqueProperty:  # if the user already exists, pass
        user = User.nodes.get(id=user_id)
    return user


def create_reflection(author, reflection_id, text_blob, title):
    """
    Create a reflection object from reddit text post
    """
    try:
        reflection = Reflection(id=reflection_id, text_blob=text_blob, title=title).save()
        reflection.user.connect(author)
    except UniqueProperty:  # if a reflection has already been stored at this id, pass
        reflection = None

    return reflection


def create_words(the_reflection):
    """
    Create a list of words from reflection
    """
    word_list = list()
    for word in word_tokenize(the_reflection.text_blob):
        if word not in string.punctuation:
            try:
                word = Word(id=word.lower()).save()
            except UniqueProperty:  # if a word has already been stored at word, plot a relationship
                word = Word.nodes.get(id=word.lower())
            word.reflections.connect(the_reflection)
            word_list.append(word)
    return word_list


def get_posts():
    post_list = list()
    headers = {'User-Agent': constants.USER_AGENT}
    r = requests.get(constants.R_EGOLOCATION, headers=headers)
    for i, obj in enumerate(r.json()['data']['children']):
        # MAKE object with the shit we get back
        the_user = create_user(obj['data']['author'])
        the_reflection = create_reflection(the_user, obj['data']['id'], obj['data']['selftext'], obj['data']['title'])
        if the_reflection:
            the_words = create_words(the_reflection)


if __name__ == '__main__':
    get_posts()
