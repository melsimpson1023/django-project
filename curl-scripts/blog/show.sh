#!/bin/bash

curl "http://localhost:8000/blogs/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
