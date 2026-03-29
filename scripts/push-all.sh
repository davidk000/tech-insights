#!/bin/bash
# push-all.sh - 一次性推送到 GitHub 和 GitCode

set -e

WORKDIR="${1:-.}"
cd "$WORKDIR"

echo "=== Pushing to GitHub & GitCode ==="
git push origin master
git push gitcode master

echo "=== Done ==="
