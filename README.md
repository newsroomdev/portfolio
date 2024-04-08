# Gerald Rich Portfolio site

This is the repository for Gerald Rich's portfolio website. The site is built with Svelte and was created with [`create-svelte`](https://github.com/sveltejs/kit/tree/master/packages/create-svelte).

## Developing

After cloning the repository and installing dependencies with `npm install` (or `pnpm install` or `yarn`), you can start a development server:

```bash
npm run dev
```

Or start the server and open the app in a new browser tab:

```bash
npm run dev -- --open
```

## Building

To create a production version of the app, run:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

## Deploying

The site is deployed automatically when changes are pushed to the main branch:

```bash
git push origin main
```

The deployment process is managed by GitHub Actions. For more information, see the workflows in the `.github/workflows/` directory.

## Infrastructure

The infrastructure for this project is managed using Terraform. The terraform/ directory contains the Terraform configuration files. These files describe the resources needed for this project, such as DNS records on Cloudflare. The infrastructure can be applied using the following command:

```bash
cd terraform
terraform apply
```

Remember to initialize Terraform with `terraform init` before applying the configuration for the first time.

## Secrets

Sensitive data like API tokens are managed using environment variables. These variables are set in the shell and are automatically picked up by Terraform.

```bash
export CLOUDFLARE_API_TOKEN=TKTKTK
export CLOUDFLARE_ACCOUNT_ID=TKTKTK
```
