#!/bin/bash

curl "http://localhost:8000/blog/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "blog": {
      "blogtitle": "'"${BLOGTITLE}"'",
      "blogsubject": "'"${BLOGSUBJECT}"'",
      "date": "'"${DATE}"'",
      "author": "'"${AUTHOR}"'",
      "blogtext": "'"${BLOGTEXT}"'"
    }
  }'

echo
