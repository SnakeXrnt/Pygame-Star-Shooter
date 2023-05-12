#!/bin/bash

# initialize a git repository in the current directory
git init

# ask for the git remote link
read -p "Enter the git remote link for the repository: " remote_link

# add the remote link to the git repository
git remote add origin $remote_link

# stage all changes


# rename the default branch to main
git branch -M main

git add .

# make an initial commit
git commit -m "Initial commit"

expect << EOF
spawn git push -u origin main
expect "Username for 'https://github.com': "
send "snakexrnt\n"
expect "Password for 'https://snakexrnt@github.com': "
send "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\n"
expect eof
EOF

git push -u origin main

# push changes to the remote repository
expect << EOF
spawn git push -u origin main
expect "Username for 'https://github.com': "
send "snakexrnt\n"
expect "Password for 'https://snakexrnt@github.com': "
send "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\n"
expect eof
EOF
