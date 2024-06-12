import os
import hashlib
import logging
from pathlib import Path

import boto3

from .main import CriptNode

logger = logging.getLogger(__name__)


class File(CriptNode):
    def __init__(self, *args, **kwargs):
        if "source" not in kwargs:
            raise ValueError(f"'source' is a required property in {kwargs}")
        if not kwargs["source"].startswith("http"):
            file_path = Path(kwargs["source"]).resolve()
            file_hash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
            file_name, file_extension = os.path.splitext(os.path.basename(file_path))
            self.__dict__["file_path"] = file_path
            self.__dict__["obj_name"] = f"{file_hash}{file_extension}"
            # TODO clean file_name
            if "name" not in kwargs:
                kwargs["name"] = f"{file_name}{file_extension}"

        super().__init__(*args, **kwargs)

    def process_with_parent(self, uuid):
        self.__dict__["parent"] = uuid
        if not self.source.startswith("http"):
            obj_name = f"Data/{uuid}/{self.__dict__['obj_name']}"
            self.source = obj_name
            if self.get("source") != obj_name:
                logger.info(f"Uploading {self.__dict__['file_path']} ...")
                self.upload_file(self.__dict__["file_path"], obj_name)
                logger.info("Upload finished")
                self.__dict__["kwargs"]["source"] = obj_name  # override source path with obj

    def upload_file(self, file_name, object_name):
        # TODO refactor into a singleton
        auth = boto3.client("cognito-identity", region_name=os.environ.get("AWS_REGION", "us-east-1"))
        cognito_login_provider = os.environ.get(
            "AWS_COGNITO_LOGIN_PROVIDER", "cognito-idp.us-east-1.amazonaws.com/us-east-1_SZGBXPl2j"
        )
        identity_id = auth.get_id(
            IdentityPoolId=os.environ.get("AWS_IDENTITY_POOL_ID", "us-east-1:9426df38-994a-4191-86ce-3cb0ce8ac84d"),
            Logins={cognito_login_provider: os.environ.get("CRIPT_STORAGE_KEY")},
        )

        aws_credentials = auth.get_credentials_for_identity(
            IdentityId=identity_id["IdentityId"], Logins={cognito_login_provider: os.environ.get("CRIPT_STORAGE_KEY")}
        )
        aws_credentials = aws_credentials["Credentials"]
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_credentials["AccessKeyId"],
            aws_secret_access_key=aws_credentials["SecretKey"],
            aws_session_token=aws_credentials["SessionToken"],
        )

        # Upload the file
        # try:
        response = s3_client.upload_file(
            file_name, os.environ.get("CRIPT_STORAGE_BUCKET", "cript-user-data"), object_name
        )
        # except ClientError as e:
        #     logging.error(e)
        #     return False
        # return True
