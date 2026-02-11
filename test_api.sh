#!/bin/bash
# Test script for OctoFit Tracker API endpoints

# Get the base URL
if [ -n "$CODESPACE_NAME" ]; then
  BASE_URL="https://$CODESPACE_NAME-8000.app.github.dev"
  echo "Testing Codespace API at: $BASE_URL"
else
  BASE_URL="http://localhost:8000"
  echo "Testing Local API at: $BASE_URL"
fi

echo "============================================"
echo "Testing OctoFit Tracker API Endpoints"
echo "============================================"
echo ""

# Test API root
echo "1. Testing API Root:"
echo "   GET $BASE_URL/api/"
curl -s "$BASE_URL/api/" | python -m json.tool
echo ""
echo "-------------------------------------------"

# Test Users endpoint
echo "2. Testing Users endpoint:"
echo "   GET $BASE_URL/api/users/"
curl -s "$BASE_URL/api/users/" | python -m json.tool | head -30
echo ""
echo "-------------------------------------------"

# Test Teams endpoint
echo "3. Testing Teams endpoint:"
echo "   GET $BASE_URL/api/teams/"
curl -s "$BASE_URL/api/teams/" | python -m json.tool | head -30
echo ""
echo "-------------------------------------------"

# Test Activities endpoint
echo "4. Testing Activities endpoint:"
echo "   GET $BASE_URL/api/activities/"
curl -s "$BASE_URL/api/activities/" | python -m json.tool | head -30
echo ""
echo "-------------------------------------------"

# Test Leaderboard endpoint
echo "5. Testing Leaderboard endpoint:"
echo "   GET $BASE_URL/api/leaderboard/"
curl -s "$BASE_URL/api/leaderboard/" | python -m json.tool | head -30
echo ""
echo "-------------------------------------------"

# Test Workouts endpoint
echo "6. Testing Workouts endpoint:"
echo "   GET $BASE_URL/api/workouts/"
curl -s "$BASE_URL/api/workouts/" | python -m json.tool | head -30
echo ""
echo "-------------------------------------------"

echo ""
echo "✅ API testing complete!"
