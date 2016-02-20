#!/usr/bin/env bash

PROJECT_DIR='pd2jira-python'
ZIP_FILE='lambda.zip'

echo "Installing all dependencies via pip"
pip install -r requirements.txt -t ${PROJECT_DIR} 

if [ -f ${ZIP_FILE} ]; then
    echo "Removing current file: ${ZIP_FILE}"
    rm  ${ZIP_FILE}
fi

echo "zipping project into ${ZIP_FILE}"
zip -r ${ZIP_FILE} ${PROJECT_DIR}/*

echo "${ZIP_FILE} is ready!"
