#pycodestyle --statistics alibabacloud/  --max-line-length=100 --ignore=W391,E121,E123,E126,E226,E24,E704,W503,W504 --exclude=DescribeEndpointsRequest.py,vendored,clients,services
pycodestyle --statistics tests/  --max-line-length=100 --ignore=W391,E121,E123,E126,E226,E24,E704,W503,W504
pycodestyle --statistics python-function-test/  --max-line-length=100 --ignore=W391,E121,E123,E126,E226,E24,E704,W503,W504

