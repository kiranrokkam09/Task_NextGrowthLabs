
#!/bin/bash

echo "BUILD START"

# Install dependencies
npm install

# Build your application
npm run build

pip install -r requirements.txt

# Specify the build output directory
export VERCEL_OUTPUT_PATH=dist

echo "BUILD COMPLETE"
