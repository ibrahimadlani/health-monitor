#!/bin/bash

# Function to add color and format
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
BLUE="\033[0;34m"
RESET="\033[0m"

# Activate virtual environment
echo -e "${BLUE}🔄 Activating virtual environment...${RESET}\n"
source ./back/venv/bin/activate

# Run tests
echo -e "${YELLOW}\t🧪 Running pytest...${RESET}"
pytest ./back --cov=./back/ > /dev/null 2>&1
if [ $? -eq 0 ]; then
  echo -e "${GREEN}\t\t✓ - All tests passed!${RESET}\n"
else
  echo -e "${RED}\t\t✗ - Some tests failed! Please fix them before committing.${RESET}\n"
  deactivate
  exit 1
fi

# Run black for code formatting
echo -e "${YELLOW}\t🖤 Running black on ./back/...${RESET}"
black ./back > /dev/null 2>&1
if [ $? -eq 0 ]; then
  echo -e "${GREEN}\t\t✓ - Code formatted successfully!${RESET}\n"
else
  echo -e "${RED}\t\t✗ - Code formatting failed! Please check black output.${RESET}"
  deactivate
  exit 1
fi

# Run pylint on core and api (merged)
echo -e "${YELLOW}\t🔍 Running pylint on ./back/core and ./back/api...${RESET}"
pylint --rcfile=./back/.pylintrc ./back/core ./back/api > /dev/null 2>&1
if [ $? -eq 0 ]; then
  echo -e "${GREEN}\t\t✓ - Pylint passed on core and api!${RESET}\n"
else
  echo -e "${RED}\t\t✗ - Pylint failed on core or api! Please fix linting issues.${RESET}"
  deactivate
  exit 1
fi

# Deactivate virtual environment
echo -e "${BLUE}🔄 Deactivating virtual environment...${RESET}"
deactivate

echo -e "\n\n${WHITE}🎉 All checks passed! Ready to commit.${RESET}"
