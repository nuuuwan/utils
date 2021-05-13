DIST_NAME=utils
REPOSITORY=testpypi
REPOSITORY_DOMAIN=test.pypi

# REPOSITORY=pypi
# REPOSITORY_DOMAIN=pypi

# Build
python3 -m build

# Upload
python3 -m twine upload --repository $REPOSITORY dist/*

# View Project
open https://$REPOSITORY_DOMAIN.org/project/$DIST_NAME-nuuuwan/
