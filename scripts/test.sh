echo "Run code style check ..."
#sh -xe scripts/code-style-check.sh

echo "get env ACCESS_KEY_ID for test"
printenv
echo "get env ACCESS_KEY_ID for test over"

echo "Run functional tests ..."
sh -xe scripts/run-test.sh

echo "Run code coverage reports ..."
sh -xe scripts/code-coverage-report.sh

