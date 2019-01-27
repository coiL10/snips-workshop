#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes

INTENT_ANSWER_OF_LIFE = "coiL:answer_of_life"


def main():
    with Hermes("localhost:1883") as h:
        h.subscribe_intent(INTENT_ANSWER_OF_LIFE, answer_of_life_callback) \
         .start()


def answer_of_life_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "42."
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
