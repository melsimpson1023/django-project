#!/bin/bash

curl "http://localhost:8000/blogs/${ID}" \
  --include \
  --request PATCH \
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
