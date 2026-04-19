#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# Pitch Deck Builder — Azure VM Setup Script
# Run this once to set up the pitch deck builder on the Azure VM.
# ─────────────────────────────────────────────────────────────────────────────
set -e

PITCHDECK_DIR="/home/ayush/pitchdeck"
echo "📂 Setting up Pitch Deck Builder at $PITCHDECK_DIR"

# Create directory
mkdir -p "$PITCHDECK_DIR"
cd "$PITCHDECK_DIR"

echo "📦 Installing Python dependencies..."
pip3 install playwright PyMuPDF python-pptx requests --break-system-packages -q

echo "🌐 Installing Playwright Chromium..."
python3 -m playwright install chromium --with-deps 2>/dev/null || {
  # Alternative: install without deps (if sudo not available)
  python3 -m playwright install chromium
  echo "⚠️  Note: If Chromium fails, run: sudo python3 -m playwright install-deps chromium"
}

echo "✅ Setup complete!"
echo ""
echo "Usage:"
echo "  python3 $PITCHDECK_DIR/atlas_pitchdeck.py \\"
echo "    --chat_id YOUR_CHAT_ID \\"
echo "    --company 'Company Name' \\"
echo "    --tagline 'Your tagline' \\"
echo "    --description 'What you do' \\"
echo "    --customer 'Target customer' \\"
echo "    --market 'Market size' \\"
echo "    --differentiation 'Your edge' \\"
echo "    --biz_model 'Revenue model' \\"
echo "    --traction 'Key metrics' \\"
echo "    --team 'Team details' \\"
echo "    --ask 'Raising amount + use' \\"
echo "    --style yc"
echo ""
echo "Styles: yc | dark | modern"
