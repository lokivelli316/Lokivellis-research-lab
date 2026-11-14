# Termux Installation — Public Keyless Research Forge

This repository is the sanitized installable build. Credentials are added **after installation** in the operator's local environment; they are not stored in Git.

## Install

```bash
cd "$HOME"
git clone https://github.com/lokivelli316/Lokivellis-research-lab.git
cd Lokivellis-research-lab
bash install_termux.sh
bash run.sh
bash verify.sh
termux-open-url http://127.0.0.1:8877
```

## Expected status before private keys / external donors

A new clean install is allowed to report:

```text
VERIFY PASS WITH ENVIRONMENT HOLDS
```

when the Research Forge front door and regression contracts pass but external donor services such as Generator Forge, TTF/PMAE, Solar Lab, MCLAB or Playground are not yet running.

That is not full-stack certification.

## After local private configuration

Generator Forge remains the paired provider broker at `127.0.0.1:8795`. The three Titan seats and dedicated math seat obtain their live provider/model bindings from the operator's local/private runtime configuration. The public repository never contains the credentials.

Full target-device certification requires:

```text
VERIFY PASS: integrated shell + donor validations
```

on the phone.


## Local credential import after installation

The public repository remains keyless. After installation, import credentials from explicit local files or scan roots into the gitignored local `.env`:

```bash
python3 scripts/configure_local_secrets.py /path/to/your/provider.env
```

or, if your existing key files are spread through a private local workspace:

```bash
python3 scripts/configure_local_secrets.py --scan-root "$HOME/your-private-key-folder"
```

The importer:

- accepts only the supported provider variable names;
- never prints credential values;
- preserves an already-configured local value over an imported duplicate;
- writes only the repository-local gitignored `.env`;
- enforces mode `600`.

This prepares the local/private runtime. Generator Forge and other paired services retain their own credential boundaries; this does not rewrite their existing configuration.
