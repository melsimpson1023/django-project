#!/bin/bash

curl "http://localhost:8000/blog" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
