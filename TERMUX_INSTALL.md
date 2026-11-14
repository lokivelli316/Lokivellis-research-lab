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
