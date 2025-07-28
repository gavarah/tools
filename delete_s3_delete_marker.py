import boto3

def delete_delete_markers(bucket_name, prefix=None, profile_name=None):
    session = boto3.Session(profile_name=profile_name)
    s3 = session.client('s3')

    paginator = s3.get_paginator('list_object_versions')
    kwargs = {'Bucket': bucket_name}
    if prefix:
        kwargs['Prefix'] = prefix

    deleted_count = 0

    for page in paginator.paginate(**kwargs):
        delete_markers = page.get('DeleteMarkers', [])
        for marker in delete_markers:
            key = marker['Key']
            version_id = marker['VersionId']
            print(f"Deleting delete marker: {key} (version: {version_id})")
            s3.delete_object(Bucket=bucket_name, Key=key, VersionId=version_id)
            deleted_count += 1

    print(f"\n✅ Done. Deleted {deleted_count} delete markers.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Remove all delete markers from an S3 bucket to restore files.')
    parser.add_argument('--bucket', required=True, help='Name of the S3 bucket')
    parser.add_argument('--prefix', help='Optional prefix to limit scope (e.g., folder/subfolder/)')
    parser.add_argument('--profile', help='AWS CLI profile to use')

    args = parser.parse_args()
    delete_delete_markers(args.bucket, args.prefix, args.profile)
