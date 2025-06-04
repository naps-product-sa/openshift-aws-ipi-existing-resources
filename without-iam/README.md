## install policy documents

Manually created from https://docs.openshift.com/container-platform/4.14/installing/installing_aws/installing-aws-user-infra.html#installation-aws-permissions_installing-aws-user-infra

I changed `s3:HeadBucket` to `s3:ListBucket`

## policy documents

(python script requires PyYAML library, install with `pip install PyYAML` or use a python virtual environment)

The python script will take a list of yaml CredentialRequest objects and create a AWS policy document from them. Extract the CredentialRequest objects from the release image:

https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/installing_on_aws/installer-provisioned-infrastructure#installing-aws-manual-modes_installing-aws-customizations

(use the procedure above for generating the credentialrequests directory

Generate a single AWS policy for all CredentialRequests

```
python create_policy.py credentialrequests/*
```

