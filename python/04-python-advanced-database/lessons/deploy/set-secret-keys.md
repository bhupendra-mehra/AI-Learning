I'll explain each GitHub Actions secret using your existing setup: the `docker-learning` VM, the `advanced-python-database` GitHub repository, and your GHCR image registry.

These secrets allow GitHub Actions to connect to your VM, download the Docker image, and deploy the application automatically.

## 1. Where to configure the secrets

[Chapter 1: GitHub Actions Workflows | GitHub Actions Cookbook](https://images.openai.com/static-rsc-4/4mHFHuz-4KvxFxbdJ_YaEIGctZERFo6MW74a0nDpKVU6r8DdGWCuOCFZfB-0lLnATO8mGv7VFgY5pqkpie0LpS8puGcHAifuaV7GrhQLBrCfcle9mwdn_CLcE9CAXHdVmkrPnnOXto4AQ6wpEgRLzuY-qyfW9uniNqeB6ELv0yA?purpose=inline)

Open repository secrets

GitHub → `advanced-python-database` → Settings → Secrets and variables → Actions

[Open repository Actions secrets](https://github.com/bhupendra-mehra/advanced-python-database/settings/secrets/actions)

[Environment variables - Write On! with Retype](https://images.openai.com/static-rsc-4/9i7tpxcRfPFE8gyCaEZwb583j-BA-rR3vEJGP49sHMfccBZAGC382dtR0QY7ACVITk_FBM3ouahM2wzSkNKRYROionuj9FR_i-grkFitRk_L_E14CTlpLUkpxmZANx4A0ysK-gQKrBefneOhA4AE0PGspSLPTNFoQYCXJohBpWQ?purpose=inline)

Create each secret

Click New repository secret, enter the secret name and value, then click Add secret. Repeat for all five.

Do not put these values directly in `cd.yml` or commit them to your repository.

## 2. `GCP_VM_HOST` — your VM's external IP address

Source: Google Cloud Console

This tells GitHub Actions which server to connect to.

[Terraform: SAP HANA scale-up deployment guide  |  SAP on Google Cloud  |  Google Cloud Documentation](https://images.openai.com/static-rsc-4/2h5iVWv3hc22kxyZ_UmubzK0rOQJtNfwibNH5yaLbuskoUZSDRtrg29X1Ph-7fQ5Fnk9e--9Q-2U99NMdxt3tdnCxXJ_YPygRoLxlk2wiwAd1OyMoC6N4X6RQtDTN_uni8LCANbjY4hp5P2TzuCfNjrR_7oL1k00M9jQOjwpd8A?purpose=inline)

[cloud.google.com](https://cloud.google.com/sap/docs/sap-hana-deployment-guide-tf?hl=pt-BR)

How to get it

1. Open the [Google Cloud VM instances page](https://console.cloud.google.com/compute/instances).
2. Select the project containing your `docker-learning` VM.
3. Find the row named `docker-learning`.
4. Copy the value under External IP.

Example only:

```
34.123.45.67
```

In GitHub Actions secrets, create:

| Field  | Value                        |
| ------ | ---------------------------- |
| Name   | `GCP_VM_HOST`                |
| Secret | Your VM's actual external IP |

Don't use `localhost`, the VM's internal IP, or the VM name unless you have specifically configured a network route that makes it reachable.

Important: Your VM may have an ephemeral external IP, which can change after it is stopped and restarted. If it changes, update the secret. Reserving a static external IP may incur charges depending on its usage and current Google Cloud pricing, so don't reserve one just for this exercise without checking first.

## 3. `GCP_VM_USER` — the SSH login username

This is the Linux user that GitHub Actions will use to connect to your VM.

You have been working with the `docker-learning` VM and the `/home/bhupendrabce` directory. Let's verify the actual login user rather than guessing.

Run this in the VM terminal where you normally execute commands:

```
whoami
```

If it returns `bhupendrabce`, and that user can log in over SSH and run Docker commands, use:

| Field  | Value          |
| ------ | -------------- |
| Name   | `GCP_VM_USER`  |
| Secret | `bhupendrabce` |

If it returns `root`, that only tells us your current shell is root; it doesn't guarantee that direct root SSH login is enabled. Prefer a regular SSH-enabled account such as `bhupendrabce` if it is configured.

The account must be able to execute Docker commands with `sudo` without an interactive password prompt, because your workflow uses commands such as:

```
sudo docker pull ...
```

We'll verify SSH access in Step 4.

## 4. `GCP_VM_SSH_KEY` — the private SSH key

This is the most important secret because your previous workflow failed with:

```
ssh.ParsePrivateKey: ssh: no key found
```

That error indicates the SSH action could not parse the private key it received.

SSH uses a matching pair:

Private key — keep secret

Stored in GitHub as `GCP_VM_SSH_KEY`. It proves the workflow is allowed to authenticate.

Public key — installed on the VM

Stored in the SSH user's `authorized_keys` file. It allows the matching private key to authenticate.

### Step 4A: Generate a dedicated key in WSL

On your local WSL terminal, run:

```
ssh-keygen -t ed25519 -C "github-actions-deploy" \
  -f ~/.ssh/gcp_cd_deploy -N ""
```

This creates two files:

```
~/.ssh/gcp_cd_deploy       # Private key
~/.ssh/gcp_cd_deploy.pub   # Public key
```

The command creates a key without a passphrase so the automated workflow can use it non-interactively. Protect your private key carefully.

### Step 4B: Install the public key on the VM

Display the public key in WSL:

```
cat ~/.ssh/gcp_cd_deploy.pub
```

Copy the entire output. It should be a single line starting with `ssh-ed25519`.

On the VM, assuming your chosen login user is `bhupendrabce`, run:

```
sudo mkdir -p /home/bhupendrabce/.ssh
sudo nano /home/bhupendrabce/.ssh/authorized_keys
```

Paste the public key on a new line and save the file. Then run:

```
sudo chown -R bhupendrabce:bhupendrabce /home/bhupendrabce/.ssh
sudo chmod 700 /home/bhupendrabce/.ssh
sudo chmod 600 /home/bhupendrabce/.ssh/authorized_keys
```

This assumes the VM uses ordinary SSH public-key authentication. If you use Google Cloud OS Login or another managed SSH method, the setup may differ.

### Step 4C: Test the key before using GitHub Actions

From WSL, run:

```
ssh -i ~/.ssh/gcp_cd_deploy \
  -o IdentitiesOnly=yes \
  bhupendrabce@YOUR_VM_EXTERNAL_IP
```

Replace `YOUR_VM_EXTERNAL_IP` with the real IP from Step 2.

If the command connects successfully, the key pair and VM access are working. If it fails, resolve that issue before continuing.

### Step 4D: Save the private key in GitHub

In WSL, display the private key:

```
cat ~/.ssh/gcp_cd_deploy
```

Copy the complete contents. It normally starts with:

```
-----BEGIN OPENSSH PRIVATE KEY-----
```

and ends with:

```
-----END OPENSSH PRIVATE KEY-----
```

In GitHub repository secrets, create:

| Field  | Value                                               |
| ------ | --------------------------------------------------- |
| Name   | `GCP_VM_SSH_KEY`                                    |
| Secret | Entire private key, including the header and footer |

Don't paste the `.pub` file into this secret. Don't send the private key in this chat, and don't commit it to Git.

## 5. `GHCR_USERNAME` — your GitHub username

This is the account used to authenticate to GitHub Container Registry.

Your repository is:

`bhupendra-mehra/advanced-python-database`

So the username is likely `bhupendra-mehra`, provided that's your actual GitHub login username.

| Field  | Value             |
| ------ | ----------------- |
| Name   | `GHCR_USERNAME`   |
| Secret | `bhupendra-mehra` |

You can verify your username on your [GitHub profile](https://github.com/settings/profile).

This username is used for the registry login, not the VM's Linux account.

## 6. `GHCR_TOKEN` — a GitHub Personal Access Token

Your GCP VM needs permission to pull private Docker images from GHCR. A token with package-read permission provides that access.

### Step 6A: Create the token

1. Open [GitHub Personal Access Tokens — classic](https://github.com/settings/tokens).
2. Click Generate new token (classic).
3. Give it a descriptive name, such as `gcp-vm-ghcr-read`.
4. Set an expiration appropriate for your learning project.
5. Select only the `read:packages` scope.
6. Generate the token and copy it immediately.

[GitHub Packagesを用いてプライベートに自分のライブラリを公開する！ | tech-broccoli.life](https://images.openai.com/static-rsc-4/IjsFxzCTOkfuceWAgELLTavgdnT1Y8ZT1sc_iFtBEnaNdxqISt7nk_LUAhVC0rREpcRTmvsZuliS3cxlgEtkJL9BoTH4RrRk8tTZ1lhez1PMlvBwYA8cSqdNg71GeWM3ZbSn8mxg_9arZBNGaIhtAVwDUTTU1u8x43JpntfDNT0?purpose=inline)

[tech-broccoli.life](https://tech-broccoli.life/articles/engineer/use-github-packages/)

The `read:packages` scope allows the token to download packages. If your organization has additional access restrictions, you may also need to grant the token access to the package.

### Step 6B: Save it in GitHub Actions secrets

| Field  | Value               |
| ------ | ------------------- |
| Name   | `GHCR_TOKEN`        |
| Secret | The generated token |

Keep the token private. If you lose it, generate a replacement rather than trying to retrieve the original.

## 7. Final checklist

After adding all five secrets, your GitHub repository should have these exact names:

GCP_VM_HOST

VM's current external IP

GCP_VM_USER

SSH-enabled Linux username

GCP_VM_SSH_KEY

Complete private SSH key

GHCR_USERNAME

GitHub login username

GHCR_TOKEN

PAT with read:packages

5 of 5 checked

## 8. Run the deployment workflow again

Once you've configured the secrets and verified SSH access, rerun the failed workflow from GitHub Actions.

If SSH authentication succeeds but deployment fails afterward, the next error will help identify whether the problem is `sudo`, Docker permissions, GHCR authentication, or the database initialization command.

Let's do this in order: first generate the dedicated SSH key, install its public key on the VM, and test the connection. Then configure the five secrets and rerun the workflow.
