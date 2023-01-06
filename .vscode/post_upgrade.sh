echo 'unset DATABASE_URL' >> ~/.bashrc
echo 'unset PGHOSTADDR' >> ~/.bashrc
echo 'alias make_url="python3 $GITPOD_REPO_ROOT/.vscode/make_url.py"' >> ~/.bashrc

export POST_UPGRADE_RUN=1
source ~/.bashrc
