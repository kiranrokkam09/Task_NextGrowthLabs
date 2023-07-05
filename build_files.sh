
#!/bin/bash

echo "BUILD START"

# # Install dependencies
# npm install

# # Build your application
# npm run build

pip install -r requirements.txt

# Specify the build output directory
mkdir -p dist
mv <path-to-build-output> dist

echo "BUILD COMPLETE"
