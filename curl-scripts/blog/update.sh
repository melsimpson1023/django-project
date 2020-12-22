#!/bin/bash

curl "http://localhost:8000/blog/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "blog": {
      "blogTitle": "'"${BLOGTITLE}"'",
      "description": "'"${DESCRIPTION}"'",
      "date": "'"${DATE}"'",
      "author": "'"${AUTHOR}"'",
      "blogimage": "'"${BLOGIMAGE}"'",
      "blogtext": "'"${BLOGTEXT}"'"
    }
  }'

echo
