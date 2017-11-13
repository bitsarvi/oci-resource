# OCI Object Storage Resource

A concourse resource for interacting with Oracle Cloud Infrastructure's Object Storage

This resource is based on the official [S3 resource](https://github.com/concourse/s3-resource).

## Source Configuration

* `ns` (*required*): the namespace containing the bucket

* `bucket` (*required*): the name of the bucket.

* `config` (*required*): the various [configuration entities](https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm) required by the OCI APIs. Example:
  ```
  config: |
    {
      "user": "...",
      "fingerprint": "...",
      "key_file": "...",
      "tenancy": "...",
      "region": "..."
    }
  ```

### File Names

One of the following two options must be specified:

* `regexp`: the pattern to match filenames against within a bucket. The first grouped match is used to extract the version.

  The version extracted from this pattern is used to version the resource. Semantic versions, or just numbers, are supported. Accordingly, full regular expressions are supported, to specify the capture groups.

## Behavior

### `check`: Extract versions from the bucket.

Objects will be found via the pattern configured by `regexp`. The versions will be used to order them (using [semver](http://semver.org/)). Each object's filename is the resulting version.

### `in`: Fetch an object from the bucket.

Places the following files in the destination:

* `(filename)`: the file fetched from the bucket.

* `regexp`: the pattern to match filenames against within a bucket. The first grouped match is used to extract the version.

* `version`: the version identified in the file name (only if using `regexp`).

#### Parameters

*None*

### `out`: Upload an object to the bucket.

Given a file specified by `file`, upload it to the OCI Object Storage bucket.

#### Parameters

* `file` (*required*): path to the file to upload, provided by an output of a
  task. If multiple files are matched by the glob, an error is raised. The file which matches will be placed into the directory structure on GCS as defined in `regexp` in the resource definition. The matching syntax is bash glob expansion, so no capture groups, etc.

## Example Configuration

### Resource Type

```yaml
resource_types:
  - name: ocios-resource
    type: docker-image
    source:
      repository: bitsarvi/ocios-resource
```

### Resource

``` yaml
resources:
  - name: release
    type: ocios-resource
    source:
      bucket: releases
      config: <OCI-SDK-API-CONFIG-CONTENTS>
```

### Plan

``` yaml
- get: release
```

``` yaml
- put: release
  params:
    file: path/to/release-*.tgz
```

## Developing on this resource

First get the resource via: `go get github.com/bitsarvi/ocios-resource`

Run the `unit-tests`: `make`

Run the `integration-tests`: `make integration-tests`

## Developing using Concourse
Clone this repository and just run one-off task with concourse

```bash
fly -t ConcourseTarget execute -c build.yml -i ocios-resource=. -o built-resource=.
```


Just build the Docker image to be use inside your pipeline

```bash
 docker build -t bitsarvi/ocios-resource .
```


