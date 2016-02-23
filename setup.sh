#!/usr/bin/env bash

PROJECT_DIR='pd2jira_python'
ZIP_FILE='lambda.zip'

echo "Installing all dependencies via pip"
pip install -r requirements.txt -t ${PROJECT_DIR} 

if [ -f ${ZIP_FILE} ]; then
    echo "Removing current file: ${ZIP_FILE}"
    rm  ${ZIP_FILE}
fi

echo "zipping project into ${ZIP_FILE}"
original_dir=$(pwd)
cd ${PROJECT_DIR}
zip -r ${ZIP_FILE} *
cd ${original_dir}
mv ${PROJECT_DIR}/${ZIP_FILE} .

echo "${ZIP_FILE} is ready!"
