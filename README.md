# Python Starter

## Steps to set up
1. Create a new repository in GitHub using this repository as a template
2. Generate Docker Hub PAT (Personal Access Token)
3. Create repository secrets in GitHub repo
   - DOCKER_USERNAME (Docker Hub username)
   - DOCKER_PASSWORD (Docker Hub PAT)
4. Create a Docker Hub repository with the same name as the GitHub repository
5. Update `assignees` in `renovate.json` with your GitHub username
6. Set up code-cove and make sure it has access to this repository
   - https://docs.codecov.com/docs/quick-start
