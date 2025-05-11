#!/bin/bash

# Navigate to your project root (edit if needed)
cd /workspaces/playwrightmcp || exit 1

# Show current branch
branch=$(git rev-parse --abbrev-ref HEAD)
echo "🔍 On branch: $branch"

# Stage all changes
git add .

# Check for commit message
if [ -z "$1" ]; then
  default_msg="🔧 Auto-commit from $(date '+%Y-%m-%d %H:%M:%S')"
  echo "⚠️  No commit message provided. Using default:"
  echo "    $default_msg"
  git commit -m "$default_msg"
else
  git commit -m "$1"
fi

# Push to current branch
git push origin "$branch"
echo "✅ Pushed to $branch"
