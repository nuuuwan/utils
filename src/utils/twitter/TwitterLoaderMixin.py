import argparse


class TwitterLoaderMixin:
    @classmethod
    def from_args(cls):
        parser = argparse.ArgumentParser()
        for twtr_arg_name in [
            'twtr_api_key',
            'twtr_api_secret_key',
            'twtr_access_token',
            'twtr_access_token_secret',
        ]:
            parser.add_argument(
                '--' + twtr_arg_name,
                type=str,
                required=False,
                default=None,
            )
        args = parser.parse_args()
        return cls(
            args.twtr_api_key,
            args.twtr_api_secret_key,
            args.twtr_access_token,
            args.twtr_access_token_secret,
        )
