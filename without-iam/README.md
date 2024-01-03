The python script will take a list of yaml CredentialRequest objects and create a AWS policy document from them. Extract the CredentialRequest objects from the release image:

https://docs.openshift.com/container-platform/4.14/installing/installing_aws/installing-aws-customizations.html#manually-create-iam_installing-aws-customizations

Get the release image

```
$ openshift-install version
```

## 4.13

Use the release image and extract the CredentailRequests

```
$ oc adm release extract quay.io/openshift-release-dev/ocp-release:4.y.z-x86_64 \
  --credentials-requests \
  --cloud=aws
```

```
python create_policy.py .
```

## 4.14

```
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
  --to=credentialrequests
```

```
python create_policy.py credentialrequests
```
