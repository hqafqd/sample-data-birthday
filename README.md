# sample-data-birthday

## generate data
```
$python3 DataGenerator.py
```

## Upload the data to AWS S3

### install aws cli
```
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /
```

### aws configure
```
$ aws configure

and enter your access key, secret access key
and then check by command

$ cat ~/.aws/credentials
```

### upload
```
$ aws s3 cp ./data s3://data-sample-birthday/ --recursive
```

### download
```
$ aws s3 cp s3://data-sample-birthday/ ./
```