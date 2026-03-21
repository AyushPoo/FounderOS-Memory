#!/data/data/com.termux/files/usr/bin/bash

echo "Pulling latest..."
git pull

echo "Adding changes..."
git add .

echo "Committing..."
git commit -m "mobile sync $(date)"

echo "Pushing..."
git push

echo "Done."
