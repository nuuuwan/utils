DIST_NAME=utils


# python3 setup.py test
# pylint src/$DIST_NAME

git add .
git commit -m "$1"
git push origin main

open https://github.com/nuuuwan/$DIST_NAME
