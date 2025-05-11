#!/bin/bash

cd /workspaces/playwrightmcp || exit 1

# Get commit message or use default
msg="$1"
if [ -z "$msg" ]; then
  msg="🔄 Auto-sync on $(date '+%Y-%m-%d %H:%M:%S')"
fi

# Show current branch
branch=$(git rev-parse --abbrev-ref HEAD)
echo "🔍 Branch: $branch"

# Stage, commit, and push
git add .
git commit -m "$msg"
git push origin "$branch"

echo "✅ Sync complete."
