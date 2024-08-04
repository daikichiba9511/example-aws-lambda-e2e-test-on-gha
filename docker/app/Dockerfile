FROM public.ecr.aws/lambda/python:3.10 as app

WORKDIR ${LAMBDA_TASK_ROOT}

# README.md,pyproject.tomlがないとinstall時にコケる
COPY README.md pyproject.toml requirements.lock "${LAMBDA_TASK_ROOT}"
RUN \
  python -m pip install --upgrade \
      'pip==24.2' \
      'wheel==0.43.0' \
      'setuptools==72.1.0' && \
  python -m pip install --no-cache-dir -r requirements.lock -t "${LAMBDA_TASK_ROOT}"
COPY . "${LAMBDA_TASK_ROOT}"
CMD [ "src.example_aws_lambda_e2e_test_on_gha.app.handler" ]
