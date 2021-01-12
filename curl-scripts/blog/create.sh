#!/bin/bash

curl "http://localhost:8000/blog/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "blog": {
      "title": "'"${TITLE}"'",
      "subject": "'"${SUBJECT}"'",
      "date": "'"${DATE}"'",
      "text": "'"${TEXT}"'"
    }
  }'

echo
