# OpenShift AWS IPI Installation with Existing AWS Resources

Resources to make an IPI installation easier when using existing AWS resources

## Existing VPC

First create the VPC and subnets, the CloudFormation template came from [our docs](https://docs.openshift.com/container-platform/4.13/installing/installing_aws/installing-aws-user-infra.html#installation-cloudformation-vpc_installing-aws-user-infra)
```
aws cloudformation deploy --template-file existing-vpc/vpc.yaml --stack-name my-existing-vpc
```

This will create the VPC and create subnets in three Availabilty Zones, the output will contain the subnet
IDs that will plug into the `install-config.yaml`

install-config.yaml
```yaml
...
platform:
  aws:
    region: us-east-2
    subnets:
    - subnet-public-AZ-1
    - subnet-private-AZ-2
    - subnet-public-AZ-3
    - subnet-private-AZ-4
    - subnet-public-AZ-5
    - subnet-private-AZ-6
...
```

If you set the CloudFormation template parameter `--parameter-overrides AvailabilityZoneCount 1` then it will
only create subnets in the first Availabilty Zone and further changes will be required for the `install-config.yaml`.

```yaml
...
controlPlane:
  platform:
    aws:
      zones:
      - us-east-2a
...
compute:
- platform:
    aws:
      zones:
      - us-east-2a
...
```
