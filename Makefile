SRC_DIR = src
VIRTUAL_ENV = virtual_env
FUNCTION_NAME = fifty_sound
LAMBDA_FILE = fifty_sound.py
LAMBDA_TEST = test.py

### AWS CLI SPECIFIC
AWS_REGION = ap-northeast-1 
LAMBDA_ROLE = arn:aws:iam::728373861643:role/lambda_basic_execution
FUNCTION_HANDLER = lambda_handler

## remember to activate virtual env when developing
create_env:
	@echo "Creating virtual env dir..."
	if [ ! -d ${VIRTUAL_ENV} ]; then \
	    python3 -m venv ${VIRTUAL_ENV}; \
	fi
	@echo "Done"

build: create_package_copy_lib copy_src_to_package test_package zip

## copy dependency libs and rm unused file/dirs
create_package_copy_lib:
	if [ ! -d package ]; then \
	    mkdir -p package/tmp; \
	    cp -a ${VIRTUAL_ENV}/lib/python3.6/site-packages/* package/tmp/.; \
	    rm -rf package/tmp/pip*; \
	    rm -rf package/tmp/setuptools*; \
	    rm package/tmp/easy_install.py; \
	    rm -rf package/tmp/pkg_resources; \
	    rm -rf package/tmp/__pycache__; \
	fi

## generate zip file for uploading
copy_src_to_package:
	cp -a ${SRC_DIR}/* package/tmp/.

zip:
	rm package/tmp/${LAMBDA_TEST}
	rm -rf package/tmp/__pycache__
	cd package/tmp && zip -r ../${FUNCTION_NAME}.zip .

test_package:
	@echo "Testing package installation..."
	python3 package/tmp/${LAMBDA_TEST}
	@echo "Done"

clean:
	rm -rf package

lambda_delete:
	aws lambda delete-function \
		--function-name ${FUNCTION_NAME}

lambda_create:
	aws lambda create-function \
		--region ${AWS_REGION} \
		--function-name ${FUNCTION_NAME} \
		--zip-file fileb://./package/${FUNCTION_NAME}.zip \
		--role ${LAMBDA_ROLE} \
		--handler ${FUNCTION_NAME}.${FUNCTION_HANDLER} \
		--runtime python3.6 \
		--timeout 5 \
		--memory-size 128

