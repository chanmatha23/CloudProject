rm -f dailyMessage-package.zip
cd package
zip -r ../dailyMessage-package.zip .
cd ..
zip -g dailyMessage-package.zip lambda_function.py
