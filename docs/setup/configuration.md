# Configuration

- You need to have an active CRIPT user from the web app to get the API KEYS.
- CRIPT_LOG can be set to `info`, `debug`, `error`. Leaving it empty disables the logs
## Production
Create a `.env` file and copy your API KEYS from the CRIPT website->Account->Security Settings to CRIPT_API_KEY and CRIPT_STORAGE_KEY

```
CRIPT_API_KEY=API Token
CRIPT_STORAGE_KEY=Storage Token
CRIPT_LOG=
```

## Staging

```
CRIPT_API_KEY=
CRIPT_STORAGE_KEY=
CRIPT_LOG=
CRIPT_BASE_URL=https://lb-stage.mycriptapp.org/api/v1
CRIPT_STORAGE_BUCKET=cript-stage-user-data
AWS_IDENTITY_POOL_ID=us-east-1:25043452-a922-43af-b8a6-7e938a9e55c1	
AWS_COGNITO_LOGIN_PROVIDER=cognito-idp.us-east-1.amazonaws.com/us-east-1_vyK1N9p22
```