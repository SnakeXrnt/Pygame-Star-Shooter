#!/bin/bash

# initialize a git repository in the current directory
git init

# ask for the git remote link
read -p "Enter the git remote link for the repository: " remote_link

# add the remote link to the git repository
git remote add origin $remote_link

# stage all changes
git add .

# rename the default branch to main
git branch -M main

# make an initial commit
git commit -m "Initial commit"

git push -u origin main

# push changes to the remote repository
expect << EOF
spawn git push -u origin main
expect "Username for 'https://github.com': "
send "SnakeXrnt\n"
expect "Password for 'https://SnakeXrnt@github.com': "
send "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\n"
expect eof
EOF
