from invoke import task


PYTHON_VERSION = "3.10"


@task
def setup(c, version=None):
    """
    Setup dev environment, requires conda
    """
    version = version or PYTHON_VERSION
    suffix = "" if version == PYTHON_VERSION else version.replace(".", "")
    env_name = f"ploomber-test{suffix}"

    c.run(f"conda create --name {env_name} python={version} --yes")
    c.run(
        'eval "$(conda shell.bash hook)" '
        f"&& conda activate {env_name} "
        "&& pip install --editable ."
    )

    print(f"Done! Activate your environment with:\nconda activate {env_name}")
