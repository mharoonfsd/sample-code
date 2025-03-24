#!/usr/bin/env bash
pip install -r ./requirements.txt
pip install rasa[spacy]
python -m spacy download en_core_web_lg
python -m spacy link en_core_web_lg en
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
pip install ./custom_built_packages/tensorflow-1.14.0-cp37-cp37m-linux_x86_64.whl
