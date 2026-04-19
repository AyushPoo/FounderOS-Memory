#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# Pitch Deck Builder — Deploy to Azure VM
# Sends all files to the Azure VM and runs setup.
# Run from your local machine or from Claude's working session.
# ─────────────────────────────────────────────────────────────────────────────

VM_HOST="20.193.252.82"
VM_USER="ayush"
REMOTE_DIR="/home/ayush/pitchdeck"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Deploying Pitch Deck Builder to Azure VM..."
echo "   Host: $VM_HOST"
echo "   Dir:  $REMOTE_DIR"
echo ""

# Create remote directory
ssh "$VM_USER@$VM_HOST" "mkdir -p $REMOTE_DIR"

# Copy all Python scripts
echo "📤 Uploading scripts..."
scp "$SCRIPT_DIR/generate_deck.py"    "$VM_USER@$VM_HOST:$REMOTE_DIR/"
scp "$SCRIPT_DIR/extract_style.py"    "$VM_USER@$VM_HOST:$REMOTE_DIR/"
scp "$SCRIPT_DIR/state_manager.py"    "$VM_USER@$VM_HOST:$REMOTE_DIR/"
scp "$SCRIPT_DIR/atlas_pitchdeck.py"  "$VM_USER@$VM_HOST:$REMOTE_DIR/"
scp "$SCRIPT_DIR/requirements.txt"    "$VM_USER@$VM_HOST:$REMOTE_DIR/"

echo "📦 Running setup on VM..."
ssh "$VM_USER@$VM_HOST" "bash $REMOTE_DIR/setup.sh"

echo ""
echo "✅ Deployment complete!"
echo ""
echo "Next steps:"
echo "1. Update Atlas system prompt with the content from ATLAS_SYSTEM_PROMPT_ADDITION.md"
echo "2. Test by messaging @Blasikenbot: 'I want to build a pitch deck'"
echo ""
echo "Manual test command:"
echo "  ssh $VM_USER@$VM_HOST python3 $REMOTE_DIR/atlas_pitchdeck.py \\"
echo "    --chat_id 7866603961 --company 'Test Co' --tagline 'Test tagline' \\"
echo "    --description 'We test things' --customer 'Testers' --market '1B' \\"
echo "    --differentiation 'We are fast' --biz_model '99/month SaaS' \\"
echo "    --traction '100 users' --team 'Alice: CEO, Bob: CTO' \\"
echo "    --ask 'Raising 500K pre-seed' --style yc"
