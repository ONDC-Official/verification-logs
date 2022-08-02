# Signing and Verification
Steps for signing and verification

1. Install pip3 and dependencies
```
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

2. Export request body json path:
```
export REQUEST_BODY_PATH=<request-body-jon-path>
```

3. Generate key-pairs
```
python cryptic_utils.py generate_key_pairs
```

4. Export private and public keys
```
export BPP_PRIVATE_KEY=<private_key>
export BPP_PUBLIC_KEY=<public_key>
```

5. Create authorisation header
```
python cryptic_utils.py create_authorisation_header
```

6. Verify authorisation header
```
python cryptic_utils.py verify_authorisation_header '<auth_header>'
```