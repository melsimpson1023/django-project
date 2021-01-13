#!/bin/bash

curl "http://localhost:8000/blogs/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
