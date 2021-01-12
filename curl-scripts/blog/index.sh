#!/bin/bash

curl "http://localhost:8000/blogs/" \
  --include \
  --request GET \
  --header "Content-Type: application/json" \

echo
